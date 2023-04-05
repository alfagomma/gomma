
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

    def __manageRequestResponse(self, r: requests.Response):
        """ parsing requests response"""
        logging.debug(
            f'manage requests response {r.url} ({r.elapsed}) {r.status_code}')
        response = {
            'status': r.ok == True
        }
        if not r.text:
            return response
        content = r.headers.get('content-type')
        if 'text/html' in content:
            return r.text
        elif 'application/json' in content:
            try:
                body = r.json()
            except Exception as e:
                logging.exception("Unable to parse json")
                response['status'] = False
                response['error'] = {'title': 'Unable to parse response'}
                return response

            if response.get('status'):
                try:
                    response = {**response, **body}
                except:
                    logging.exception("Unable to merge")
                    return response
            else:
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

    def __createAgent(self):
        """ Create requests session. """
        logging.debug(f'Creating new requests session')
        # recupero tokenid
        uid = self.redis.hmget(self.__cacheKey, 'uid')[0]
        if not uid:
            logging.error(f'Unknow cache key uid in {self.__cacheKey}!')
            return False
        # instanzio requests session
        agent = requests.Session()
        agent.headers.update(
            {
                'user-agent': 'Gomma-sdk',
                'Accept': 'application/json',
                'x-uid': uid
            })
        return agent

    def __createApiToken(self):
        """ retrive new api token"""
        agcloud_id = self.__credentials.get('agcloud_id')
        agcloud_secret = self.__credentials.get('agcloud_secret')
        host = self.config.get('agapi_host')
        rqToken = f'{host}/auth/token'
        rUid = requests.post(rqToken, auth=(agcloud_id, agcloud_secret))
        if 200 != rUid.status_code:
            return False
        data = json.loads(rUid.text)
        return data

    def __refreshApiToken(self, uid: str):
        """ retrive new refreshed token"""
        host = self.config.get('agapi_host')
        rqToken = f'{host}/auth/token'
        headers = {'x-uid': uid}
        r = requests.get(rqToken, headers=headers)
        if 200 != r.status_code:
            return False
        data = json.loads(r.text)
        return data

    def __setGomma(self, uid: str = None):
        """ creo nuova sessione gomma. """
        logging.debug(f'Init new session token ...')
        if uid:
            apitoken = self.__refreshApiToken(uid)
        else:
            apitoken = self.__createApiToken()
        if not apitoken:
            logging.error('Unable to read api token!')
            return False
        expire_in = apitoken['expires_in']
        uid = apitoken['access_token']
        data = {
            'uid': uid
        }
        tokenExpireAt = int(time.time()) + expire_in
        self.redis.hmset(self.__cacheKey, data)
        # sottraggo 10 secondi: meglio che scada prima ag:gomma che la authkey delle api!
        self.redis.expireat(self.__cacheKey, int(tokenExpireAt)-10)
        return True

    # devi verificare SEMPRE la chiave redis di GOMMA
    def __getGomma(self):
        """ Restituisce info della sessione gomma."""
        # esiste?
        if self.redis.exists(self.__cacheKey):
            # prima verifico scadenze
            gommattl = self.redis.ttl(self.__cacheKey)
            if gommattl < 5:
                logging.warning('gomma expired! ({}s left)'.format(gommattl))
                # crea una nuova session
                self.__setGomma()
            elif 5 <= gommattl <= 900:
                logging.warning(
                    'gomma almost expired! ({}s left)'.format(gommattl))
                # refresh session
                uid = self.redis.hmget(self.__cacheKey, 'uid')[0]
                self.__setGomma(uid)
        else:
            # creo nuovo session token
            self.__setGomma()
        # self.redis.hgetall(self.__cacheKey) # non mi serve
        return True

    def getAgent(self, csrf=None):
        """Retrive API request session."""
        logging.debug('Get request agent')
        # sempre il doublecheck stato token
        self.__getGomma()
        agent = self.__createAgent()
        if not agent:
            raise Exception('Unknow GOMMA Agent!')
        return agent

    def response(self, response):
        """ default response object from requests"""
        return self.__manageRequestResponse(response)
