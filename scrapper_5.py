import time
import urllib.request

urlroot = "http://www.kuttner-institute.jura.uni-muenchen.de/kartei/"
count = 1
filelocation = "C:/Archive/development/atria/atria/filelist2.txt"
outputfolder = "C:/Archive/development/atria/atria/images/"
sleeptime = 2


fhand1 = open(filelocation, encoding="utf8")

for c in fhand1:

    if len(c) < 0:
        print ("skip")
    else:
        c = c.strip()
        url = urlroot+c
        print (count, url)
 
        try:
            with urllib.request.urlopen(url) as response:
                image_data = response.read()
                filename = outputfolder + c
                with open(filename, 'wb') as f:
                    f.write(image_data)
                print("Downloaded image")
                time.sleep(sleeptime)
        except:
            print("Error downloading image", c)

        count = count + 1
    
