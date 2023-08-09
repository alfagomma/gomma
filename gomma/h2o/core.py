
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
H2o SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "3.1.5"
__date__ = "2022-03-10"

import logging

from gomma.session import Session


class H2o(object):
    """
    H2o core class .
    """

    def __init__(self, profile_name=None):
        """
        Initialize main class.
        """
        logging.info('Init H2o SDK')
        s = Session(profile_name)
        self.host = s.config.get('agapi_host')
        self.s = s

    # customer
    def getCustomers(self, params: dict = {}):
        """
        Read all customers.
        """
        logging.debug('Getting all customers')
        rq = f'{self.host}/customer'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createCustomer(self, payload: dict):
        """
        Create new customer.
        """
        logging.debug(f'Init creating customer {payload}...')
        rq = f'{self.host}/customer'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCustomer(self, customer_id: int, params: dict = {}):
        """
        Get customer by id.
        """
        logging.debug(f'Reading customer {customer_id}...')
        rq = f'{self.host}/customer/{customer_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCustomerFromTax(self, code: str):
        """
        Read customer from tax code.
        """
        logging.debug(f'Reading customer from tax code {code}')
        rq = f'{self.host}/customer/findByTax'
        query = {
            'code': code
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def get_customer_by_code(self, code: str):
        """
        Read customer by tax or business code.
        """
        logging.debug(f'Reading customer by code {code}')
        rq = f'{self.host}/customer/findByCode'
        query = {
            'code': code
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def updateCustomer(self, customer_id: int, payload: dict):
        """
        Update customer data.
        """
        logging.debug(f'Updating customer {customer_id}...')
        rq = f'{self.host}/customer/{customer_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def patch_customer(self, customer_id: int, payload: dict):
        """
        Patch customer.
        """
        logging.debug(f'Patching customer {customer_id}...')
        rq = f'{self.host}/customer/{customer_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # erp
    def getCustomerFromErp(self, customer_id: int, erp_id: int, params: dict = {}):
        """
        Read customer from erp external ID
        """
        logging.debug(f'Reading customer {customer_id} for erp {erp_id}')
        rq = f'{self.host}/customer/findByErp'
        query = {**params, **{
            'erp_id': erp_id,
            'ext_id': customer_id
        }}
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def createCustomerErp(self, customer_id: int, payload: dict):
        """
        Update customer ERP Xrefs. | DEPRECATED
        """
        logging.debug(f'Init creating customer {customer_id} ERP xref ...')
        rq = f'{self.host}/customer/{customer_id}/erp'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def attach_customer_erp(self, customer_id: int, erp_id: int, ext_id: str):
        """
        Add new customer erp xref.
        """
        logging.debug(
            f'Add customer {customer_id} ERP {erp_id} xref {ext_id} ...')
        rq = f'{self.host}/customer/{customer_id}/erp'
        payload = {'erp_id': erp_id, 'ext_id': f'{ext_id}'}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def detach_customer_erp(self, customer_id: int, erp_id: int):
        """
        Remove customer erp xref.
        """
        logging.debug(f'Remove customer {customer_id} ERP {erp_id} ...')
        rq = f'{self.host}/customer/{customer_id}/erp/{erp_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # account
    def getAccounts(self, params: dict = {}):
        """
        Read all accounts.
        """
        logging.debug('Getting all accounts')
        rq = f'{self.host}/account'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getAccount(self, account_id: int, params: dict = {}):
        """
        Get account by id.
        """
        logging.debug(f'Reading account {account_id}...')
        rq = f'{self.host}/account/{account_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createAccount(self, payload: dict):
        """
        Create new account.
        """
        logging.debug(f'Init creating account {payload}...')
        rq = f'{self.host}/account'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getAccountByEmail(self, email: str, params: dict = {}):
        """Get account details."""
        logging.info(
            f'Get account by email {email} with params {params}')
        query = {**params, **{'email': email}}
        rq = f'{self.host}/account/findByEmail'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)
        
    def create_customer_account(self, customer_id: int, payload: dict):
        """
        Add new customer account.
        """
        logging.debug(f'Add customer {customer_id} account {payload} ...')
        rq = f'{self.host}/customer/{customer_id}/account/create'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)
    
    def attach_customer_account(self, customer_id: int, account_id: int):
        """
        Attach existing account to customer.
        """
        logging.debug(f'Attach account {account_id} to customer {customer_id} ')
        rq = f'{self.host}/customer/{customer_id}/account'
        agent = self.s.getAgent()
        payload = {'account_id': account_id}
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def delete_customer_account(self, customer_id: int, account_id: int):
        """
        Remove customer account.
        """
        logging.debug(
            f'Remove customer {customer_id} account {account_id} ...')
        rq = f'{self.host}/customer/{customer_id}/account/{account_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # customer markets
    def attachCustomerMarket(self, customer_id: int, market_id: int):
        """
        Create new customer market
        """
        logging.debug(
            f'Attach market {market_id} to the customer {customer_id}')
        payload = {
            'market_id': market_id
        }
        rq = f'{self.host}/customer/{customer_id}/market'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # customer address
    def createCustomerAddress(self, customer_id: int, payload: dict):
        """
        Create new customer address
        """
        logging.debug(f'Creating customer {customer_id} address')
        rq = f'{self.host}/customer/{customer_id}/address'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateCustomerAddress(self, customer_id: int, address_id: int, payload: dict):
        """
        Update customer address.
        """
        logging.debug(f'Init updating {customer_id} address {address_id} ...')
        rq = f'{self.host}/customer/{customer_id}/address/{address_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def patchCustomerAddress(self, customer_id: int, address_id: int, payload: dict):
        """
        Patch customer address data.
        """
        logging.info(
            f'Patching customer {customer_id} address {address_id} with {payload}')
        rq = f'{self.host}/customer/{customer_id}/address/{address_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    def getCustomerAddresses(self, customer_id: int, params: dict = {}):
        """
        List customer addresses.
        """
        logging.debug(f'Getting all customer {customer_id} addresses')
        rq = '{self.host}/customer/{customer_id}/address'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCustomerAddress(self, customer_id: int, address_id: int, params: dict = {}):
        """
        Get customer address.
        """
        logging.debug(f'Get customer {customer_id} address {address_id}')
        rq = f'{self.host}/customer/{customer_id}/address/{address_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCustomerAddressFromExtId(self, customer_id: int, ext_id: str, params: dict = {}):
        """
        List customer addresses.
        """
        logging.debug(
            f'Search customer {customer_id} address ext_id {ext_id}.')
        query = {**params, **{
            'ext_id': ext_id
        }}
        rq = f'{self.host}/customer/{customer_id}/address/findByExtId'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    # customer sales agent
    def customer_add_agent(self, customer_id: int, payload: dict):
        """Add sales agent user details."""
        logging.debug(
            f'Add agent to customer {customer_id} with {payload}')
        rq = f'{self.host}/customer/{customer_id}/agent'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def customer_remove_agent(self, customer_id: int, agent_id: int):
        """Remove customer sales agent."""
        logging.debug(
            f'Remove agent {agent_id} to customer {customer_id}')
        rq = f'{self.host}/customer/{customer_id}/agent/{agent_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    # competitor

    def createCompetitor(self, payload: dict):
        """
        Create new competitor.
        """
        logging.debug('Init creating competitor...')
        rq = f'{self.host}/competitor'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCompetitor(self, competitor_id: int, params: dict = {}):
        """
        Get competitor by id.
        """
        logging.debug(f'Reading competitor {competitor_id}...')
        rq = f'{self.host}/competitor/{competitor_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    # invoice
    def getInvoiceTypes(self, params: dict = {}):
        """
        Read all invoice types.
        """
        logging.debug('Getting invoice types.')
        rq = f'{self.host}/invoice/type'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getInvoiceTypeFromName(self, name: str):
        """
        Get invoice type by name.
        """
        logging.debug('Getting invoice types.')
        rq = f'{self.host}/invoice/type/findByName'
        payload = {
            'name': name
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    def createInvoiceType(self, payload: dict):
        """
        Create new invoice type.
        """
        logging.debug('Creating new invoice type.')
        rq = f'{self.host}/invoice/type'
        agent = self.s.getAgent()
        r = agent.get(rq, json=payload)
        return self.s.response(r)


    # salesgroup

    def createSalesgroup(self, payload: dict):
        """
        Create new salesgroup.
        """
        logging.debug('Init creating salesgroup...')
        rq = f'{self.host}/salesgroup'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getSalesgroups(self, params: dict = {}):
        """
        Read all salesgroup.
        """
        logging.debug('Getting all salesgroup')
        rq = f'{self.host}/salesgroup'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getSalesgroup(self, salesgroup_id: int, params: dict = {}):
        """
        Get salesgroup by id.
        """
        logging.debug(f'Reading salesgroup {salesgroup_id}...')
        rq = f'{self.host}/salesgroup/{salesgroup_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def attach_salesgroup_customer(self, salesgroup_id: int, customer_id: int):
        """
        Add new salesgroup customer.
        """
        logging.debug(
            f'Add salesgroup {salesgroup_id} customer {customer_id} ...')
        rq = f'{self.host}/salesgroup/{salesgroup_id}/customer'
        payload = {'customer_id': customer_id}
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def detach_salesgroup_customer(self, salesgroup_id: int, customer_id: int):
        """
        Remove salesgroup customer.
        """
        logging.debug(f'Remove salesgroup {salesgroup_id} customer {customer_id} ...')
        rq = f'{self.host}/salesgroup/{salesgroup_id}/customer/{customer_id}'
        agent = self.s.getAgent()
        r = agent.delete(rq)
        return self.s.response(r)

    def getCustomerSalesgroup(self, customer_id: int, params: dict = {}):
        """
        Get customer salesgroups.
        """
        logging.debug(f'Reading customer {customer_id}...')
        rq = f'{self.host}/customer/{customer_id}/salesgroup'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)