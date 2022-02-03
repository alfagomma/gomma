
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Hook SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.1.1"
__date__ = "2019-06-11"

import json
import logging
import time

from gomma.session import Session

logger = logging.getLogger(__name__)


class Hook(object):
    """
    Hook core class .
    """

    def __init__(self, profile_name=None):
        """
        Initialize main class with this and that.
        """
        logging.info('Init Hook SDK')
        s = Session(profile_name)
        host = s.config.get('hook_host')
        self.host = f'{host}'
        self.s = s

    # ERP
    def erp_sap_material(self, payload: dict):
        """
        Call erp sap worker queue
        """
        logging.debug(f'Calling erp sap queue')
        rq = f'{self.host}/erp/sap/material'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # ERP SAP CUSTOMER
    def erp_sap_customer(self, payload: dict):
        """
        Call erp sap customer worker queue
        """
        logging.debug(f'Calling erp sap customer queue')
        rq = f'{self.host}/erp/sap/customer'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # ERP SAP SUPPLIER
    def erp_sap_supplier(self, payload: dict):
        """
        Call erp sap supplier worker queue
        """
        logging.debug(f'Calling erp sap supplier queue')
        rq = f'{self.host}/erp/sap/supplier'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)
