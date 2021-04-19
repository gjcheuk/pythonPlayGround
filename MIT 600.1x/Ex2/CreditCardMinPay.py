# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:43:13 2021

@author: user
"""
balance = 392600
annualInterestRate = 0.2

def minimum_pay(b, a):
    '''
    

    Parameters
    ----------
    b : Int or Float
        Outstanding balance on the credit card at the beginning.
    a : Float
        Annual interest rate.

    Returns
    -------
    The minimum payment that is needed to pay off the balance in 12 months

    '''
    
    a_monthly = a / 12
    m = 10
    
    while True:
        n = 0
        bal = b
        while m < a_monthly * b:
            m += 10
            
        while bal > 0:
            ub = bal - m
            bal = ub + a_monthly * ub
            n += 1

        if n <= 12:
            return m
        else:
            m += 10

result = minimum_pay(balance, annualInterestRate)

print("Minimum payment: " + str(result))