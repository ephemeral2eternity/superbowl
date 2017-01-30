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
    'twNFL':'https://twitter.com/NFL',
    'twNFLpic':'https://pbs.twimg.com/profile_images/804347579475509248/THjHIDnN_400x400.jpg',
    'twPepsi':'https://twitter.com/pepsi',
    'twPepsiPic':'https://pbs.twimg.com/profile_images/762773014010327040/q4Bc_-Sz_400x400.jpg',
    'twPatriots':'https://twitter.com/Patriots',
    'twPatriotsPic':'https://pbs.twimg.com/profile_images/804697712734175232/42DnCaO2_400x400.jpg',
    'twNFLonFOX':'https://twitter.com/NFLonFOX',
    'twNFLonFOXPic':'https://pbs.twimg.com/profile_images/497792085869621250/o3Ze__SC_400x400.jpeg',
    'twFalcons':'https://twitter.com/AtlantaFalcons',
    'twFalconsPic':'https://pbs.twimg.com/profile_images/819252155190104064/Nd-8m09l_400x400.jpg',
    'twSuperBowl':'https://twitter.com/SuperBowl',
    'twSuperBowlPic':'https://pbs.twimg.com/profile_images/697894442569592832/TbP44AA8_400x400.jpg',
    'twMattRyan':'https://twitter.com/m_ryan02',
    'twMattRyanPic':'https://pbs.twimg.com/profile_images/819305718327046144/MBVfbZnW_400x400.jpg',
    'twBlount':'https://twitter.com/LG_Blount',
    'twBlountPic':'https://pbs.twimg.com/profile_images/823672964482826241/Ajz57Znk_400x400.jpg',
    'facebook':'https://www.facebook.com/',
    'facebookCDN':'https://fbcdn.net/',
    'fbPepsi':'https://www.facebook.com/PepsiUS/',
    'fbPepsiPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/p320x320/1098335_10152375519544050_1128198535_n.jpg?oh=678b70701661fc61e78ef4ccf4405e9b&oe=5904EDB9',
    'fbNFL':'https://www.facebook.com/NFL/',
    'fbNFLPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/p320x320/15056467_10154439610601263_2441588400849183241_n.jpg?oh=4611aab2fdeee667c7cd44f4122cbefa&oe=59069AAC',
    'fbPatriots':'https://www.facebook.com/newenglandpatriots/',
    'fbPatriotsPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/p200x200/10419064_10152937094182372_1259165244297845786_n.jpg?oh=1063cbe68be5545af16abd5f73c4adaa&oe=590219E4',
    'fbTomBrady':'https://www.facebook.com/TomBrady/',
    'fbTomBradyPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/c70.0.320.320/p320x320/12241318_1012406785467138_4732246889614416082_n.png?oh=e9b9460187d5322abe71b5513866701c&oe=591F5E12',
    'fbFalcons':'https://www.facebook.com/atlantafalcons/',
    'fbFalconsPic':'https://scontent-dft4-2.xx.fbcdn.net/v/t1.0-1/p320x320/15894628_10154390384577842_24953920858010758_n.jpg?oh=c04aa4f5fe85c57e82ea0c61991d0487&oe=590D0997'
}

cache_ips, cache_urls = load_cache_ips()