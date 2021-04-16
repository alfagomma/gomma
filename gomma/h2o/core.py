
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
H2o SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.1.4"
__date__ = "2019-05-22"

import json
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
        host = s.config.get('agapi_host')
        self.host = f'{host}/h2o'
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

    # order
    def createOrder(self, payload):
        """
        Create new order.
        """
        logging.debug('Creating order %s' % payload)
        rq = f'{self.host}/order'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def getOrders(self, query=None):
        """
        Read all orders.
        """
        logging.debug('Getting orders.')
        rq = f'{self.host}/order'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getOrder(self, order_id: int):
        """
        Get order by id
        """
        logging.debug(f'Reading order {order_id}..')
        rq = f'{self.host}/order/{order_id}'
        agent = self.s.getAgent()
        r = agent.get(rq)
        return self.s.response(r)

    def getOrderFromErp(self, erp_id: int, ext_id):
        """
        Read order from erp external ID.
        """
        logging.debug(f'Reading order {ext_id} for erp {erp_id}')
        rq = f'{self.host}/order/findByErp'
        payload = {
            'erp_id': erp_id,
            'ext_id': ext_id
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    def createOrderDetail(self, order_id: int, payload):
        """
        Create order detail.
        """
        logging.debug('Creating order detail')
        rq = f'{self.host}/order/{order_id}/detail'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # order type
    def getOrderTypes(self, query=None):
        """
        Read all order types.
        """
        logging.debug('Getting order types.')
        rq = f'{self.host}/order/type'
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)

    def getOrderTypeFromName(self, name: str):
        """
        Get order type by name.
        """
        logging.debug('Getting order types.')
        rq = f'{self.host}/order/type/findByName'
        payload = {
            'name': name
        }
        agent = self.s.getAgent()
        r = agent.get(rq, params=payload)
        return self.s.response(r)

    def createOrderType(self, payload):
        """
        Create new order type.
        """
        logging.debug('Creating new order type.')
        rq = f'{self.host}/order/type'
        agent = self.s.getAgent()
        r = agent.get(rq, json=payload)
        return self.s.response(r)
