
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Eb2 SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.1.3"
__date__ = "2020-01-20"

import json
import logging
import time

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
    def getCompany(self, company_id: int, params=None):
        """
        Legge un company dal suo id.
        """
        logging.info(f'Get company {company_id}')
        rq = f'{self.host}/company/{company_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCompanies(self, query=None):
        """
        Prende tutti gli companies.
        """
        logging.info('Getting all the companies')
        rq = f'{self.host}/company'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def createCompany(self, payload):
        """
        Create new company.
        """
        logging.info(f'Creating company {payload}')
        rq = f'{self.host}/company'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCompanyFromExt_id(self, ext_id: str, params=None):
        """
        Get company from ext_id.
        """
        logging.info(f'Search company ext_id {ext_id}.')
        payload = {
            'ext_id': ext_id
        }
        if params:
            new_payload = dict(company.split("=")
                               for company in params.split('&'))
            payload = {**payload, **new_payload}
        rq = f'{self.host}/company/findByExtId'
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    def updateCompany(self, company_id: int, payload):
        """
        Update company.
        """
        logging.info(f'Updating company {company_id} with {payload}')
        rq = f'{self.host}/company/{company_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)
