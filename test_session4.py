#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:25:34 2020

@author: Krish
"""

import session4
import os
import inspect
import re
from session4 import Qualean, PERMITTED_INPUT_SET
import random
import pytest
from decimal import Decimal
import math

README_CONTENT_CHECK_FOR = [
    '__init__'
]

MANDATORY_FUNCTIONS = [
    '__init__',
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]


CHECK_FOR_THINGS_NOT_ALLOWED = [
    'xyz123#$$'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_mandatory_fuctions_availability():
    MANDATORY_FUNCTIONs_availability = True
    f = open("session4.py", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            MANDATORY_FUNCTIONs_availability = False
            pass
    assert MANDATORY_FUNCTIONs_availability == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_valid_input():
    with pytest.raises(ValueError):
        Qualean(100)
    with pytest.raises(ValueError):
        Qualean("100")
    with pytest.raises(ValueError):
        Qualean(8+9j)
    try:
        Qualean(1)
        Qualean(1.0)
        Qualean(-1)
        Qualean(-1.0)
        Qualean(0)
        Qualean(0.0)
    except ValueError:
        pytest.fail("Value error raised for an valid input")


def test_add():
    a = Qualean(random.choice(PERMITTED_INPUT_SET))
    b = Qualean(random.choice(PERMITTED_INPUT_SET))
    sum = a+b
    i_sum = a.i_state + b.i_state
    assert i_sum == sum, "Addition does not satisfy for" + str(a) + ", " + str(b)

def test_sum_equals_product():
    for i in PERMITTED_INPUT_SET:
        q = Qualean(i)
        product = 100 * q
        sum = 0
        for i in range(100):
            sum += q
        print("sum " +  str(sum))
        print("product " + str(product))
        assert product == sum, "Sum is not equal to product for " + str(q)

def test_sqrt():
    q = Qualean(random.choice(PERMITTED_INPUT_SET))
    sqrt = q.__sqrt__()
    print ("sqrt " + str(sqrt))
    print(" isinstance(sqrt, complex) " + str(isinstance(sqrt, complex)))
    res = (isinstance(sqrt, complex) or (not bool(q)) or sqrt == Decimal(str(q)).sqrt())
    assert res, "Square root does not match"

def test_and_short_circuit():
    q1 = Qualean(random.choice(PERMITTED_INPUT_SET))
    q2 = None
    res = (bool(q1 and q2) == False)
    assert res, "AND Short circuit fail, condition 1"
    
    q1 = Qualean(0)
    q2 = Qualean(random.choice(PERMITTED_INPUT_SET))
    res = (bool(q1 and q2) == False)
    assert res, "AND Short circuit fail, condition 2"

def test_or_short_circuit():
    q1 = Qualean(random.choice(PERMITTED_INPUT_SET))
    q2 = None
    res = (bool(q1 or q2) == True)
    assert res, "OR Short circuit fail, condition 1 for" + str(q1)+ " and " + str(q2)
    
    q1 = Qualean(1)
    q2 = Qualean(random.choice(PERMITTED_INPUT_SET))
    res = (bool(q1 or q2) == True)
    assert res, "OR Short circuit fail, condition 2 for" + str(q1)+ " and " + str(q2)

def test_sum_million_equals_zero():
    sum = Qualean(0)
    for i in range(1000000):
        sum = sum + Qualean(random.choice(PERMITTED_INPUT_SET))
    print("sum " + str(sum))
    assert math.isclose(float(sum), 0, rel_tol = 1e+02), "Sum is not zero"