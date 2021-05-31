
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BASE SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "2.1.1"
__date__ = "2019-11-07"

import logging

from gomma.session import Session


class Base(object):
    """
    AGCloud BASE Data core class .
    """

    def __init__(self, profile_name=None):
        """
        Initialize main class with this and that.
        """
        logging.info('Init Base SDK')
        s = Session(profile_name)
        host = s.config.get('agapi_host')
        self.host = host
        self.s = s

    # erp
    def getErp(self, erp_id: int, params=None):
        """
        Get ERP data.
        """
        logging.debug(f'Get erp {erp_id}')
        rq = f'{self.host}/erp/{erp_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # unit of measure
    def getUoms(self, query=None):
        """Get all uoms."""
        logging.debug('Getting all unit of measure...')
        rq = f'{self.host}/settings/unitofmeasure'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getUom(self, uom_id: int, query=None):
        """
        Leggo uom da id.
        """
        logging.debug(f'Reading family {uom_id}...')
        rq = f'{self.host}/settings/unitofmeasure/{uom_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getUomFromCode(self, code: str, query=None):
        """
        Leggo uom da code.
        """
        logging.debug(f'Reading uom code {code}...')
        params = {
            'code': code
        }
        if query:
            new_params = dict(item.split("=") for item in query.split('&'))
            params = {**params, **new_params}
        rq = f'{self.host}/settings/unitofmeasure/findByCode'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # Currency
    def getCurrencies(self, query=None):
        """Get all currencies."""
        logging.debug('Getting all unit of measure...')
        rq = f'{self.host}/settings/currency'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getCurrency(self, currency_id: int, query=None):
        """
        Leggo uom da id.
        """
        logging.debug(f'Reading currency {currency_id}...')
        rq = f'{self.host}/settings/currency/{currency_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getCurrencyFromCode(self, code: str, query=None):
        """
        Get currency from code.
        """
        logging.debug(f'Reading currency code {code}...')
        params = {
            'code': code
        }
        if query:
            new_params = dict(item.split("=") for item in query.split('&'))
            params = {**params, **new_params}
        rq = f'{self.host}/settings/currency/findByCode'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

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
