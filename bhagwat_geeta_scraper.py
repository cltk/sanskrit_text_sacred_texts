import urllib
import re
import os 
import string
import regex
import sys
try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def get_html(url_link):
	if sys.version_info < (3, 4):
			return urllib.urlopen(url_link)
	else:
		with urllib.request.urlopen(url_link) as url:
			return url.read()

def re_Write(name):
	path_="latin/_"+name+"_latin.txt"
	target_= open(path_, 'w')

	with open("latin/"+name+"_latin.txt") as f:
		for line in f:
			if line.rstrip() !='':
				target_.write(line.strip()+"\n")
	
def clean_geeta():
	#scrapping all books one by book
	for i in range (1,10): 
		re_Write('bgs0'+str(i))
	for i in range (10,19): 
		re_Write('bgs'+str(i))	

	
#scrapping all the linking together
def scrap_each_book(book_name,book_no):
	url="http://sacred-texts.com/hin/bgs/"+book_name+".htm"
	print (url)
	html = get_html(url)
	soup = BeautifulSoup(html)
	text=soup.find('body')

	text= text.encode('utf-8')
	text= text.replace('<br/>', '#')
	text = re.sub("([<](.)+[\s]+(.)+[>])|[<](.)+[/][>]", '', text)
	text=re.sub(r"([0-9]+\.[0-9]+)", "", text)
	text=re.split(r"#",text)

	target_ = open("latin/"+str(book_name)+"_latin.txt", 'w')
	no_sentences_=0
	for i in range(len(text)):
		line=text[i].rstrip()
		if line!="":
			target_.write(line.lower())
			target_.write("\n")
			no_sentences_+=1
	
def scrap_geeta():
	#scrapping all books one by book
	for i in range (1,10): 
		scrap_each_book('bgs0'+str(i),i)
	for i in range (10,19): 
		scrap_each_book('bgs'+str(i),i)	
	

if __name__ == "__main__":
	#scrap_geeta()
	clean_geeta()