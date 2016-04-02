import urllib
import re
import os 
import string
import urllib.request
import regex
try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def get_html(url_link):
	with urllib.request.urlopen(url_link) as url:
		return url.read()

def write_text(target_new,target_old):


	no_sentences=0
	for line in target_old:
				
				line=line.strip()
				if line!="":
					target_new.write(line+"\n")
					no_sentences+=1
	#print no_sentences				
	return no_sentences
				
def scrap_doc(name,book_name):	
	folder=book_name[:-4]
	target_r = open("dataset/Mahabharata/"+folder+"/"+name+"_roman.txt", 'r')
	target_s = open("dataset/Mahabharata/"+folder+"/"+name+"_sans.txt", 'r')

	target_r_w = open("dataset/Mahabharata/latin/"+name[:-4]+"latin.txt", 'w')
	target_s_w = open("dataset/Mahabharata/devangari/"+name[:-4]+"dev.txt", 'w')

	if (write_text(target_s_w,target_s) != write_text(target_r_w,target_r)):
		print (name)

def make_dir(directory):
	if not os.path.exists(directory):
			os.makedirs(directory)
	
def get_chapter_links(link):

	url="http://sacred-texts.com/hin/mbs/"+link
	book_name=link
	#html = urllib.urlopen(url)
	html=get_html(url)
	soup = BeautifulSoup(html)

	h_tag=soup.find('hr')
	for br in h_tag.find_next_siblings():
		link=br.get('href')
		if link!=None:
			scrap_doc(link,book_name)

def get_links_books():

	make_dir("dataset/Mahabharata/latin")
	make_dir("dataset/Mahabharata/devangari")

	url="http://sacred-texts.com/hin/mbs/index.htm"
	
	#html = urllib.urlopen(url)
	html=get_html(url)	
	soup = BeautifulSoup(html)


	h_tag=soup.find('hr')
	for br in h_tag.find_next_siblings():
		link=br.get('href')
		if link!=None:
			get_chapter_links(link)

if __name__ == "__main__":
	get_links_books()