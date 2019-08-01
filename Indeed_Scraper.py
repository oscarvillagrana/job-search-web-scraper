#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

#-----------------------------------------------------
# Ask the user to enter an html filename to scrape if
# not including a website url
#-----------------------------------------------------

# try:
#     soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
# except FileNotFoundError:
#     print("File Not Found. Exiting!")


page = "https://www.indeed.com/q-software-developer-l-San-Francisco-jobs.html"
headers = {'User-Agent':'Mozilla/5.0'}
session = requests.Session()
pageTree = session.get(page, headers=headers)
pageSoup = BeautifulSoup(pageTree.content, 'html.parser')



#-----------------------------------------------------
# Scrape company and job information
#-----------------------------------------------------

def get_company_and_jobs():
    """this function scrapes the company names 
    and job titles"""
    companyName = pageSoup.find_all('span', class_='company')
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        for x in companyName:
            print(x.text,span.text)

def get_company_names(self):
    """this function scrapes the company names"""
    companyName = pageSoup.find_all('span', class_='company')
    for span in companyName:
        print(span.text)
    
def get_job_titles(self):
    """this function scrapes the job titles"""
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        print(span.text)


#-----------------------------------------------------
# Parse Data with Pandas DataFrame
#-----------------------------------------------------


def Parse_Data():
    """Turns the returned list into a Pandas DataFrame"""
    # still using html files atm
    with open(input("Enter a file to read: "), 'r') as f:
        data = f.read()
    m = re.findall('(\w+)\n\n\n(\w+)', data)
    d = {'Company': [c[0] for c in m], 'Position': [c[1] for c in m]}
    df = pd.DataFrame(data=d)


#-----------------------------------------------------
# Here I am trying to figure out how to make a dataframe
# out of the get_company_and_jobs
#-----------------------------------------------------

###  TODO
# 
# AttributeError when trying to append the output 
# from get_company_and_jobs

company_name = []
job_title = []
company_name.append(companyName.replace("\n",""))
job_title.append(jobTitle.text)
df = pd.DataFrame({"company_name":company_name,"job_title":job_title})
