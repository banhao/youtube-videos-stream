# youtube-videos-stream.py
#_*_coding: utf-8_*_

import sys, unittest, time, datetime
import urllib.request, urllib.error, urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException

filename = sys.argv[1]
channelid = filename.split('-')[0]
fp = open(filename, "r")
#driver=webdriver.Firefox()
driver=webdriver.Chrome()
for url in fp.readlines():
	url = url.rstrip("\n")
	driver.get(url)
#	except InvalidArgumentException:
#		print(url)
	time.sleep(10)
	stream = driver.find_element_by_xpath('//*[@id="date"]/yt-formatted-string')
	f = open(channelid+'-videos-stream.list', 'a+')
	f.write(url + ";" + stream.text + "\n")
f.close
