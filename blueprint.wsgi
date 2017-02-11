#!/usr/bin/python

"""Import."""
import sys
import os
sys.stdout = sys.stderr

# path
sys.path.insert(0,"/home/frederico/virtualenvs/blueprint/blueprint")
os.chdir("/home/frederico/virtualenvs/blueprint/blueprint")

# virtualenvs
activate_this = '/home/frederico/virtualenvs/blueprint/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# application
from run import app as application
