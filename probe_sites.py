## Do a PING/CURL Test to denoted commercial hosts or urls
# test_cdn_client.py
# Chen Wang, Oct. 23, 2015
# chenw@cmu.edu
import config

import hosts
import time
from datetime import datetime
from utils import *
from monitor.ping import *
from monitor.curl import *

probe_num = 1

rtt_data = {}
curl_data = {}

myName = getMyName()

startTS = time.time()
curTS = startTS
preTS = startTS
dateStr = datetime.fromtimestamp(curTS).strftime('%m%d')

rtt_data['Timestamp'] = curTS
curl_data['Timestamp'] = curTS
for host_name in hosts.commercial_hosts.keys():
    mnRTT = getMnRTT(hosts.commercial_hosts[host_name], probe_num)
    rtt_data[host_name] = mnRTT
    curTS = time.time()
    time_elapsed = curTS - preTS
    preTS = curTS
    print "Running Time for ping ", host_name, ' is ', str(time_elapsed)


for url_name in hosts.commercial_urls:
    rsp_time = curl(hosts.commercial_urls[url_name])
    curl_data[url_name] = rsp_time
    curTS = time.time()
    time_elapsed = curTS - preTS
    preTS = curTS
    print "Running Time for curl ", url_name, ' is ', str(time_elapsed)

rtt_file_name = config.probe_path + myName + '_' + dateStr + '_ping.csv'
rtt_headers = ['Timestamp'] + hosts.commercial_hosts.keys()
appendCSV(rtt_file_name, rtt_headers, rtt_data)


curl_file_name = config.probe_path + myName + '_' + dateStr +'_curl.csv'
curl_headers = ['Timestamp'] + hosts.commercial_urls.keys()
appendCSV(curl_file_name, curl_headers, curl_data)

time_elapsed = time.time() - startTS
print "Total running time is", str(time_elapsed)
