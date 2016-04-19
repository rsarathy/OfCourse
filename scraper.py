from bs4 import BeautifulSoup
import urllib2

# webpage = urllib2.urlopen('http://en.wikipedia.org/wiki/Main_Page')
webpage = urllib2.urlopen('http://courses.illinois.edu/schedule/2016/fall/CS/425/')
soup = BeautifulSoup(webpage,'html.parser')

ptags = soup.find_all('p')

CREDIT = ptags[0].text
DESCRP = ptags[1].text
PREREQ = ptags[2].text

print CREDIT
print DESCRP
print PREREQ

with open("newcourses.txt", "a") as myfile:
    pass


# for ptag in soup.find_all('p'):
#     print ptag.text
