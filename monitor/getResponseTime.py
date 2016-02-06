'''
Curl a URL to get the response time for downloading the page
'''
from subprocess import Popen, PIPE
import re
import sys
import os

## Call system command to ping a
def curl(url):
    '''
    Pings a host and return True if it is available, False if not.
    '''
    cmd = ['ping', '-c', str(count), ip]
    return
