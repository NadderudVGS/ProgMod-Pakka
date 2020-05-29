"""
fjerner __pycache__ filer:
-------------------------------
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
-------------------------------
"""
from os import system
import areal
import deriverte
import integrerte
import plot
import nullpunkt

# fjerner irriterende filer
system('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')

