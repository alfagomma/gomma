
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Coral SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.2.1"
__date__ = "2021-03-05"

import logging

from gomma.session import Session


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
        host = s.config.get('agapi_host')
        self.host = f'{host}/coral'
        self.s = s

    # supplier
    def getSupplier(self, supplier_id: int, params={}):
        """
        Read single supplier.
        """
        logging.info(f'Get supplier {supplier_id}')
        rq = f'{self.host}/supplier/{supplier_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def listSupplier(self, params=None):
        """
        Read all suppliers.
        """
        logging.info('Getting all the suppliers')
        rq = f'{self.host}/supplier'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createSupplier(self, payload):
        """
        Create new supplier.
        """
        logging.info(f'Creating supplier {payload}')
        rq = f'{self.host}/supplier'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getSupplierFromErp(self, erp_id: int, code: str, params={}):
        """
        Get supplier from erp.
        """
        logging.info(f'Search supplier from erp {erp_id} code {code}.')
        query = {
            'erp': erp_id,
            'code': code
        }
        payload = {**params, **query}
        rq = f'{self.host}/supplier/findByErp'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateSupplier(self, supplier_id: int, payload):
        """
        Update supplier.
        """
        logging.info(f'Updating supplier {supplier_id} with {payload}')
        rq = f'{self.host}/supplier/{supplier_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def patchSupplier(self, supplier_id: int, payload):
        """
        Patch supplier data.
        """
        logging.info(f'Patching supplier {supplier_id} with {payload}')
        rq = f'{self.host}/supplier/{supplier_id}'
        try:
            agent = self.s.getAgent()
            r = agent.patch(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def listSupplierCompanies(self, supplier_id: int, params={}):
        """
        Read supplier companies.
        """
        logging.info(f'Reading supplier {supplier_id} companies')
        rq = f'{self.host}/supplier/{supplier_id}/company'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def supplierAttachCompany(self, supplier_id: int, company_id: int):
        """
        Attach company to supplier.
        """
        logging.info(
            f'Attaching company {company_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/company'
        payload = {
            'company_id': company_id
        }
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def supplierDetachCompany(self, supplier_id: int, company_id: int):
        """
        Detach company to supplier.
        """
        logging.info(
            f'Detaching company {company_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/company/{company_id}'
        try:
            agent = self.s.getAgent()
            r = agent.delete(rq)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def listSupplierErps(self, supplier_id: int, params={}):
        """
        Read supplier erps.
        """
        logging.info(f'Reading supplier {supplier_id} erps')
        rq = f'{self.host}/supplier/{supplier_id}/erp'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def supplierAttachErp(self, supplier_id: int, erp_id: int, code: str):
        """
        Attach erp to supplier.
        """
        logging.info(
            f'Attaching erp {erp_id} code {code} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/erp'
        payload = {
            'erp_id': erp_id,
            'code': code
        }
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def supplierDetachErp(self, supplier_id: int, erp_id: int):
        """
        Detach erp to supplier.
        """
        logging.info(f'Detaching erp {erp_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/erp/{erp_id}'
        try:
            agent = self.s.getAgent()
            r = agent.delete(rq)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # category

    def getSupplierCategory(self, category_id: int, params={}):
        """
        Read single category.
        """
        logging.info(f'Get supplier category {category_id}')
        rq = f'{self.host}/supplier/category/{category_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def listSupplierCategory(self, params={}):
        """
        Read all supplier categories.
        """
        logging.info('Getting all the categories')
        rq = f'{self.host}/supplier/category'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createSupplierCategory(self, payload):
        """
        Create new supplier category.
        """
        logging.info(f'Creating supplier category {payload}')
        rq = f'{self.host}/supplier/category'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateSupplierCategory(self, category_id: int, payload):
        """
        Update supplier category.
        """
        logging.info(f'Updating category {category_id} with {payload}')
        rq = f'{self.host}/supplier/category/{category_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # warehouse
    def listWarehouses(self, params={}):
        """
        Read all warehouses.
        """
        logging.info('Reading all warehouses')
        rq = f'{self.host}/warehouse'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getWarehouse(self, warehouse_id: int, params={}):
        """Get warehouse details."""
        logging.info(f'Get warehouse {warehouse_id} with params {params}')
        rq = f'{self.host}/warehouse/{warehouse_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createWarehouse(self, payload):
        """ 
        Create new warehouse
        """
        logging.info(f'Creating new warehouse {payload}')
        rq = f'{self.host}/warehouse'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateWarehouse(self, warehouse_id: int, payload):
        """ 
        Update warehouse.
        """
        logging.info(f'Updateing warehouse {warehouse_id} - {payload}')
        rq = f'{self.host}/warehouse/{warehouse_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getWarehouseFromName(self, name: str, params={}):
        """read warehouse from name."""
        logging.info(f'GEt warehouse from {name}')
        query = {
            'name': name
        }
        payload = {**params, **query}
        rq = f'{self.host}/warehouse/findByName'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)
