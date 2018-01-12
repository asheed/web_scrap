# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

__author__ = 'woojin'

def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read(), "html.parser")
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title

if __name__ == '__main__':
	#title = getTitle("http://pythonscraping.com/pages/page1.html")
	title = getTitle("http://daum.net")

	if title == None:
		print("Title could not be found")
	else:
		print(title)