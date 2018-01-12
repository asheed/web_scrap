# -*- coding: utf-8 -*-
__author__ = 'woojin'
from urllib.request import urlopen
from bs4 import BeautifulSoup


if __name__ == '__main__':
	html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
	bsObj = BeautifulSoup(html, "html.parser")
	nameList = bsObj.findAll("span", {"class":"green"})
	for name in nameList:
		print(name)
		#print(name.get_text())
