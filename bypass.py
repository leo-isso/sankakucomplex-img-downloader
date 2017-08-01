import urllib.request

#Bypassing Error 403
#User-Agent

def bypassOpen(adress):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    request = urllib.request.Request(adress, headers=headers)
    response = urllib.request.urlopen(request)

def bypassRead(adress):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    request = urllib.request.Request(adress, headers=headers)
    response = urllib.request.urlopen(request)
    responseData = response.read()
    return responseData
