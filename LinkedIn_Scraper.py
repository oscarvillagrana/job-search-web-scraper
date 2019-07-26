# Scraper_Linked_in.py

"""
<a data-control-id="/k9FAJq2SYSDWoW3J2RuKw==" data-control-name="A_jobssearch_job_result_click" href="/jobs/view/1002971771/?eBP=CwEAAAFr7HFQQ5GOeji5_qSMji15711rYmqonYcD0CrDqLgQrTIlJRU-VXNZqPIdg21B466ctny2rzQ5fs-SPPMyxKXiDOeWK5EacB9Z4G18KbQMF4Hww1Oi5E3Pd9W08cFrnLQfJUAv4ucWz2CeNaCKW0T1m2k_CjQvBtKmAdsCzQRGLBk_A-1Pci9UuUfcuRK34HIQYOimpVy6zifk8USeS6bE6vugcC2mm96_b-LnZhOgbF4cWTXugDgvnGYdYy2YgPXHp8chA7INL78E-YrJRHZefQqWqHEyB62xcGnsi42nMYRmuDZ30QIFQXhTrQ6Fz9THJnqE0MLPX_rVhZlqt67Fd5BLJF5C1hqRSqDKd011IxcAk_dxwv22yI-JgQZobgqpJbb2baNbGq8433n0HA&amp;recommendedFlavor=SCHOOL_RECRUIT&amp;refId=bcce5709-ad9d-4331-87b8-6b104ce5397e&amp;trk=d_flagship3_search_srp_jobs" id="ember147" class="job-card-search__link-wrapper js-focusable disabled ember-view">          Salesforce QA Engineer
            <span class="job-card-search__promoted-tag label-16dp ml1">
              Promoted
            </span>
</a>

<a data-control-id="/k9FAJq2SYSDWoW3J2RuKw==" data-control-name="job_card_company_link" href="/company/17751/" id="ember149" class="job-card-search__company-name-link ember-view">          Sage Intacct, Inc.
</a>


class_="job-card-search__link-wrapper js-focusable disabled ember-view"


class_="job-card-search__company-name-link ember-view"
"""

from bs4 import BeautifulSoup


soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
# ammends
title = soup.find_all('a', class_="job-card-search__link-wrapper js-focusable disabled ember-view")
company = soup.find_all('a', class_="job-card-search__company-name-link ember-view")
for span in title:
    for x in company:
        print(x.text,span.text)


# this loop finds all titles
title = soup.find_all('a', class_="job-card-search__link-wrapper js-focusable disabled ember-view")
for a in title:
    print(a.text)

# this loop finds all companies
company = soup.find_all('a', class_="job-card-search__company-name-link ember-view")
for a in company:
    print(a.text)

#
# Ex. Stako 40208610
#


for d in soup.find_all("div", class_="day"):
    notes = d.find_all("div", class_="note")
    teachers = d.find_all("div",class_="teacher")
    date = d.find("div", class_="date")
    times = d.find_all("div", class_="time")
    day = d.find("h3",class_="dayname")
    for note,time,   teacher in zip(notes,times,  teachers):
        note_text = note.text
        if "X2" in note_text:
            print((day.text, date.text, teacher.text,time.text, note.text))


# my version

for title, company in soup:
    print(title.text, company.text)

#
# Stako 40208610
#

data = [] 
soup = BeautifulSoup(open('scrape_out.txt'))

for lines in soup :  
    date = soup.find('div', attrs={'class': 'date'}).text.strip()
    day = soup.find('h3', attrs={'class': 'dayname'}).text.strip()
    teacher = soup.find('div', attrs={'class': 'teacher'}).text.strip()
    #lecture = soup.find('div', attrs={'a': })
    time = soup.find('div', attrs={'class': 'time'}).text.strip()
    location = soup.find('div', attrs={'class': 'location'}).text.strip()
    note = soup.find('div', attrs={'class': 'note'}).text.strip()

    data.append((day, date, teacher, time, note))

print data


# my version
data = [] 
soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")

for lines in soup :  
    title = soup.find('a', class_="job-card-search__link-wrapper js-focusable disabled ember-view").text.strip()
    company = soup.find('a', class_="job-card-search__company-name-link ember-view").text.strip()
    data.append((title, company))

print(data)

# my version
data = [] 
soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")

for lines in soup :  
    title = soup.find_all('a', class_="job-card-search__link-wrapper js-focusable disabled ember-view")
    company = soup.find_all('a', class_="job-card-search__company-name-link ember-view")
    data.append((title, company))

print(data)



#
# this loop finds all companies
#

for a in company:
    print(a.text)
