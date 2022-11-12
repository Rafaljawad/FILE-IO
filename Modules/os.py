# os
# The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules.

# This module provides a portable way of using operating system-dependent functionality.

# The os and os.path modules include many functions to interact with the file system



# importing os module 
import os 
# Get the current working 
# directory (CWD)

cworking = os.getcwd()

print(cworking)
#output -->c:\Users\rafal\Videos\python-training-with-kumar-lecturs\practice and notes\File-IO


print(os.chdir(r"c:\Users\rafal\Videos\python-training-with-kumar-lecturs\practice and notes\practice_virtual_env"))