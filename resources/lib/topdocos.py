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

        path = i.get('href')

        items = {
            'label': label,
            'path': path,
        }

        output.append(items)

    return output


def get_categorys_content(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    content = soup.find_all('article', {'class': 'module'})

    output = []

    for i in content:
        label = i.find('h2')
        label = label.find('a').get('title')
        
        path = i.find('h2')
        path = path.find('a').get('href')

        items = {
                'label': label,
                'path': path,
        }

        output.append(items)

    return output


def play_categorys(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    content = soup.find('meta', {'itemprop': 'embedUrl'})
    
    output = []
   
    path = content.get('content').split('embed/')[1]

    label = soup.find('meta', {'itemprop': 'name'})
    label = label.get('content')
    print 'labe: '
    print label
    
    items = {
            'label': label,
            'path': path,
    }

    output.append(items)

    return output
    

play_categorys('http://topdocumentaryfilms.com/911-decade-deception/')
