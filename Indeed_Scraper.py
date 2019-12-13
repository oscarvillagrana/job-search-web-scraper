#!/usr/bin/python

from bs4 import BeautifulSoup
import re
import pandas as pd
import requests


#-------------------------------------------------
# Making the Soup
#-------------------------------------------------


# ask the user to enter a local html filename
def get_local_soup():
    try:
        return BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
    except FileNotFoundError:
        print("File Not Found. Exiting!")

def get_input_soup():
    try:
        return BeautifulSoup(open(input("Enter a website to read: ")), "html.parser")
    except FileNotFoundError:
        print("Site Not Found. Exiting!")

def format_page():
    print("First we will format the job search with rearch keywords")
    sub0 = input("Enter first Job Search keyword: ")
    sub1 = input("Enter second Job Search keyword: ")
    page = "https://www.indeed.com/jobs?as_and={0}+{1}&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&as_src=&salary=&radius=0&l=San+Francisco&fromage=any&limit=50&sort=&psf=advsrch"
    a = page.format(sub0, sub1)
    return a     

page = "https://www.indeed.com/q-software-developer-l-San-Francisco-jobs.html"

# page = format_page()
headers = {'User-Agent':'Mozilla/5.0'}

def get_soup():
    session = requests.Session()
    pageTree = session.get(page, headers=headers)
    return BeautifulSoup(pageTree.content, 'html.parser')

pageSoup = get_soup()

# print(pageSoup)

#----------------------------------------------------
# Getters
#----------------------------------------------------

def print_company_names():
    companyName = pageSoup.find_all('span', class_='company')
    for span in companyName:
        print(span.text)

# print_company_names()

def print_job_titles():
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        print(span.text)

# print_job_titles()

# Prints company and job information
def print_company_and_jobs():
    companyName = pageSoup.find_all('span', class_='company')
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        for x in companyName:
            print(x.text,span.text)

# print_company_and_jobs()


# Makes a list with company and job information
def get_company_and_jobs():
    comps_and_jobs = []
    companyName = pageSoup.find_all('span', class_='company')
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        for x in companyName:
            comps_and_jobs.append(str(x.text))
            comps_and_jobs.append(str(span.text))
    return comps_and_jobs

# get_company_and_jobs()

def get_company_names():
    comp_names = []
    companyName = pageSoup.find_all('span', class_='company')
    for span in companyName:
        comp_names.append(str(span.text))
    return comp_names

def get_job_titles():
    jobs = []
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        jobs.append(str(span.text))
    return jobs


#-----------------------------------------------------
# TODO: Turn results into a table with pandas or a dict
#-----------------------------------------------------


# Parse Data with html files
def Parse_Local_Data():
    with open(input("Enter a file to read: "), 'r') as f:
        data = f.read()
    m = re.findall('(\w+)\n(\w+)', data)
    d = {'Company': [c[0] for c in m], 'Position': [c[1] for c in m]}
    df = pd.DataFrame(data=d)

def Parse_Data():
    data = get_company_names()    
    m = re.findall('(\w+)\n(\w+)', data)
    d = {'Company': [c[0] for c in m], 'Position': [c[1] for c in m]}
    df = pd.DataFrame(data=d)


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
            cols.append({'title':link.text,\
                         'href':link.attrs['href']})
        else:
            cols.append({'title':th.text, 'href':None})
    return cols

# my version so far:
def get_job_titles():
    jobs = []
    jobTitle = pageSoup.find_all('div', class_='title')
    for span in jobTitle:
        link = span.find('href')
        if link:
            jobs.append({'title':link.text,
                          'href':link.attrs['href']})
        else:
            jobs.append({'title':span.text, 'href':None})
    return jobs


#not working
def print_links(): 
    jobLink = pageSoup.find_all('div', class_='title')
    for div in jobLink: 
        print(div.find('a')['href']) 

#not working
def print_links(): 
    jobLink = [div.a for div in pageSoup.find_all('div', class_='title')]
    for div in jobLink: 
        print(div['href']) 


#-----------------------------------------------------
# TODO: Make table
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


#-----------------------------------------------------
# TODO: Remove Duplicates
# Python for data analysis.pg.194.e379
#-----------------------------------------------------


def remove_duplicates():
    data = get_company_and_jobs()
    # returns boolean indicating duplicate row
    data.duplicated()
    # returns a df where the duplicated array is True
    data.drop_duplicates(['column1'])
    # take_last will return the last observed value combination and default keeps the first
    data.drop_duplicates(['column1','column2'], take_last=True)