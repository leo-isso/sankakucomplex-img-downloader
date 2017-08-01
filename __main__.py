
__author__ = "Leonardo Isso"
__version__ = "0.0.1"
__credits__ = ["Leonardo Isso"]

import os
import sys
import urllib
from fileSave import createFiles
from bypass import bypassOpen 

if __name__ == '__main__':
    # Check for internet connection
    print('Checking for internet connection...')
    try:
        bypassOpen('http://www.google.com/')
        print('Connected.')
    except Exception:
        print('NO CONNECTION, exiting')
        sys.exit(1)
    createFiles()
