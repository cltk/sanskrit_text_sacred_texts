import urllib
import urllib.request
import re
import os 
import string
import regex
try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup

def make_dir(directory):
	if not os.path.exists(directory):
			os.makedirs(directory)	

def write_text(col1,target):

	col1=re.sub("\d+", "#", col1)
	lines=col1.split('#')
	no_sentences=0
	for l in range(len(lines)):
				line=lines[l]
				line=line.strip()
				line=line.replace(u'\xa0', u'')

				if line!="":
					target.write(line)
					target.write("\n")
					no_sentences+=1
	return no_sentences

def get_html(url_link):
	with urllib.request.urlopen(url_link) as url:
		return url.read()
		
def scrap_doc(url_chapter,name):	
	html=get_html(url_chapter)
	soup = BeautifulSoup(html)
	
	#to remove <a></a>
	for tag in soup.find_all('a'):
		tag.replaceWith('')
	
	tds = soup.find_all('td')
	col1=tds[0].text
	col2=tds[1].text

	target_l = open("dataset/Ramayana/latin/"+name[:-4]+"_latin.txt", 'w')
	target_d = open("dataset/Ramayana/devnagari/"+name[:-4]+"_dev.txt", 'w')

	if (write_text(col1,target_l) != write_text(col2,target_d)):
		print (name)

	
def get_chapter_links(link):
	
	url="http://sacred-texts.com/hin/rys/"+link
	#book_name=link #link extension for book 
	html=get_html(url)
	soup = BeautifulSoup(html)

	h_tag=soup.find('hr')
	for br in h_tag.find_next_siblings():
		link=br.get('href')
		if link!=None:
			scrap_doc("http://sacred-texts.com/hin/rys/"+link,link)

def get_links_books():

	directory="dataset/Ramayana/"
	directory_l="dataset/Ramayana/latin"
	directory_d="dataset/Ramayana/devnagari"
	make_dir(directory)
	make_dir(directory_d)
	make_dir(directory_l)
	
	url="http://sacred-texts.com/hin/rys/index.htm"
	
	html=get_html(url)
	soup = BeautifulSoup(html)


	h_tag=soup.find('hr')
	for br in h_tag.find_next_siblings():
		link=br.get('href')
		if link!=None:
			get_chapter_links(link)

if __name__ == "__main__":
	get_links_books()