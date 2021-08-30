
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

    def patchWarehouse(self, whs_id: int, payload):
        """
        Patch warehouse.
        """
        logging.debug(f'Patching warehouse {whs_id} with {payload}')
        rq = f'{self.host}/warehouse/{whs_id}'
        try:
            agent = self.s.getAgent()
            r = agent.patch(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # network
    def listNetworks(self, params={}):
        """
        Read all networks.
        """
        logging.info('Reading all networks')
        rq = f'{self.host}/network'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getNetwork(self, network_id: int, params={}):
        """Get network details."""
        logging.info(f'Get network {network_id} with params {params}')
        rq = f'{self.host}/network/{network_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createNetwork(self, payload):
        """ 
        Create new network
        """
        logging.info(f'Creating new network {payload}')
        rq = f'{self.host}/network'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateNetwork(self, network_id: int, payload):
        """ 
        Update network.
        """
        logging.info(f'Updateing network {network_id} - {payload}')
        rq = f'{self.host}/network/{network_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getNetworkFromName(self, name: str, params={}):
        """read network from name."""
        logging.info(f'GEt network from {name}')
        query = {
            'name': name
        }
        payload = {**params, **query}
        rq = f'{self.host}/network/findByName'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def patchNetwork(self, network_id: int, payload):
        """
        Patch network.
        """
        logging.debug(f'Patching network {network_id} with {payload}')
        rq = f'{self.host}/network/{network_id}'
        try:
            agent = self.s.getAgent()
            r = agent.patch(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # glaccount
    def listGlaccounts(self, params={}):
        """
        Read all glaccounts.
        """
        logging.info('Reading all glaccounts')
        rq = f'{self.host}/glaccount'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getGlaccount(self, glaccount_id: int, params={}):
        """Get glaccount details."""
        logging.info(f'Get glaccount {glaccount_id} with params {params}')
        rq = f'{self.host}/glaccount/{glaccount_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createGlaccount(self, payload):
        """ 
        Create new glaccount
        """
        logging.info(f'Creating new glaccount {payload}')
        rq = f'{self.host}/glaccount'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateGlaccount(self, glaccount_id: int, payload):
        """ 
        Update glaccount.
        """
        logging.info(f'Updateing glaccount {glaccount_id} - {payload}')
        rq = f'{self.host}/glaccount/{glaccount_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getGlaccountFromName(self, name: str, params={}):
        """read glaccount from name."""
        logging.info(f'Get glaccount from {name}')
        query = {
            'name': name
        }
        payload = {**params, **query}
        rq = f'{self.host}/glaccount/findByName'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getGlaccountFromCode(self, code: str, params={}):
        """read glaccount from code."""
        logging.info(f'Get glaccount from {code}')
        query = {
            'code': code
        }
        payload = {**params, **query}
        rq = f'{self.host}/glaccount/findByCode'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # glaccount category
    def listGlaccountCategory(self, params={}):
        """
        Read all glaccount category.
        """
        logging.info('Reading all glaccount categories')
        rq = f'{self.host}/glaccount/category'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getGlaccountCategory(self, category_id: int, params={}):
        """Get glaccount details."""
        logging.info(
            f'Get glaccount category {category_id} with params {params}')
        rq = f'{self.host}/glaccount/category/{category_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createGlaccountCategory(self, payload):
        """ 
        Create new glaccount category
        """
        logging.info(f'Creating new glaccount category {payload}')
        rq = f'{self.host}/glaccount/category'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateGlaccountCategory(self, category_id: int, payload):
        """ 
        Update glaccount.
        """
        logging.info(f'Updateing glaccount {category_id} - {payload}')
        rq = f'{self.host}/glaccount/category/{category_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getGlaccountCategoryFromName(self, name: str, params={}):
        """read glaccount from name."""
        logging.info(f'Get glaccount category from {name}')
        query = {
            'name': name
        }
        payload = {**params, **query}
        rq = f'{self.host}/glaccount/category/findByName'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    # glaccount kpi
    def listGlaccountKpi(self, params={}):
        """
        Read all glaccount kpi.
        """
        logging.info('Reading all glaccount kpis')
        rq = f'{self.host}/glaccount/kpi'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getGlaccountKpi(self, kpi_id: int, params={}):
        """Get glaccount details."""
        logging.info(
            f'Get glaccount kpi {kpi_id} with params {params}')
        rq = f'{self.host}/glaccount/kpi/{kpi_id}'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=params)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def createGlaccountKpi(self, payload):
        """ 
        Create new glaccount kpi
        """
        logging.info(f'Creating new glaccount kpi {payload}')
        rq = f'{self.host}/glaccount/kpi'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def updateGlaccountKpi(self, kpi_id: int, payload):
        """ 
        Update glaccount.
        """
        logging.info(f'Updateing glaccount {kpi_id} - {payload}')
        rq = f'{self.host}/glaccount/kpi/{kpi_id}'
        try:
            agent = self.s.getAgent()
            r = agent.post(rq, json=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)

    def getGlaccountKpiFromName(self, name: str, params={}):
        """read glaccount from name."""
        logging.info(f'Get glaccount kpi from {name}')
        query = {
            'name': name
        }
        payload = {**params, **query}
        rq = f'{self.host}/glaccount/kpi/findByName'
        try:
            agent = self.s.getAgent()
            r = agent.get(rq, params=payload)
        except Exception:
            logging.error(f'Failed request {rq}')
            return False
        return self.s.response(r)
