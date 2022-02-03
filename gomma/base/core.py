
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
BASE SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "3.1.1"
__date__ = "2022-02-02"

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
    def getErp(self, erp_id: int, params: dict = {}):
        """
        Get ERP data.
        """
        logging.debug(f'Get erp {erp_id}')
        rq = f'{self.host}/erp/{erp_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # unit of measure
    def getUoms(self, params: dict = {}):
        """Get all uoms."""
        logging.debug('Getting all unit of measure...')
        rq = f'{self.host}/settings/unitofmeasure'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getUom(self, uom_id: int, params: dict = {}):
        """
        Leggo uom da id.
        """
        logging.debug(f'Reading family {uom_id}...')
        rq = f'{self.host}/settings/unitofmeasure/{uom_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getUomFromCode(self, code: str, params: dict = {}):
        """
        Leggo uom da code.
        """
        logging.debug(f'Reading uom code {code}...')
        query = {**params, **{'code': code}}
        rq = f'{self.host}/settings/unitofmeasure/findByCode'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    # Currency
    def getCurrencies(self, params: dict = {}):
        """Get all currencies."""
        logging.debug('Getting all unit of measure...')
        rq = f'{self.host}/settings/currency'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCurrency(self, currency_id: int, params: dict = {}):
        """
        Leggo uom da id.
        """
        logging.debug(f'Reading currency {currency_id}...')
        rq = f'{self.host}/settings/currency/{currency_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCurrencyFromCode(self, code: str, params: dict = {}):
        """
        Get currency from code.
        """
        logging.debug(f'Reading currency code {code}...')
        params = {**params, **{'code': code}}
        rq = f'{self.host}/settings/currency/findByCode'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # company

    def getCompany(self, company_id: int, params: dict = {}):
        """
        Legge un company dal suo id.
        """
        logging.info(f'Get company {company_id}')
        rq = f'{self.host}/company/{company_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCompanies(self, params: dict = {}):
        """
        Prende tutti gli companies.
        """
        logging.info('Getting all the companies')
        rq = f'{self.host}/company'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createCompany(self, payload: dict):
        """
        Create new company.
        """
        logging.info(f'Creating company {payload}')
        rq = f'{self.host}/company'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCompanyFromCode(self, code: str, params: dict = {}):
        """
        Get company from code.
        """
        logging.info(f'Search company code {code}.')
        query = {**params, **{'code': code}}
        rq = f'{self.host}/company/findByCode'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def updateCompany(self, company_id: int, payload: dict):
        """
        Update company.
        """
        logging.info(f'Updating company {company_id} with {payload}')
        rq = f'{self.host}/company/{company_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # supplier

    def getSupplier(self, supplier_id: int, params: dict = {}):
        """
        Read single supplier.
        """
        logging.info(f'Get supplier {supplier_id}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def listSupplier(self, params: dict = {}):
        """
        Read all suppliers.
        """
        logging.info('Getting all the suppliers')
        rq = f'{self.host}/supplier'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createSupplier(self, payload: dict):
        """
        Create new supplier.
        """
        logging.info(f'Creating supplier {payload}')
        rq = f'{self.host}/supplier'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getSupplierFromErp(self, erp_id: int, code: str, params: dict = {}):
        """
        Get supplier from erp.
        """
        logging.info(f'Search supplier from erp {erp_id} code {code}.')
        query = {**params, **{'erp': erp_id, 'code': code}}
        rq = f'{self.host}/supplier/findByErp'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def updateSupplier(self, supplier_id: int, payload: dict):
        """
        Update supplier.
        """
        logging.info(f'Updating supplier {supplier_id} with {payload}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def patchSupplier(self, supplier_id: int, payload: dict):
        """
        Patch supplier data.
        """
        logging.info(f'Patching supplier {supplier_id} with {payload}')
        rq = f'{self.host}/supplier/{supplier_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # supplier company
    def listSupplierCompanies(self, supplier_id: int, params: dict = {}):
        """
        Read supplier companies.
        """
        logging.info(f'Reading supplier {supplier_id} companies')
        rq = f'{self.host}/supplier/{supplier_id}/company'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
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
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def supplierDetachCompany(self, supplier_id: int, company_id: int):
        """
        Detach company to supplier.
        """
        logging.info(
            f'Detaching company {company_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/company/{company_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    def listSupplierErps(self, supplier_id: int, params: dict = {}):
        """
        Read supplier erps.
        """
        logging.info(f'Reading supplier {supplier_id} erps')
        rq = f'{self.host}/supplier/{supplier_id}/erp'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
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
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def supplierDetachErp(self, supplier_id: int, erp_id: int):
        """
        Detach erp to supplier.
        """
        logging.info(f'Detaching erp {erp_id} to supplier {supplier_id}.')
        rq = f'{self.host}/supplier/{supplier_id}/erp/{erp_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # category

    def getSupplierCategory(self, category_id: int, params: dict = {}):
        """
        Read single category.
        """
        logging.info(f'Get supplier category {category_id}')
        rq = f'{self.host}/supplier/category/{category_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def listSupplierCategory(self, params: dict = {}):
        """
        Read all supplier categories.
        """
        logging.info('Getting all the categories')
        rq = f'{self.host}/supplier/category'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createSupplierCategory(self, payload: dict):
        """
        Create new supplier category.
        """
        logging.info(f'Creating supplier category {payload}')
        rq = f'{self.host}/supplier/category'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateSupplierCategory(self, category_id: int, payload: dict):
        """
        Update supplier category.
        """
        logging.info(f'Updating category {category_id} with {payload}')
        rq = f'{self.host}/supplier/category/{category_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # warehouse
    def listWarehouses(self, params: dict = {}):
        """
        Read all warehouses.
        """
        logging.info('Reading all warehouses')
        rq = f'{self.host}/warehouse'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getWarehouse(self, warehouse_id: int, params: dict = {}):
        """Get warehouse details."""
        logging.info(f'Get warehouse {warehouse_id} with params {params}')
        rq = f'{self.host}/warehouse/{warehouse_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createWarehouse(self, payload: dict):
        """ 
        Create new warehouse
        """
        logging.info(f'Creating new warehouse {payload}')
        rq = f'{self.host}/warehouse'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateWarehouse(self, warehouse_id: int, payload: dict):
        """ 
        Update warehouse.
        """
        logging.info(f'Updateing warehouse {warehouse_id} - {payload}')
        rq = f'{self.host}/warehouse/{warehouse_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getWarehouseFromName(self, name: str, params: dict = {}):
        """read warehouse from name."""
        logging.info(f'GEt warehouse from {name}')
        query = {**params, **{'name': name}}
        rq = f'{self.host}/warehouse/findByName'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def patchWarehouse(self, whs_id: int, payload: dict):
        """
        Patch warehouse.
        """
        logging.debug(f'Patching warehouse {whs_id} with {payload}')
        rq = f'{self.host}/warehouse/{whs_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # network
    def listNetworks(self, params: dict = {}):
        """
        Read all networks.
        """
        logging.info('Reading all networks')
        rq = f'{self.host}/network'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getNetwork(self, network_id: int, params: dict = {}):
        """Get network details."""
        logging.info(f'Get network {network_id} with params {params}')
        rq = f'{self.host}/network/{network_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createNetwork(self, payload: dict):
        """ 
        Create new network
        """
        logging.info(f'Creating new network {payload}')
        rq = f'{self.host}/network'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateNetwork(self, network_id: int, payload: dict):
        """ 
        Update network.
        """
        logging.info(f'Updateing network {network_id} - {payload}')
        rq = f'{self.host}/network/{network_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getNetworkFromName(self, name: str, params: dict = {}):
        """read network from name."""
        logging.info(f'GEt network from {name}')
        query = {**params, **{'name': name}}
        rq = f'{self.host}/network/findByName'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def patchNetwork(self, network_id: int, payload: dict):
        """
        Patch network.
        """
        logging.debug(f'Patching network {network_id} with {payload}')
        rq = f'{self.host}/network/{network_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # glaccount
    def listGlaccounts(self, params: dict = {}):
        """
        Read all glaccounts.
        """
        logging.info('Reading all glaccounts')
        rq = f'{self.host}/glaccount'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getGlaccount(self, glaccount_id: int, params: dict = {}):
        """Get glaccount details."""
        logging.info(f'Get glaccount {glaccount_id} with params {params}')
        rq = f'{self.host}/glaccount/{glaccount_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createGlaccount(self, payload: dict):
        """ 
        Create new glaccount
        """
        logging.info(f'Creating new glaccount {payload}')
        rq = f'{self.host}/glaccount'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateGlaccount(self, glaccount_id: int, payload: dict):
        """ 
        Update glaccount.
        """
        logging.info(f'Updateing glaccount {glaccount_id} - {payload}')
        rq = f'{self.host}/glaccount/{glaccount_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getGlaccountFromName(self, name: str, params: dict = {}):
        """read glaccount from name."""
        logging.info(f'Get glaccount from {name}')
        query = {**params, **{'name': name}}
        rq = f'{self.host}/glaccount/findByName'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def attachGlaccountCategory(self, glaccount_id: int, category_id: int):
        """
        Add category to glaccount
        """
        logging.debug(
            f'Attaching category {category_id} at glaccount {glaccount_id} ...')
        rq = f"{self.host}/glaccount/{glaccount_id}/category"
        payload = {
            'category_id': category_id
        }
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def syncGlaccountCategory(self, glaccount_id: int, categories: list = []):
        """
        Sync glaccount categories.
        """
        logging.debug(
            f'Syncing glaccount {glaccount_id} categories {categories} ...')
        rq = f"{self.host}/glaccount/{glaccount_id}/category/sync"
        payload = {'categoryid[]': cat for cat in categories}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def detachGlaccountCategory(self, glaccount_id: int, category_id: int):
        """
        Remove category from glaccount
        """
        logging.debug(
            f'Removing category {category_id} from glaccount {glaccount_id} ...')
        rq = f"{self.host}/glaccount/{glaccount_id}/category/{category_id}"
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # glaccount category
    def listGlcategory(self, params: dict = {}):
        """
        Read all glaccount category.
        """
        logging.info('Reading all glaccount categories')
        rq = f'{self.host}/glaccount/category'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getGlcategory(self, category_id: int, params: dict = {}):
        """Get glaccount details."""
        logging.info(
            f'Get glaccount category {category_id} with params {params}')
        rq = f'{self.host}/glaccount/category/{category_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createGlcategory(self, payload: dict):
        """ 
        Create new glaccount category
        """
        logging.info(f'Creating new glaccount category {payload}')
        rq = f'{self.host}/glaccount/category'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateGlcategory(self, category_id: int, payload: dict):
        """ 
        Update glaccount.
        """
        logging.info(f'Updateing glaccount {category_id} - {payload}')
        rq = f'{self.host}/glaccount/category/{category_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getGlcategoryFromName(self, name: str, params: dict = {}):
        """read glaccount from name."""
        logging.info(f'Get glaccount category from {name}')
        query = {**params, **{'name': name}}
        rq = f'{self.host}/glaccount/category/findByName'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    # glaccount kpi
    def listGlKpi(self, params: dict = {}):
        """
        Read all glaccount kpi.
        """
        logging.info('Reading all glaccount kpis')
        rq = f'{self.host}/glaccount/kpi'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getGlKpi(self, kpi_id: int, params: dict = {}):
        """Get glaccount details."""
        logging.info(
            f'Get glaccount kpi {kpi_id} with params {params}')
        rq = f'{self.host}/glaccount/kpi/{kpi_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createGlKpi(self, payload: dict):
        """ 
        Create new glaccount kpi
        """
        logging.info(f'Creating new glaccount kpi {payload}')
        rq = f'{self.host}/glaccount/kpi'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateGlKpi(self, kpi_id: int, payload: dict):
        """ 
        Update glaccount.
        """
        logging.info(f'Updateing glaccount {kpi_id} - {payload}')
        rq = f'{self.host}/glaccount/kpi/{kpi_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getGlKpiFromName(self, name: str, params: dict = {}):
        """read glaccount from name."""
        logging.info(f'Get glaccount kpi from {name}')
        query = {**params, **{'name': name}}
        rq = f'{self.host}/glaccount/kpi/findByName'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    # user

    def listUser(self, params: dict = {}):
        """
        Read all user kpi.
        """
        logging.info('Reading all user')
        rq = f'{self.host}/user'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getUser(self, user_id: int, params: dict = {}):
        """Get user details."""
        logging.info(
            f'Get user {user_id} with params {params}')
        rq = f'{self.host}/user/{user_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # internalnewsletter

    def listIntnewsletter(self, params: dict = {}):
        """
        Read all intnewsletter kpi.
        """
        logging.info('Reading all intnewsletter')
        rq = f'{self.host}/intnewsletter'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getIntnewsletter(self, intnewsletter_id: int, params: dict = {}):
        """Get intnewsletter details."""
        logging.info(
            f'Get intnewsletter {intnewsletter_id} with params {params}')
        rq = f'{self.host}/intnewsletter/{intnewsletter_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def updateIntnewsletter(self, intnewsletter_id: int, payload: dict):
        """ 
        Update intnewsletter.
        """
        logging.info(f'Updateing intnewsletter {intnewsletter_id} - {payload}')
        rq = f'{self.host}/intnewsletter/{intnewsletter_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)
