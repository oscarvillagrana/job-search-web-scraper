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

pageSoup = get_soup()

#-----------------------------------------------------
# Prints company and job information
#-----------------------------------------------------

def print_company_and_jobs():
    """this function scrapes the company names 
    and job titles"""
    companyName = pageSoup.find_all('span', class_='company')
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        for x in companyName:
            print(x.text,span.text)

def print_company_names():
    """prints a list of the company names"""
    companyName = pageSoup.find_all('span', class_='company')
    for span in companyName:
        print(span.text)

def print_job_titles():
    """this function scrapes the job titles"""
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        print(span.text)

def get_company_and_jobs():
    """this function scrapes the company names 
    and job titles"""
    comps_and_jobs = []
    companyName = pageSoup.find_all('span', class_='company')
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:

        for x in companyName:
            comps_and_jobs.append(str(x.text))
            comps_and_jobs.append(str(span.text))
    return comps_and_jobs

def get_company_names():
    """this function scrapes the company names"""
    comp_names = []
    companyName = pageSoup.find_all('span', class_='company')
    for span in companyName:
        comp_names.append(str(span.text))
    return comp_names

def get_job_titles():
    """this function scrapes the job titles"""
    jobs = []
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        jobs.append(str(span.text))
    return jobs

#-----------------------------------------------------
# TODO: Get links from Soup and add them to df
#-----------------------------------------------------

# Here I am trying to translate this get_column_titles function 
# example into one that keeps the links of jobs and company

# example: data visualisation with python and javascript p.152

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

# my version so far:

def get_job_titles():
    """this function scrapes the job titles"""
    jobs = []
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        link = span.find('a')
        if link:
            comps.append({'name':link.text,
                          'href':link.attrs['href']})
        else:
            comps.append({'name':th.text, 'href':none})
    return span.text

#-----------------------------------------------------
# Parse Data with Pandas DataFrame
#
# TODO: Turn results into a table with pandas or a dict
#-----------------------------------------------------

def Parse_Data():
    """Turns html files list into a Pandas DataFrame"""
    with open(input("Enter a file to read: "), 'r') as f:
        data = f.read()
    
    m = re.findall('(\w+)\n(\w+)', data)
    d = {'Company': [c[0] for c in m], 'Position': [c[1] for c in m]}
    df = pd.DataFrame(data=d)

def Parse_Data1():
    """Turns the returned list into a Pandas DataFrame"""
    data = get_company_names()
    
    m = re.findall('(\w+)\n(\w+)', data)
    d = {'Company': [c[0] for c in m], 'Position': [c[1] for c in m]}
    df = pd.DataFrame(data=d)

#-----------------------------------------------------
# TODO: Remove Duplicates
#-----------------------------------------------------

#-----------------------------------------------------
# Here I am trying to figure out how to make a dataframe
# out of the get_company_and_jobs
#-----------------------------------------------------

# AttributeError when trying to append the output 
# from get_company_and_jobs

def make_table():
    company_name = []
    job_title = []
    company_name.append(companyName.replace("\n",""))
    job_title.append(jobTitle.text)
    df = pd.DataFrame({"company_name":company_name,"job_title":job_title})
    return df