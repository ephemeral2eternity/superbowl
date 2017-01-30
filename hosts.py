import os
from ips.load_ips import *

commercial_hosts = {
    'netflix':'netflix753.as.nflximg.com.edgesuite.net',
    'foxsports':'hlslinear-l3c.med1.foxsportsgo.com',
    'conviva':'gwb.lphbs.com',
    'doubleclick': 'ad.doubleclick.net',
    'doubleclick-stat': 'stats.l.doubleclick.net',
    'google-tag-manager':'www.googletagmanager.com',
    'papajohns':'www.papajohns.com',
    'lube':'quakersteakandlube.alohaorderonline.com',
    'twitter':'www.twitter.com',
    'twimg':'twimg.com',
    'pbstwimg':'pbs.twimg.com',
    'videotwimg':'video.twimg.com',
    'facebook':'www.facebook.com',
    'fbcdn':'fbcdn.net'
}

commercial_urls = {
    'foxSportsGo':'https://www.foxsportsgo.com/',
    'pizzahut':'https://www.pizzahut.com/#/home',
    'lube':'https://quakersteakandlube.alohaorderonline.com/',
    'papajohns':'https://www.papajohns.com/',
    'twitter':'https://twitter.com/',
    'twimg':'https://twimg.com/',
    'pbstwimg':'http://pbs.twimg.com/',
    'twsports':'https://twitter.com/i/streams/category/686639666771046402',
    'twHashSB':'https://twitter.com/hashtag/superbowl',
    'twHashPepsi':'https://twitter.com/hashtag/pepsihalftime',
    'twHashSB51':'https://twitter.com/hashtag/sb51',
    'twNFLpic':'https://pbs.twimg.com/profile_images/804347579475509248/THjHIDnN_400x400.jpg',
    'twPepsiPic':'https://pbs.twimg.com/profile_images/762773014010327040/q4Bc_-Sz_400x400.jpg',
    'twPatriotsPic':'https://pbs.twimg.com/profile_images/804697712734175232/42DnCaO2_400x400.jpg',
    'twNFLonFOXPic':'https://pbs.twimg.com/profile_images/497792085869621250/o3Ze__SC_400x400.jpeg',
    'facebook':'https://www.facebook.com/',
    'facebookCDN':'https://fbcdn.net/',
    'fbPepsi':'https://www.facebook.com/PepsiUS/',
    'fbPepsiPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/p320x320/1098335_10152375519544050_1128198535_n.jpg?oh=678b70701661fc61e78ef4ccf4405e9b&oe=5904EDB9',
    'fbNFL':'https://www.facebook.com/NFL/',
    'fbNFLPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/p320x320/15056467_10154439610601263_2441588400849183241_n.jpg?oh=4611aab2fdeee667c7cd44f4122cbefa&oe=59069AAC',
    'fbPatriots':'https://www.facebook.com/newenglandpatriots/',
    'fbPatriotsPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/p200x200/10419064_10152937094182372_1259165244297845786_n.jpg?oh=1063cbe68be5545af16abd5f73c4adaa&oe=590219E4',
}

cache_ips, cache_urls = load_cache_ips()