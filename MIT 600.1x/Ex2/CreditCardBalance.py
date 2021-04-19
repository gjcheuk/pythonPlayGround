# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:43:13 2021

@author: user
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

def balance_remain_after_one_year(b, a, m, n):
    '''
    

    Parameters
    ----------
    b : Int or Float
        Outstanding balance on the credit card at the beginning.
    a : Float
        Annual interest rate.
    m : Float
        Minimum monthly payment rate.
    n : Int
        Number of months for the purpose of calculation

    Returns
    -------
    The remaining balance that is outstanding on the credit card at the end of
    a n months period.

    '''
    a_monthly = a/12
    
    ub = b - m * b
    b = ub + a_monthly * ub

    if n == 1:
        return b
    else:
        return balance_remain_after_one_year(b, a, m, n - 1)

result = round(balance_remain_after_one_year(balance, annualInterestRate, monthlyPaymentRate, 12),2)

print("Remaining blanace: " + str(result))