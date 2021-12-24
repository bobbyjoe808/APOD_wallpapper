import cv2
import ctypes
import nasapy
import os
from datetime import date, datetime
from datetime  import timedelta
import urllib.request
import ssl 

d = datetime.today() - timedelta(days=1)
d = d.strftime('%Y-%m-%d')


# get image and description

##
k = 'Your key here'
##

nasa = nasapy.Nasa(key=k)
apod = nasa.picture_of_the_day(date=d, hd=True)

title = d +' '+ apod["title"] + ".jpg"

##
image_dir = ' Put image directory here'
##

ssl._create_default_https_context = ssl._create_unverified_context
urllib.request.urlretrieve(url = apod["hdurl"] , filename = os.path.join(image_dir,title))

with open(image_dir+'/'+ d +' '+ apod["title"] + '.txt', 'w') as f:
    f.write(apod["explanation"])

path = image_dir+'/'+title

# size image and set as wallpaper
img = cv2.imread(path)
h, w = img.shape[:2]
#h1, w1 = int(h*3/2), int(w*3/2)
h1, w1 = int(1900), int(round(w*1900)/h)
resized_image = cv2.resize(img, (w1, h1))
cv2.imwrite(path, resized_image)

ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 1)

# show explanation on main screen automatically 

##
with open('C:/Users/'USER_NAME'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/space.txt', 'w') as f:
    f.write(apod["explanation"])
##

