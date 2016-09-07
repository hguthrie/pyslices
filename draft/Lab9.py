__author__ = 'hguthrie'
#  -*- coding: utf-8 -*-


class Payroll:
    def __init__(self, **pay):
        self.variables = pay
    def set_vars(self, key, val):
        self.variables[key] = val
    def get_vars(self, key):
        return self.variables.get(key, None)

    def pay(self):

    def hours(self):



class Employee(Payroll):
    def name(self):

    def overtime(self):