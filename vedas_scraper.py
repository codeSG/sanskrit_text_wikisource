import re
import os 
import string
import regex
import urllib
#import urllib.request

try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup
def make_dir(directory):
	if not os.path.exists(directory):
			os.makedirs(directory)	
def get_html(url_link):
	with urllib.request.urlopen(url_link) as url:
		return url.read()
def clean_files():
	directory="Vedas/"
	path_="Vedas/skandapur_cleaned.txt"
	target_= open(path_, 'w')

	with open(directory+"skandapur.txt") as f:
		for line in f:
			if line.rstrip() !='':
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				line=re.sub(r"[.][/]", "", line)
				line=re.sub(r"(SP)(\w)+(\s)+", "", line)
				target_.write(line.strip())

				target_.write("\n")
def write_text(lines,target):

	
	no_sentences=0
	for l in range(len(lines)):
				line=lines[l]
				#line=line.strip()

				if line!="":
					target.write(line)
					target.write("\n")
					no_sentences+=1
	return no_sentences


		


def get_links_books():
	links=["https://sa.wikisource.org/wiki/%E0%A4%85%E0%A4%B7%E0%A5%8D%E0%A4%9F%E0%A4%BE%E0%A4%99%E0%A5%8D%E0%A4%97%E0%A4%B9%E0%A5%83%E0%A4%A6%E0%A4%AF%E0%A4%AE%E0%A5%8D/%E0%A4%B8%E0%A5%82%E0%A4%A4%E0%A5%8D%E0%A4%B0%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%BE%E0%A4%A8%E0%A4%AE%E0%A5%8D#.E0.A4.85.E0.A4.A7.E0.A5.8D.E0.A4.AF.E0.A4.BE.E0.A4.AF_01"]
	directory="Vedas/"
	make_dir(directory)
	url=links[0]
	
	html=get_html(url)
	#html=urllib.urlopen(url)
	soup = BeautifulSoup(html)

	path_="Vedas/Vedas.txt"
	target_= open(path_, 'w')

	text=soup.findAll('p')

	for i in range (3,len(text)):
		if text[i]!="":
			line=text[i].get_text()
			if  line.rstrip():
				line=re.sub(r"[\u0966-\u096F]+", "", line)
				line=re.sub(r"(\.|[\u0966-\u096F]*)([A-Za-z])\w*|([\u0966-\u096F]*\.[\u0966-\u096F]*)+|([\s])+॥$", "", line)
				target_.write(line.strip())
				target_.write("\n")
if __name__ == "__main__":
	get_links_books()