import urllib.request
import urllib.parse
import re
from bypass import bypassRead 

def run():
    print('Welcome to: Sankaku Complex Image Post Downloader')
    print('Please paste the complete URL')
    #e.x.: https://www.sankakucomplex.com/2010/11/23/my-little-cosplayer-cant-be-this-cute/
    url = input('URL: ')
    responseData = bypassRead(url)

    #PARSE HTML AND FIND IMG INSIDE "postcontent"
    imgDiv = re.findall(r'<div id="postcontent">(.*?)</div>', str(responseData))
    p = re.findall(r'<p>(.*?)</p>', str(imgDiv))
    for i in p:
        imgLink = re.findall(r'a href="(.*?)"', str(imgDiv))
    
    return(url, imgLink)
