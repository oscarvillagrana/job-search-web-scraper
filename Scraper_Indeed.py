#!/bin/python
# Scraper_Indeed

########################################################
#
# Extract company name and job title from html file
#
########################################################        


from bs4 import BeautifulSoup

# this loop ammends each title & company per result
soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")

company = soup.find_all('span', class_='company')
title = soup.find_all('div', class_='title')

for span in title:
    for x in company:
        print(x.text,span.text)


########################################################
#
# parse data using regex and convert to DataFrame
#
########################################################


import re
import pandas as pd

with open(input("Enter a file to read: "), 'r') as f:
    data = f.read()

m = re.findall('(\w+)\n\n\n(\w+)', data)
d = {'Company': [c[0] for c in m], 'Position': [c[1] for c in m]}
df = pd.DataFrame(data=d)


#
# use zip to ammend different html tags
# stacko example 47863031
#


company = soup.find_all('span', class_='company')
title = soup.find_all('div', class_='title')
for t,c  in zip(title, company): 
    print ("Job_Title :%s Company_Name :%s" %(t,c)) 


#
# stacko example 47863031
#

soup = BeautifulSoup(open(filename), "html.parser")
data = ''.join([' '.join(span.text.split()) for span in soup.select(".NormalTextRun")])
print(data)

from bs4 import BeautifulSoup
soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
data = ''.join([' '.join(item.text.split()) for item in soup.select(".NormalTextRun")])
print(data)

dates = '' 
for data in elem.find_all('span', class_='TextRun'):
    dates.join([dates, data.text])


#
# my version
#

soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
title = soup.find_all('div', class_='title')
for span in title:
    print(span.text)

soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
for title in soup.find_all('div', class_='title'):
    for span in title:
    print(span.text)


soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
titles = ''
for title in soup.find_all('div', class_='title'):
    titles.join([titles, span.text])
    print(titles)

dates = '' 
for data in soup.find_all('span', class_='title'):
    dates.join([dates, data.text])

#
# new version
#

from bs4 import BeautifulSoup

soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")

company = soup.find_all('span', class_='company')
title = soup.find_all('div', class_='title')

for each in soup:
    print(each.text.strip().encode('utf-8'))

print each.text.strip().encode('utf-8')



for span in title:
for span in company:
    print(span.text)
    print(span.text)




title = 

for span in soup.find_all('div', class_='title'):
    print(span.text)
    for span in soup.find_all('span', class_='company'):
        print(span.text)
    print(span.text)

#
# what if I add the attributes in one line
#

for span in soup.find_all('div', class_='title', class_='company'):
    print(span.text)


#
# example 
#

print each.text.strip().encode('utf-8')


########################################################
#
# Class
#
########################################################        


from bs4 import BeautifulSoup

class Job_Search(object):
    """A job search downloaded as a HTML file"""


    def __init__(self, soup, title, company):
        self.soup = self._soup()
        self.title = title
        self.company = company

    def soup(self):
        soup = BeautifulSoup(open(filename), "html.parser")

    # getters
    def get_job_title(self):
        """this function scrapes the job titles"""
        title = soup.find_all('div', class_='title')
        for span in title:
            print(span.text)

    def get_company_name(self):
        """this function scrapes the job titles"""
        company = soup.find_all('span', class_='company')
        for span in company:
            print(span.text)

    def __repr__(self):
        return " Job_Search class representing a job search html page"


########################################################
#
# Extracts individualy the company names and job titles
# from a html file
#
########################################################        


soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")

# this loop finds all job titles
title = soup.find_all('div', class_='title')
for span in title:
    print(span.text)

# this loop finds all companies
company = soup.find_all('span', class_='company')
for span in company:
    print(span.text)
