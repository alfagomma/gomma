
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
H2o SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.1.4"
__date__ = "2021-05-31"

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
    def getCustomers(self, query=None):
        """
        Read all customers.
        """
        logging.debug('Getting all customers')
        rq = '%s/customer' % (self.host)
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def createCustomer(self, payload):
        """
        Create new customer.
        """
        logging.debug('Init creating customer...')
        print(payload)
        rq = f'{self.host}/customer'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCustomer(self, customer_id: int):
        """
        Get customer by id.
        """
        logging.debug(f'Reading customer {customer_id}...')
        rq = f'{self.host}/customer/{customer_id}'
        agent = self.s.getAgent()
        r = agent.get(rq)
        return self.s.response(r)

    def getCustomerFromErp(self, customer_id, erp_id):
        """
        Read customer from erp external ID
        """
        logging.debug(f'Reading customer {customer_id} for erp {erp_id}')
        rq = f'{self.host}/customer/findByErp'
        payload = {
            'erp_id': erp_id,
            'ext_id': customer_id
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    def getCustomerFromTax(self, code):
        """
        Read customer from tax code.
        """
        logging.debug(f'Reading customer from tax code {code}')
        rq = f'{self.host}/customer/findByTax'
        payload = {
            'code': code
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    def updateCustomer(self, customer_id: int, payload):
        """
        Update customer data.
        """
        logging.debug(f'Updating customer {customer_id}...')
        rq = f'{self.host}/customer/{customer_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def createCustomerXerp(self, customer_id: int, payload):
        """
        Update customer ERP Xrefs.
        """
        logging.debug(f'Init creating customer {customer_id} ERP xref ...')
        rq = f'{self.host}/customer/{customer_id}/xerp'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # customer markets
    def attachCustomerMarket(self, customer_id: int, payload):
        """
        Create new customer market
        """
        logging.debug(f'Creating customer {customer_id} market')
        rq = f'{self.host}/customer/{customer_id}/market'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def syncCustomerMarket(self, customer_id: int, payload):
        """
        Syncronize customer markets
        """
        logging.debug(f'Syncing customer {customer_id} markets')
        rq = f'{self.host}/customer/{customer_id}/market/sync'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)        

    # customer address
    def createCustomerAddress(self, customer_id: int, payload):
        """
        Create new customer address
        """
        logging.debug(f'Creating customer {customer_id} address')
        rq = f'{self.host}/customer/{customer_id}/address'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateCustomerAddress(self, customer_id: int, address_id: int, payload):
        """
        Update customer address.
        """
        logging.debug(f'Init updating {customer_id} address {address_id} ...')
        rq = f'{self.host}/customer/{customer_id}/address/{address_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCustomerAddresses(self, customer_id: int, query=None):
        """
        List customer addresses.
        """
        logging.debug(f'Getting all customer {customer_id} addresses')
        rq = '{self.host}/customer/{customer_id}/address'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getCustomerAddress(self, customer_id: int, address_id: int, params=None):
        """
        Get customer address.
        """
        logging.debug(f'Get customer {customer_id} address {address_id}')
        rq = f'{self.host}/customer/{customer_id}/address/{address_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getCustomerAddressFromExtId(self, customer_id: int, ext_id: str, query=None):
        """
        List customer addresses.
        """
        logging.debug(
            f'Search customer {customer_id} address ext_id {ext_id}.')
        payload = {
            'ext_id': ext_id
        }
        if query:
            new_payload = dict(item.split("=") for item in query.split('&'))
            payload = {**payload, **new_payload}
        rq = f'{self.host}/customer/{customer_id}/address/findByExtId'
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    # competitor
    def createCompetitor(self, payload):
        """
        Create new competitor.
        """
        logging.debug('Init creating competitor...')
        rq = f'{self.host}/competitor'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getCompetitor(self, competitor_id: int):
        """
        Get competitor by id.
        """
        logging.debug(f'Reading competitor {competitor_id}...')
        rq = f'{self.host}/competitor/{competitor_id}'
        agent = self.s.getAgent()
        r = agent.get(rq)
        return self.s.response(r)

    # invoice
    def createInvoice(self, payload):
        """
        Create new invoice.
        """
        logging.debug(f'Creating invoice {payload}')
        rq = f'{self.host}/invoice'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getinvoices(self, query=None):
        """
        Read all invoices.
        """
        logging.debug('Getting invoices.')
        rq = f'{self.host}/invoice'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getInvoice(self, invoice_id: int):
        """
        Get invoice by id
        """
        logging.debug(f'Reading invoice {invoice_id}..')
        rq = f'{self.host}/invoice/{invoice_id}'
        agent = self.s.getAgent()
        r = agent.get(rq)
        return self.s.response(r)

    def getInvoiceFromErp(self, erp_id: int, ext_id):
        """
        Read invoice from erp external ID.
        """
        logging.debug(f'Reading invoice {ext_id} for erp {erp_id}')
        rq = f'{self.host}/invoice/findByErp'
        payload = {
            'erp_id': erp_id,
            'ext_id': ext_id
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    # invoice type
    def getInvoiceTypes(self, query=None):
        """
        Read all invoice types.
        """
        logging.debug('Getting invoice types.')
        rq = f'{self.host}/invoice/type'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
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

    def createInvoiceType(self, payload):
        """
        Create new invoice type.
        """
        logging.debug('Creating new invoice type.')
        rq = f'{self.host}/invoice/type'
        agent = self.s.getAgent()
        r = agent.get(rq, json=payload)
        return self.s.response(r)
