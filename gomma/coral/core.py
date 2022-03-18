
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CORAL SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "3.2.1"
__date__ = "2022-03-18"

import logging

from gomma.session import Session


class Coral(object):
    """
    AGCloud CORAL Data core class .
    """

    def __init__(self, profile_name=None):
        """
        Initialize main class with this and that.
        """
        logging.debug('Init Coral SDK')
        s = Session(profile_name)
        host = s.config.get('agapi_host')
        self.host = host
        self.s = s

    # supplier

    def supplier_read(self, supplier_id: int, params: dict = {}):
        """
        Read single supplier.
        """
        logging.debug(f'Get supplier {supplier_id}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def supplier_list(self, params: dict = {}):
        """
        Read all suppliers.
        """
        logging.debug('Getting all the suppliers')
        rq = f'{self.host}/supplier'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def supplier_create(self, payload: dict):
        """
        Create new supplier.
        """
        logging.debug(f'Creating supplier {payload}')
        rq = f'{self.host}/supplier'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def supplier_by_erp(self, erp_id: int, code: str, params: dict = {}):
        """
        Get supplier from erp.
        """
        logging.debug(f'Search supplier from erp {erp_id} code {code}.')
        query = {**params, **{'erp': erp_id, 'code': f'{code}'}}
        rq = f'{self.host}/supplier/findByErp'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def supplier_update(self, supplier_id: int, payload: dict):
        """
        Update supplier.
        """
        logging.debug(f'Updating supplier {supplier_id} with {payload}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def supplier_patch(self, supplier_id: int, payload: dict):
        """
        Patch supplier data.
        """
        logging.debug(f'Patching supplier {supplier_id} with {payload}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # supplier company
    def supplier_list_company(self, supplier_id: int, params: dict = {}):
        """
        Read supplier companies.
        """
        logging.debug(f'Reading supplier {supplier_id} companies')
        rq = f'{self.host}/supplier/{supplier_id}/company'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def supplier_attach_company(self, supplier_id: int, company_id: int):
        """
        Attach company to supplier.
        """
        logging.debug(
            f'Attaching company {company_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/company'
        payload = {
            'company_id': company_id
        }
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def supplier_detach_company(self, supplier_id: int, company_id: int):
        """
        Detach company to supplier.
        """
        logging.debug(
            f'Detaching company {company_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/company/{company_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # supplier xerp

    def supplier_list_erp(self, supplier_id: int, params: dict = {}):
        """
        Read supplier erps.
        """
        logging.debug(f'Reading supplier {supplier_id} erps')
        rq = f'{self.host}/supplier/{supplier_id}/erp'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def supplier_attach_erp(self, supplier_id: int, payload: dict):
        """
        Attach erp to supplier.
        """
        logging.debug(
            f'Attaching erp {payload} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/erp'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def supplier_detach_erp(self, supplier_id: int, erp_id: int):
        """
        Detach erp to supplier.
        """
        logging.debug(f'Detaching erp {erp_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/erp/{erp_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # category

    def supplier_category_read(self, category_id: int, params: dict = {}):
        """
        Read single category.
        """
        logging.debug(f'Get supplier category {category_id}')
        rq = f'{self.host}/supplier/category/{category_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def supplier_category_list(self, params: dict = {}):
        """
        Read all supplier categories.
        """
        logging.debug('Getting all the categories')
        rq = f'{self.host}/supplier/category'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def supplier_category_create(self, payload: dict):
        """
        Create new supplier category.
        """
        logging.debug(f'Creating supplier category {payload}')
        rq = f'{self.host}/supplier/category'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def supplier_category_update(self, category_id: int, payload: dict):
        """
        Update supplier category.
        """
        logging.debug(f'Updating category {category_id} with {payload}')
        rq = f'{self.host}/supplier/category/{category_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # warehouse
    def warehouse_list(self, params: dict = {}):
        """
        Read all warehouses.
        """
        logging.debug('Reading all warehouses')
        rq = f'{self.host}/warehouse'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def warehouse_read(self, warehouse_id: int, params: dict = {}):
        """Get warehouse details."""
        logging.debug(f'Get warehouse {warehouse_id} with params {params}')
        rq = f'{self.host}/warehouse/{warehouse_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def warehouse_create(self, payload: dict):
        """ 
        Create new warehouse
        """
        logging.debug(f'Creating new warehouse {payload}')
        rq = f'{self.host}/warehouse'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def warehouse_update(self, warehouse_id: int, payload: dict):
        """ 
        Update warehouse.
        """
        logging.debug(f'Updateing warehouse {warehouse_id} - {payload}')
        rq = f'{self.host}/warehouse/{warehouse_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def warehouse_by_name(self, name: str, params: dict = {}):
        """read warehouse from name."""
        logging.debug(f'GEt warehouse from {name}')
        query = {**params, **{'name': name}}
        rq = f'{self.host}/warehouse/findByName'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def warehouse_patch(self, whs_id: int, payload: dict):
        """
        Patch warehouse.
        """
        logging.debug(f'Patching warehouse {whs_id} with {payload}')
        rq = f'{self.host}/warehouse/{whs_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)
