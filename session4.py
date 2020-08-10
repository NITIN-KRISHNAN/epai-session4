#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:24:33 2020

@author: NITIN-KRISHNAN
"""
import math
import random
from decimal import Decimal, ROUND_HALF_EVEN, getcontext

PERMITTED_INPUT_SET = [1, 0 , -1]

class Qualean:

    def __init__(self, val):
        if not (isinstance(val, int) or isinstance(val, float) and val.is_integer()):
            raise ValueError("Invalid Input - should be an integer")
        elif val not in PERMITTED_INPUT_SET:
            raise ValueError("Invalid Input - should be one of permitted values ", PERMITTED_INPUT_SET)
        else:
            # TODO this might not be required
            getcontext().rounding = ROUND_HALF_EVEN
            self.i_state = int(val) * self.get_random_number()

    def __repr__(self):
        return  "Qualean state="+str(self.i_state)

    def __str__(self):
        return str(self.i_state)

    def __and__(self, other):
        print("__and__")
        return self.i_state and other.i_state

    def __or_(self, other):
        print("__or__")
        return self.i_state or other.i_state

    def __bool__(self):
        print("__bool__")
        return (self.i_state != 0)  

    def __nonzero__(self):
        print("__nonzero__")
        return (self.i_state == 0)

    def __eq__(self, other):
        return self.i_state == other

    def __float__(self):
        return float(self.i_state)

    def __Decimal__(self):
        return Decimal(self.i_state)

    def __ge__(self, other):
        return self.i_state >= other

    def __gt__(self, other):
        return self.i_state > other

    def __le__(self, other):
        return self.i_state <= other

    def __lt__(self, other):
        return self.i_state < other

    def __sqrt__(self):
        if(self.i_state < 0):
            return complex(0, (-1 * self.i_state).sqrt())
        elif(self.i_state < 0):
            return self.i_state.sqrt()
        else:
            return Decimal(0)

    def __invertsign__(self):
        self.i_state = -1 * self.i_state
        return self

    def __add__(self, other):
        return self.i_state + other

    def __radd__(self, other):
        return self.i_state + other

    def __mul__(self, other):
        return self.i_state * other

    def __rmul__(self, other):
        return self.i_state * other

    def get_random_number(self):
        return Decimal(str(random.uniform(-1, 1))).quantize(Decimal('1.0000000000'), rounding = ROUND_HALF_EVEN)

    def is_negative(self):
        return self.i_state < 0
