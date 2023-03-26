#!/usr/bin/env python

import os
import time
import pandas
import urllib.request

file = pandas.read_csv("tiles_list.csv")

paths = file['path'].tolist()
urls = file['url'].tolist()

k1 = 0
k2 = 0


for (path, url) in zip(paths, urls):
    k1 += 1
    k2 += 1
    if(os.path.isfile(path)):
        continue
    print(str(k1) + " Downloading : " + path[83:])
    urllib.request.urlretrieve(url, path)
    if(k2 >= 50):
        k2 = 0
        time.sleep(30)
    
    
