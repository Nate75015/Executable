#!/usr/bin/env python
# coding: utf-8

# In[ ]:




"""Fichier d'installation de notre script salut.py."""
from cx_Freeze import setup, Executable
import pandas
import numpy
import os
import sys


# In[ ]:


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


# In[ ]:


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "MARQUE",
        version = "0.1",
        options = {'build_exe': {"packages": ["os","pandas","numpy"]}},
        description = "My GUI application!",
        executables = [Executable("2016_Extraction_Name.py")])
