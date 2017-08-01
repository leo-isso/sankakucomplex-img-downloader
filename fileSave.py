import urlFilter
import os
import urllib.request


def createFiles():
    url, imgLink = urlFilter.run()
    #Bypassing Error 403
    bypass = urllib.request.URLopener()
    bypass.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

    #Creates new folder name based on URL link
    urlSplit = url.split('/')
    filePath = urlSplit[-2]

    #Creates new dir
    print('Creating new dir for your images')
    if not os.path.exists(filePath):
        os.makedirs(filePath)
        print('New dir ' + filePath)
    else:
        print('dir already exists, resuming')

    #Scrap images
    for newImg in imgLink:
        #Create image name based on URL link
        #Check file format
        #Check http, https existence on string
        #Retrieve file
        imgSplit = newImg.split('/')
        imgName = imgSplit[-1]
        if any(ext in imgName for ext in['jpg', 'jpeg', 'gif', 'png']):
            if 'https:' in newImg or 'http:' in newImg:
                try:
                    filePathTemplate = filePath + '\\' + imgName
                    bypass.retrieve(newImg, filePathTemplate)
                    print(imgName + ' was save!')
                except:
                    print('Error with ' + newImg)
            else:
                try:
                    filePathTemplate = filePath + '\\' + imgName
                    bypass.retrieve('https:' + newImg, filePathTemplate)
                    print(imgName + ' was save!')
                except:
                    print('Error with (https:) ' + newImg)
        else:
            print(newImg + ' is not an image')
    print('Finished!')
    '''
    #TEST LINKS OUTPUT
    saveFile = open('output.txt','w')
    saveFile.write(str(imgLink))
    '''

    
