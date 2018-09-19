# -*- coding: utf-8 -*-
"""
Spyder Editor

Already in same directory as:
Session_01-20180918T193558Z-001.zip

If not, make a path
"""

import zipfile
import os

filename = "Session_01-20180918T193558Z-001.zip"
print("Looking for:", filename)
print("You are in", os.getcwd())
filefound = os.path.exists(filename)
print("File found:", filefound)

if filefound:
    print("Contents of zipfile:")
    f = zipfile.ZipFile(filename)
    print(f.namelist())
    answer = input("Do you wish to extract? (Y/n) ")
    if answer == "Y":
        f.extractall()
    f.close()
else:
    print("No action taken")
