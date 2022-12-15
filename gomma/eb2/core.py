
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
EB2 SDK
"""

__author__ = "Davide Pellegrino"
__version__ = "1.1.2"
__date__ = "2022-12-15"

import logging

from gomma.session import Session


class Eb2(object):
    """
    Eb2 core class .
    """

    def __init__(self, profile_name=None):
        """
        Init Eb2 cls.
        """
        logging.info(f'Init Eb2 SDK -p {profile_name}')
        s = Session(profile_name)
        self.host = s.config.get('agapi_host')
        logging.debug(f'host is {self.host}')
        self.s = s

    # employee
    def getEmployee(self, employee_id: int, params: dict = {}):
        """
        Read employee from id.
        """
        logging.debug(f'Get employee {employee_id}')
        rq = f'{self.host}/employee/{employee_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getEmployeeFromUser(self, user_id: int, params: dict = {}):
        """
        Find employee from user id.
        """
        logging.debug(f'Get employee from user#{user_id}')
        rq = f'{self.host}/employee/findByUser'
        params = {**params, **{'user': user_id}}
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getEmployees(self, params: dict = {}):
        """
        Prende tutti gli employees.
        """
        logging.debug('Getting all the employees')
        rq = f'{self.host}/employee'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createEmployee(self, payload: dict):
        """
        Create new employee.
        """
        logging.debug(f'Creating employee {payload}')
        rq = f'{self.host}/employee'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateEmployee(self, employee_id: int, payload: dict):
        """
        Update employee.
        """
        logging.debug(f'Updating employee {employee_id} with {payload}')
        rq = f'{self.host}/employee/{employee_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def patchEmployee(self, employee_id: int, payload: dict):
        """
        Patch know employee field.
        """
        logging.debug(f'Patching employee {employee_id} with {payload}')
        rq = f'{self.host}/employee/{employee_id}'
        agent = self.s.getAgent()
        r = agent.patch(rq, json=payload)
        return self.s.response(r)

    # department
    def getDepartment(self, department_id: int, params: dict = {}):
        """
        Read department from id.
        """
        logging.debug(f'Get department {department_id}')
        rq = f'{self.host}/department/{department_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getDepartments(self, params: dict = {}):
        """
        Prende tutti gli departments.
        """
        logging.debug('Getting all the departments')
        rq = f'{self.host}/department'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createDepartment(self, payload: dict):
        """
        Create new department.
        """
        logging.debug(f'Creating department {payload}')
        rq = f'{self.host}/department'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateDepartment(self, department_id: int, payload: dict):
        """
        Update department.
        """
        logging.debug(f'Updating department {department_id} with {payload}')
        rq = f'{self.host}/department/{department_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    # labortype
    def getLabortype(self, labortype_id: int, params: dict = {}):
        """
        Read labortype from id.
        """
        logging.debug(f'Get labortype {labortype_id}')
        rq = f'{self.host}/labortype/{labortype_id}'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def getLabortypes(self, params: dict = {}):
        """
        Prende tutti gli labortypes.
        """
        logging.debug('Getting all the labortypes')
        rq = f'{self.host}/labortype'
        agent = self.s.getAgent()
        r = agent.get(rq, params=params)
        return self.s.response(r)

    def createLabortype(self, payload: dict):
        """
        Create new labortype.
        """
        logging.debug(f'Creating labortype {payload}')
        rq = f'{self.host}/labortype'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)

    def updateLabortype(self, labortype_id: int, payload: dict):
        """
        Update labortype.
        """
        logging.debug(f'Updating labortype {labortype_id} with {payload}')
        rq = f'{self.host}/labortype/{labortype_id}'
        agent = self.s.getAgent()
        r = agent.post(rq, json=payload)
        return self.s.response(r)
