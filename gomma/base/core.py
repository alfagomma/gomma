
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BASE SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "2.1.1"
__date__ = "2019-11-07"

import json
import logging

from agbot.session import Session, parseApiError

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
        host=s.config.get('agapi_host')
        self.host = host
        self.s = s

    #erp
    def getErp(self, erp_id:int, params=None):
        """
        Get ERP data.
        """
        logging.info(f'Get erp {erp_id}')
        rq = f'{self.host}/erp/{erp_id}'
        agent=self.s.getAgent()
        r = agent.get(rq, params=params)
        if 200 != r.status_code:
            return False
        erp = json.loads(r.text)
        return erp

    #unit of measure
    def getUoms(self, query=None):
        """Get all uoms."""
        logging.info('Getting all unit of measure...')
        rq = f'{self.host}/settings/unitofmeasure'
        agent=self.s.getAgent()
        r = agent.get(rq, params=query)
        if 200 != r.status_code:
            return False
        uoms = json.loads(r.text)
        return uoms

    def getUom(self, uom_id:int, query=None):
        """
        Leggo uom da id.
        """
        logging.info(f'Reading family {uom_id}...')
        rq = f'{self.host}/settings/unitofmeasure/{uom_id}'
        agent=self.s.getAgent()
        r = agent.get(rq, params=query)
        if 200 != r.status_code:
            return False
        uom = json.loads(r.text)
        return uom

    def getUomFromCode(self, code:str, query=None):
        """
        Leggo uom da code.
        """
        logging.info(f'Reading uom code {code}...')
        params = {
            'code': code
            }
        if query:
            new_params = dict(item.split("=") for item in query.split('&'))
            params = {**params, **new_params}     
        rq = f'{self.host}/settings/unitofmeasure/findByCode'
        agent=self.s.getAgent()
        r = agent.get(rq, params=params)
        if 200 != r.status_code:
            return False
        uom = json.loads(r.text)
        return uom        

    #Currency
    def getCurrencies(self, query=None):
        """Get all currencies."""
        logging.info('Getting all unit of measure...')
        rq = f'{self.host}/settings/currency'
        agent=self.s.getAgent()
        r = agent.get(rq, params=query)
        if 200 != r.status_code:
            return False
        uoms = json.loads(r.text)
        return uoms

    def getCurrency(self, currency_id:int, query=None):
        """
        Leggo uom da id.
        """
        logging.info(f'Reading currency {currency_id}...')
        rq = f'{self.host}/settings/currency/{currency_id}'
        agent=self.s.getAgent()
        r = agent.get(rq, params=query)
        if 200 != r.status_code:
            return False
        uom = json.loads(r.text)
        return uom

    def getCurrencyFromCode(self, code:str, query=None):
        """
        Get currency from code.
        """
        logging.info(f'Reading currency code {code}...')
        params = {
            'code': code
            }
        if query:
            new_params = dict(item.split("=") for item in query.split('&'))
            params = {**params, **new_params}     
        rq = f'{self.host}/settings/currency/findByCode'
        agent=self.s.getAgent()
        r = agent.get(rq, params=params)
        if 200 != r.status_code:
            return False
        uom = json.loads(r.text)
        return uom        
