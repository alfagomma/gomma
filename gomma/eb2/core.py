
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Eb2 SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.2.1"
__date__ = "2021-03-07"

import logging

from gomma.session import Session


class Eb2(object):
    """
    Eb2 core class .
    """

    def __init__(self, profile_name=None):
        """
        Initialize main class with this and that.
        """
        logging.info('Init Eb2 SDK')
        s = Session(profile_name)
        host = s.config.get('agapi_host')
        self.host = f'{host}/eb2'
        self.s = s

    # company
    def getCompany(self, company_id: int, params={}):
        """
        Legge un company dal suo id.
        """
        logging.info(f'Get company {company_id}')
        rq = f'{self.host}/company/{company_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getCompanies(self, params={}):
        """
        Prende tutti gli companies.
        """
        logging.info('Getting all the companies')
        rq = f'{self.host}/company'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createCompany(self, payload):
        """
        Create new company.
        """
        logging.info(f'Creating company {payload}')
        rq = f'{self.host}/company'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getCompanyFromCode(self, code: str, params={}):
        """
        Get company from code.
        """
        logging.info(f'Search company code {code}.')
        query = {
            'code': code
        }
        payload = {**params, **query}
        rq = f'{self.host}/company/findByCode'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateCompany(self, company_id: int, payload):
        """
        Update company.
        """
        logging.info(f'Updating company {company_id} with {payload}')
        rq = f'{self.host}/company/{company_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)
