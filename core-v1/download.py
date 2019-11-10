import sys
import requests
from lxml import html

from bs4 import BeautifulSoup
# import requests
import re
import sys

# import sys
# import requests
# from lxml import html
# from bs4 import BeautifulSoup

from config_details import *
import os
from pySmartDL import SmartDL

def write_to_file(filename, content, flag='wb'):
    with open(filename, flag) as w:
        w.write(content)

def get_title_page(SCHOOL_ID, USERNAME, PASSWORD, URL):
    session_requests = requests.session()
    LOGIN_URL = "https://sso.teachable.com/secure/"+SCHOOL_ID + \
        "/users/sign_in?clean_login=true&reset_purchase_session=1"

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(
        set(tree.xpath("//meta[@name='csrf-token']/@content")))[0]
    authenticity_param = list(
        set(tree.xpath("//meta[@name='csrf-param']/@content")))[0]

    # Create payload
    payload = {
        "user[school_id]": SCHOOL_ID,
        "user[email]": USERNAME,
        "user[password]": PASSWORD,
        authenticity_param: authenticity_token
    }

    # Perform login
    result = session_requests.post(
        LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

    # Scrape url
    result = session_requests.get(URL, headers=dict(referer=URL))
    # print(result.content)
    return result.content


def get_contents(local_scrape_page):
    with open(local_scrape_page) as file:
        soup = BeautifulSoup(file, 'lxml')


    pattern = re.compile(r'\s+')

    return_string = ''
    counter = 1
    for match in soup.find_all('a', class_='item'):
        name = match.find('span', class_='lecture-name').text.strip()
        name = re.sub(pattern, '', name)
        name = str(counter) + '.' + name
        counter += 1
        return_string += name + '\n'

        href = match['href']
        href = 'https://codewithmosh.com'+href
        return_string += href + '\n'

    return return_string


def get_download_links(SCHOOL_ID, USERNAME, PASSWORD, contents_url):
    return_string = ''
    LOGIN_URL = "https://sso.teachable.com/secure/"+SCHOOL_ID + \
        "/users/sign_in?clean_login=true&reset_purchase_session=1"
    print(LOGIN_URL)
    f = open(contents_url, "r")

    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get(LOGIN_URL)
    tree = html.fromstring(result.text)
    authenticity_token = list(
        set(tree.xpath("//meta[@name='csrf-token']/@content")))[0]
    authenticity_param = list(
        set(tree.xpath("//meta[@name='csrf-param']/@content")))[0]

    # Create payload
    payload = {
        "user[school_id]": SCHOOL_ID,
        "user[email]": USERNAME,
        "user[password]": PASSWORD,
        authenticity_param: authenticity_token
    }

    # Perform login
    result = session_requests.post(
        LOGIN_URL, data=payload, headers=dict(referer=LOGIN_URL))

    # Scrape url
    c = 0
    inp = f.readline()
    while("END\n" not in inp):
        if(c % 2 == 0):
            return_string += inp.split('\n')[0] + '\n'
            print(inp.split('\n')[0])
        else:
            URL = inp.split('\n')[0]
            result = session_requests.get(URL, headers=dict(referer=URL))
            soup = BeautifulSoup(result.content, 'lxml')
            link = soup.find_all('a', class_='download')
            if(len(link) >= 1):
                href = link[0]['href']
                return_string += href + '\n'
                print(href)

        
        c += 1
        inp = f.readline()
    return return_string

def download_from_file(filename):
    f = open(filename, "r")
    name = ""

    url = f.readline()
    while(len(url) > 0):
        if(url.find('https://') >= 0):
            # print('url:'+url+'\nName:'+name)
            obj =SmartDL(url.strip('\n'), './'+name)
            obj.start()
            path = obj.get_dest()
        else:
            name = url.strip('\n') + '.mp4'

        print('Done downloading...'+name)
        url = f.readline()

print('Starting...: Scraping title page from '+TOPIC_NAME)
title_page = get_title_page(SCHOOL_ID, USERNAME, PASSWORD, TOPIC_URL)
write_to_file('title.html', title_page)
print('Finished...: Scraped into title.html\n')

print("Starting...: Local scraping of contents\n")
contents_page = get_contents('title.html')
write_to_file('contents.url', contents_page, 'w')
write_to_file('contents.url', 'END\n', 'a')
print('Finished...: Contents scraped\n')

print('Starting...:Removing unneccessary title.html\n')
os.remove('title.html')
download_links_filename = TOPIC_NAME.strip().replace(' ', '_') + '.txt'
download_links = get_download_links(SCHOOL_ID, USERNAME, PASSWORD, 'contents.url')
write_to_file(download_links_filename, download_links, 'w')
print('Finished...: '+download_links_filename)
os.remove('contents.url')

print('Starting Downloads...\n')
# download_from_file(download_links_filename)
download_from_file('C#_Developers:_Double_Your_Coding_Speed.txt')
