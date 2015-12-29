from bs4 import BeautifulSoup as bs
import requests
import re


def get_categorys(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    content = soup.find('nav', {'class': 'module clear'})
    content = content.find_all('a')
    
    output = []

    for i in content:
        label = i.get_text()
        print 'label: '
        print label

        path = i.get('href')
        print 'path: '
        print path

        items = {
            'label': label,
            'path': path,
        }

        output.append(items)

    return output

#get_categorys('http://www.topdocumentaryfilms.com/category/crime/')


def get_categorys_content(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')

