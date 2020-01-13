#!/usr/bin/python
# Local_HTML_Parser.py
# Author: Oscar Villagrana

from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

#---------------------------
# Parsing with BeautifulSoup
#---------------------------

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


#-----------------------------------------------------
# Parsing with Pandas
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

