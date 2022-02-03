
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GOMMA SDK for AGCloud
"""

import json
import logging
import os
import time
from sys import exit

import requests


class Session(object):
    """
    GOMMA AGCloud SDK
    Session manager.
    """

    __currentAgent = False
    __cacheKey = 'ag:gomma'

    def __init__(self, profile_name=None):
        """
        Initialize main class with this and that.
        """
        profile_name = profile_name if profile_name else 'default'
        logging.info(f'Init Gomma session -p {profile_name}')
        self.__initProfileConfig(profile_name)
        self.__initRedisInstance()

    def __initProfileConfig(self, profile_name):
        """ load profile conf"""
        import configparser
        logging.info(f'Loading profile {profile_name}')
        # Config
        config_path = os.path.expanduser('~/.agcloud/config')
        cp = configparser.ConfigParser()
        cp.read(config_path)
        if not cp.has_section(profile_name):
            logging.error(f'Unknow {profile_name} configs!')
            exit(1)
        self.config = cp[profile_name]
        # Credentials
        credentials_path = os.path.expanduser('~/.agcloud/credentials')
        ccp = configparser.ConfigParser()
        ccp.read(credentials_path)
        if not ccp.has_section(profile_name):
            logging.error(f'Unknow {profile_name} credentials!')
            exit(1)
        self.__credentials = ccp[profile_name]
        return

    def __initRedisInstance(self):
        """init redis instance. """
        from redis import Redis
        logging.info('Init redis cache instance...')
        redis_host = self.config.get('redis_host')
        redis_pass = self.__credentials.get('redis_password')
        try:
            redis_instance = Redis(
                host=redis_host, password=redis_pass, decode_responses=True)
        except:
            logging.error('Unable to create redis instance!!')
            return False
        self.redis = redis_instance
        return True

    def __getToken(self):
        """ Read session token. If not exists, it creates it. """
        logging.debug('Init reading token..')
        token = self.redis.hgetall(self.__cacheKey)
        if not token:
            token = self.__createToken()
        return token

    def __setToken(self, payload):
        """save token """
        logging.debug(f'Init set token {payload}')
        expire_in = payload['expires_in']
        uid = payload['access_token']
        token = {
            'uid': uid
        }
        tokenExpireAt = int(time.time()) + expire_in
        self.redis.hmset(self.__cacheKey, token)
        self.redis.expireat(self.__cacheKey, int(tokenExpireAt))
        return token

    def __createToken(self):
        """ Create new session token. """
        logging.debug(f'Init new session token ...')
        agcloud_id = self.__credentials.get('agcloud_id')
        agcloud_key = self.__credentials.get('agcloud_key')
        host = self.config.get('agapi_host')
        rqToken = f'{host}/auth/token'
        rUid = requests.post(rqToken, auth=(agcloud_id, agcloud_key))
        if 200 != rUid.status_code:
            return False
        responseUid = json.loads(rUid.text)
        token = self.__setToken(responseUid)
        return token

    def __refreshToken(self):
        """ Refresh current token. """
        logging.debug(f'Init refresh token ...')
        host = self.config.get('agapi_host')
        rq = f'{host}/auth/token'
        rqRefresh = self.__currentAgent.get(rq)
        if 200 != rqRefresh.status_code:
            return False
        responseRefresh = json.loads(rqRefresh.text)
        token = self.__setToken(responseRefresh)
        return token

    def __createSessionAgent(self, token=None):
        """ Create requests session. """
        logging.debug(f'Creating new requests session')
        agent = requests.Session()
        agent.headers.update(
            {'user-agent': 'Gomma-sdk', 'Accept': 'application/json'})
        if not token:
            token = self.__getToken()
            if not token:
                logging.error(f'Unable to retrive token')
                return False
        logging.debug(f'Token is {token}')
        try:
            agent.headers.update({'x-uid': token['uid']})
        except Exception:
            logging.error("Invalid token uid keys")
            return False
        logging.debug('ok, saving current agent')
        self.__currentAgent = agent
        return agent

    def __manageRequestResponse(self, r: requests.Response):
        """ parsing requests response"""
        logging.debug(
            f'manage requests response {r.url} ({r.elapsed}) {r.status_code}')
        # prima cosa: è jsonabile?
        try:
            body = r.json()
        except Exception as e:
            logging.exception("Unable to parse json")
            return False
        # procedo
        response = {}
        if r.ok:
            response['status'] = True
            response = {**response, **body}
        else:
            response['status'] = False
            __info = {}
            if 'title' in body:
                __info['title'] = body['title']
            if 'type' in body:
                __info['type'] = body['type']
            if 'errors' in body:
                __info['errors'] = body['errors']
            response['error'] = __info
        return response

    # def __manageGenericException(self, exc: Exception):
    #     """ parsing generic Exception """
    #     logging.debug('manage generic exception')
    #     response = {
    #         'status': False,
    #         'title': str(exc),
    #         'type': 'sdk-error'
    #     }
    #     return response

    def getAgent(self, csrf=None):
        """Retrive API request session."""
        logging.debug('Get request agent')
        if self.__currentAgent:
            logging.debug('Gomma has already setup agent')
            ttl = self.redis.ttl(self.__cacheKey)
            if ttl < 2:
                logging.debug('Invalid cache key')
                agent = self.__createSessionAgent()
            elif 2 <= ttl <= 900:
                refreshedToken = self.__refreshToken()
                agent = self.__createSessionAgent(refreshedToken)
            else:
                agent = self.__currentAgent
        else:
            logging.debug('self NON HA current agent')
            agent = self.__createSessionAgent()
        if not agent:
            raise Exception('Unknow GOMMA Agent!')
        return agent

    def response(self, response):
        """ default response object from requests"""
        return self.__manageRequestResponse(response)
