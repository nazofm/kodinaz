import sys
import xbmcgui
import xbmcplugin
import urllib
import urllib2
import re
import fileinput

 
addon_handle = int(sys.argv[1])
 
xbmcplugin.setContent(addon_handle, 'movies')


url = ''
li = xbmcgui.ListItem('[COLOR yellow]National[/COLOR]', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ozmap.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101002210220m3u8'
li = xbmcgui.ListItem('ABC News (24)', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/abcnews.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101002310231.m3u8'
li = xbmcgui.ListItem('ABC', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/abc.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.abc2.m3u8'
li = xbmcgui.ListItem('ABC Comedy', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/comedy.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101002210222.m3u8'
li = xbmcgui.ListItem('ABC KIDS', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/kids.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101002210224.m3u8'
li = xbmcgui.ListItem('ABC ME', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/abcme.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'rtmp://118.97.183.196/jhos//aplus|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Australia Plus', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/aplus.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://foxsportshlsg01-lh.akamaihd.net/i/fsnewshls_0@301672/index_4625_av-p.m3u8?sd=10&rebase=on|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Fox Sports News', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/fox.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://melbourneseven-i.akamaihd.net/hls/live/263815-b/RAC/master_1000.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Racing.com', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/racing.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


url = 'http://sbslivefvstreaming.sbs.com.au/out/u/sbs1-mo-000-c3093-delpkg1-delpkg1-abr/index-root-ipad.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('SBS One', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/SBS.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://sbslivefvstreaming.sbs.com.au/out/u/sbs2-mo-000-c3093-delpkg1-delpkg1-abr/index-root-ipad.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('SBS Viceland', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/viceland.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://sbslivefvstreaming.sbs.com.au/out/u/fdnet-mo-000-c3094-delpkg1-delpkg1-abr/index-root-ipad.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('SBS Food Network', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/food.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://sbslivefvstreaming.sbs.com.au/out/u/nitv-mo-000-c3094-delpkg1-delpkg1-abr/index-root-ipad.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('NITV', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/nitv.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


url = ''
li = xbmcgui.ListItem('[COLOR yellow]Melbourne [/COLOR]', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ozmap.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101305030530.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/seven.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101305030532.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Two', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7two.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101305030533.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Mate', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7mate.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101305030535.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Flix', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7flix.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101204300430.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/nine.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101204300436.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Gem', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9gem.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101204300437.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Go', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9go.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101204300433.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Life', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9life.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://iptv.matthuisman.nz/au/Melbourne/tv.101406030635.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Ten (when live)', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ten.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = ''
li = xbmcgui.ListItem('[COLOR yellow]Perth[/COLOR]', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ozmap.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://perthseven-i.akamaihd.net/hls/live/263674/PER1/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/seven.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://perthseven-i.akamaihd.net/hls/live/263675/PER2/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Two', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7two.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://perthseven-i.akamaihd.net/hls/live/263676/PER3/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Mate', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7mate.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://perthseven-i.akamaihd.net/hls/live/263677/PER6/master_1000.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Flix', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7flix.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://9nowch9livehls-i.akamaihd.net/hls/live/250963/perth/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/nine.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgemlivehls-i.akamaihd.net/hls/live/250973/perth/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Gem', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9gem.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgolivehls-i.akamaihd.net/hls/live/250978/perth/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Go', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9go.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowlifelivehls-i.akamaihd.net/hls/live/250993/perth/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Life', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9life.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li) 

url = 'http://csm-e.cds1.yospace.com/csm/extlive/networkten01,SDNEW.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Ten (when live)', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ten.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


url = ''
li = xbmcgui.ListItem('[COLOR yellow]Brisbane[/COLOR]', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ozmap.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://brisbaneseven-i.akamaihd.net/hls/live/263663/BRI1/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/seven.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://brisbaneseven-i.akamaihd.net/hls/live/263664/BRI2/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Two', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7two.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://brisbaneseven-i.akamaihd.net/hls/live/263665/BRI3/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Mate', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7mate.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://brisbaneseven-i.akamaihd.net/hls/live/263666-b/BRI6/master_1000.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Flix', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7flix.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://9nowch9livehls-i.akamaihd.net/hls/live/250961/brisbane/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/nine.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgemlivehls-i.akamaihd.net/hls/live/250971/brisbane/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Gem', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9gem.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgolivehls-i.akamaihd.net/hls/live/250976/brisbane/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Go', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9go.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowlifelivehls-i.akamaihd.net/hls/live/250991/brisbane/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Life', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9life.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li) 

url = 'http://csm-e.cds1.yospace.com/csm/extlive/networkten01,SDTVQ.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Ten (when live)', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ten.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = ''
li = xbmcgui.ListItem('[COLOR yellow]Sydney[/COLOR]', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ozmap.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://sydneyseven-i.akamaihd.net/hls/live/263630/SYD1/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/seven.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://sydneyseven-i.akamaihd.net/hls/live/263631/SYD2/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Two', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7two.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://sydneyseven-i.akamaihd.net/hls/live/263632/SYD3/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Mate', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7mate.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://sydneyseven-i.akamaihd.net/hls/live/263634-b/SYD6/master_1000.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Flix', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7flix.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://9nowch9livehls-i.akamaihd.net/hls/live/250964/sydney/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/nine.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgemlivehls-i.akamaihd.net/hls/live/250974/sydney/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Gem', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9gem.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgolivehls-i.akamaihd.net/hls/live/250987/sydney/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Go', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9go.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowlifelivehls-i.akamaihd.net/hls/live/250994/sydney/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Life', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9life.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://csm-e.cds1.yospace.com/csm/extlive/networkten01,SDTEN.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Ten (when live)', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ten.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)


url = ''
li = xbmcgui.ListItem('[COLOR yellow]Adelaide[/COLOR]', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ozmap.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://adelaideseven-i.akamaihd.net/hls/live/263667/ADE1/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/seven.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://adelaideseven-i.akamaihd.net/hls/live/263668/ADE2/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Two', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7two.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://adelaideseven-i.akamaihd.net/hls/live/263669/ADE3/master_1250.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Mate', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7mate.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://adelaideseven-i.akamaihd.net/hls/live/263670-b/ADE6/master_1000.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('7Flix', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/7flix.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'https://9nowch9livehls-i.akamaihd.net/hls/live/250960/adelaide/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/nine.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgemlivehls-i.akamaihd.net/hls/live/250970/adelaide/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Gem', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9gem.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowgolivehls-i.akamaihd.net/hls/live/250975/adelaide/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Go', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9go.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
url = 'https://9nowlifelivehls-i.akamaihd.net/hls/live/250990/adelaide/master1.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('9Life', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/9life.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://csm-e.cds1.yospace.com/csm/extlive/networkten01,SDADS.m3u8|X-Forwarded-For=110.33.122.75'
li = xbmcgui.ListItem('Ten (when live)', iconImage='https://raw.githubusercontent.com/nazofm/kodinaz/master/icons/ten.png')
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)



xbmcplugin.endOfDirectory(addon_handle)
