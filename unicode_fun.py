#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:36:12 2018

@author: Kirby Urner
"""

def emoji():
    for codepoint in range(int('1F600', 16), int('1F620', 16)):
        print(chr(codepoint), end="")
    
def hebrew():
    print([chr(codepoint) 
        for codepoint in range(int('05D0', 16), 
                               int('05DA', 16))]) 
    
def greek():
    for codepoint in range(int('03D0', 16), int('03FF', 16)):
        print(chr(codepoint), end="")
        
def korean():
    for codepoint in range(int('BB00', 16), int('BBAF', 16)):
        print(chr(codepoint), end="")
        
def arabic():
    print([chr(codepoint) 
        for codepoint in range(int('0681', 16), 
                               int('06AF', 16))])

def main():
    print("\nEMOJI")
    emoji()
    print("\n\nHEBREW")
    hebrew()
    print("\n\nGREEK & COPTIC")        
    greek()
    print("\n\nKOREAN")
    korean()
    print("\n\nARABIC")
    arabic()

