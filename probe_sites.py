## Do a PING/CURL Test to denoted commercial hosts or urls
# test_cdn_client.py
# Chen Wang, Oct. 23, 2015
# chenw@cmu.edu

import hosts
import time
from monitor.ping import *

probe_num = 2




for host in hosts.commercial_hosts:
    mnRTT = getMnRTT(host)

