import os

commercial_hosts = [
    'netflix753.as.nflximg.com.edgesuite.net',
    'www.cbssports.com',
    '209715148.log.optimizely.com',
    's.amazon-adsystem.com',
    'ad.doubleclick.net'
]

commercial_urls = [
    'http://www.cbssports.com/nfl/superbowl/live/player',
    'https://twitter.com/SuperBowl',
    'https://twitter.com/search?q=%23superbowl'
]

## File paths
current_folder = os.path.dirname(__file__)
probe_path = current_folder + '/probe/'
try:
    os.stat(probe_path)
except:
    os.mkdir(probe_path)

trace_path = current_folder + '/trace/'
try:
    os.stat(trace_path)
except:
    os.mkdir(trace_path)