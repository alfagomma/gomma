
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GRAPH SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "2.1.1"
__date__ = "2019-11-07"

import json
import logging
import time

from gomma.session import Session


class Graph(object):
    """
    Graph Open Data core class .
    """

    def __init__(self, profile_name=None):
        """
        Initialize main class with this and that.
        """
        logging.debug('Init Graph SDK')
        s = Session(profile_name)
        host = s.config.get('aggraph_host')
        self.host = f'{host}/element'
        self.s = s

    def get_language(self, language_id: int, params=None):
        """
        Read single language
        """
        logging.debug(f'Get language {language_id}')
        rq = f'{self.host}/language/{language_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def read_all_language(self, query=None):
        """
        Read all public languages.
        """
        logging.debug('Getting all the languages')
        rq = '%s/language' % (self.host)
        agent = self.s.getAgent()
        r = agent.get(rq, params=query)
        return self.s.response(r)
