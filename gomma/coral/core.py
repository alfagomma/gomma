
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Coral SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.1.1"
__date__ = "2020-09-08"

import json
import logging
import time

from gomma.session import Session, parseApiError

class Coral(object):
    """
    Coral core class .
    """

    def __init__(self, profile_name=None):
        """
        Initialize main class with this and that.
        """
        logging.info('Init Coral SDK')
        s = Session(profile_name)
        host=s.config.get('agapi_host')
        self.host = f'{host}/coral'
        self.s = s

    #supplier
    def getSupplier(self, supplier_id:int, params=None):
        """
        Read single supplier.
        """
        logging.info(f'Get supplier {supplier_id}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent=self.s.getAgent()
        r = agent.get(rq, params=params)
        if 200 != r.status_code:
            return False
        supplier = json.loads(r.text)
        return supplier

    def getSuppliers(self, query=None):
        """
        Read all suppliers.
        """
        logging.info('Getting all the suppliers')
        rq = f'{self.host}/supplier'
        agent=self.s.getAgent()
        r = agent.get(rq, params=query)
        if 200 != r.status_code:
            return False
        suppliers = json.loads(r.text)
        return suppliers

    def createSupplier(self, payload):
        """
        Create new supplier.
        """
        logging.info(f'Creating supplier {payload}')
        rq = f'{self.host}/supplier'
        agent=self.s.getAgent()
        r = agent.post(rq, json=payload)
        if 201 != r.status_code:
            parseApiError(r)
            return False
        supplier = json.loads(r.text)
        logging.info('Create supplier %s' % supplier['data']['id'])
        return supplier

    def getSupplierFromExt_id(self, ext_id:int, params=None):
        """
        Get supplier from ext_id.
        """
        logging.info(f'Search supplier ext_id {ext_id}.')
        payload ={
            'ext_id' : ext_id
        }
        if params:
            new_payload = dict(supplier.split("=") for supplier in params.split('&'))
            payload = {**payload, **new_payload}        
        rq = f'{self.host}/supplier/findByExtId'
        agent=self.s.getAgent()
        r = agent.get(rq, params=payload)
        if 200 != r.status_code:
            parseApiError(r)
            return False
        return json.loads(r.text) 
 
    def updateSupplier(self, supplier_id:int, payload):
        """
        Update supplier.
        """
        logging.info(f'Updating supplier {supplier_id} with {payload}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent=self.s.getAgent()
        r = agent.post(rq, json=payload)
        if 200 != r.status_code:
            parseApiError(r)
            return False
        return json.loads(r.text)

    #category

    def getCategory(self, category_id:int, params=None):
        """
        Read single category.
        """
        logging.info(f'Get category {category_id}')
        rq = f'{self.host}/category/{category_id}'
        agent=self.s.getAgent()
        r = agent.get(rq, params=params)
        if 200 != r.status_code:
            return False
        category = json.loads(r.text)
        return category

    def getCategories(self, query=None):
        """
        Read all category.
        """
        logging.info('Getting all the categories')
        rq = f'{self.host}/supplier'
        agent=self.s.getAgent()
        r = agent.get(rq, params=query)
        if 200 != r.status_code:
            return False
        categories = json.loads(r.text)
        return categories

    def createCategory(self, payload):
        """
        Create new category.
        """
        logging.info(f'Creating category {payload}')
        rq = f'{self.host}/category'
        agent=self.s.getAgent()
        r = agent.post(rq, json=payload)
        if 201 != r.status_code:
            parseApiError(r)
            return False
        category = json.loads(r.text)
        logging.info('Create category %s' % category['data']['id'])
        return category

    def updateCategory(self, category_id:int, payload):
        """
        Update category.
        """
        logging.info(f'Updating category {category_id} with {payload}')
        rq = f'{self.host}/category/{category_id}'
        agent=self.s.getAgent()
        r = agent.post(rq, json=payload)
        if 200 != r.status_code:
            parseApiError(r)
            return False
        return json.loads(r.text)
