#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

#-----------------------------------------------------
# If using local html files ask the user to 
# enter a filename 
#-----------------------------------------------------

def get_local_soup():
    try:
        return BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
    except FileNotFoundError:
        print("File Not Found. Exiting!")

page = "https://www.indeed.com/q-software-developer-l-San-Francisco-jobs.html"
headers = {'User-Agent':'Mozilla/5.0'}

def get_soup():
    session = requests.Session()
    pageTree = session.get(page, headers=headers)
    return BeautifulSoup(pageTree.content, 'html.parser')


#-----------------------------------------------------
# Scrape company and job information
#-----------------------------------------------------

pageSoup = get_soup()

def get_company_and_jobs():
    """this function scrapes the company names 
    and job titles"""
    companyName = pageSoup.find_all('span', class_='company')
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        for x in companyName:
            print(x.text,span.text)

def get_company_names():
    """this function scrapes the company names"""
    companyName = pageSoup.find_all('span', class_='company')
    for span in companyName:
        print(span.text)
    
def get_job_titles():
    """this function scrapes the job titles"""
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        print(span.text)


#-----------------------------------------------------
# making a my own df
# data visualisation p.152
#-----------------------------------------------------

# example
def get_column_titles(table):
    """ Get the Nobel categories from the table header """
    cols = []
    for th in table.find('tr').find_all('th')[1:]: 
        link = th.find('a')
        # Store the category name and any Wikipedia link it has
        if link:
            cols.append({'name':link.text,\
                         'href':link.attrs['href']})
        else:
            cols.append({'name':th.text, 'href':None})
    return cols

def get_company_names():
    """this function scrapes the company names"""
    comps = []
    companyName = pageSoup.find_all('span', class_='company')
    for span in companyName:
        link = span.select_one('a')
        if link:
            comps.append({'name':link.text,
                          'href':link.attrs['href']})
        else:
            comps.append({'name':th.text, 'href':none})
        print(span.text)


#    for th in table.select_one('tr').select('th')[1:]:

    
def get_job_titles():
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

def make_table():
    company_name = []
    job_title = []
    company_name.append(companyName.replace("\n",""))
    job_title.append(jobTitle.text)
    df = pd.DataFrame({"company_name":company_name,"job_title":job_title})
