# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:43:13 2021

@author: user
"""
balance = 999999
annualInterestRate = 0.18

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
    lower = b / 12
    upper = (b * (1 + a_monthly) ** 12) / 12

    
    while True:
        n = 0
        bal = b
        m = (lower + upper)/2
        
        while bal > 0:
            ub = bal - m
            bal = ub + a_monthly * ub
            n += 1

        if n < 12:
            upper = m
        elif n > 12:
            lower = m
        elif abs(bal) < 0.01 and abs(bal) > -0.01:
            return m
        else:
            upper = m

result = round(minimum_pay(balance, annualInterestRate), 2)

print("Minimum payment: " + str(result))