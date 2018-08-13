#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 20:02:37 2017

@author: kurner
"""

import datetime

def from_year(y):
    """Please note the following: This is an integer calculation. 
    All variables are integers and all remainders from division 
    are dropped. For example, 7 divided by 3 is equal to 2 in 
    integer arithmetic.
    """
    c = y // 100
    n = y - 19 * ( y // 19 )
    k = ( c - 17 ) // 25
    i = c - c // 4 - ( c - k ) // 3 + 19 * n + 15
    i = i - 30 * ( i // 30 )
    i = i - ( i // 28 ) * ( 1 - ( i // 28 ) * ( 29 // ( i + 1 ) ) * ( ( 21 - n ) // 11 ) )
    j = y + y // 4 + i + 2 - c + c // 4
    j = j - 7 * ( j // 7 )
    l = i - j
    m = 3 + ( l + 40 ) // 44
    d = l + 28 - 31 * ( m // 4 )
    return datetime.datetime(y, m, d)

for yr in [2000 + x for x in range(21)]:
    easter = from_year(yr)
    print(easter.strftime("%a %m-%d-%Y"))