#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import pandas as pd



try:
    soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
except FileNotFoundError:
    print("File Not Found. Exiting!")




#-----------------------------------------------------
# Scrape company and job information
#-----------------------------------------------------

def get_company_and_jobs():
    """this function scrapes the company names 
    and job titles"""
    company = soup.find_all('span', class_='company')
    title = soup.find_all('div', class_='title')
    for span in title:
        for x in company:
            print(x.text,span.text)

def get_company_names(self):
    """this function scrapes the company names"""
    company = soup.find_all('span', class_='company')
    for span in company:
        print(span.text)
    
def get_job_titles(self):
    """this function scrapes the job titles"""
    title = soup.find_all('div', class_='title')
    for span in title:
        print(span.text)

#-----------------------------------------------------
# Parse Data with Pandas DataFrame
#-----------------------------------------------------


def Parse_Data():
    """this function uses Pandas' DataFrame to parse data"""
    with open(input("Enter a file to read: "), 'r') as f:
        data = f.read()
    m = re.findall('(\w+)\n\n\n(\w+)', data)
    d = {'Company': [c[0] for c in m], 'Position': [c[1] for c in m]}
    df = pd.DataFrame(data=d)