from xbmcswift2 import Plugin, xbmcgui
from resources.lib import topdocos
from bs4 import BeautifulSoup as bs
import requests

PLUGIN_URL = 'plugin://plugin.video.youtube/?action=play_video&videoid='
SITE_URL = 'http://topdocumentaryfilms.com/'

plugin = Plugin()

def get_soup(url):
    page = requests.get(url)
    soup = bs(page.text, 'html.parser')
    
    return soup

@plugin.route('/')
def main_menu():

    items = [
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('recent'),
        },
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('highest_rated'),
        },
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('most_voted'),
        },
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('most_shared'),
        },
        { 
            'label': plugin.get_string(30005),
            'path': plugin.url_for('categorys'),
        }
    ]
    
    return items


@plugin.route('/recent/')
def recent():
    
    items = []

    content = topdocos.get_section(SITE_URL, 'recently added')

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_content', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    return items


@plugin.route('/highest_rated/')
def highest_rated():

    items = []

    content = topdocos.get_section(SITE_URL, 'highest rated')

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_content', url=i['path']),
        })

    return items


@plugin.route('/most_voted/')
def most_voted():

    items = []

    content = topdocos.get_section(SITE_URL, 'most voted')

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_content', url=i['path']),
        })

    return items


@plugin.route('/most_shared/')
def most_shared():

    items = []

    content = topdocos.get_section(SITE_URL, 'most shared')

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_content', url=i['path']),
        })

    return items


@plugin.route('/categorys/')
def categorys():
    url = 'http://topdocumentaryfilms.com/all/'

    items = []

    content = topdocos.get_categorys(url)
   
    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('get_categorys', url=i['path']),
        })

    return items


@plugin.route('/categorys/<url>')
def get_categorys(url):

    items = []

    content = topdocos.get_categorys_content(url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_content', url=i['path']),
            'thumbnail': i['thumbnail'],
        })

    thumb = ''
    items2 = []
    soup = get_soup(url)
    paging = soup.find_all('div', {'class': 'pagination module'})
    for i in paging:
		content = i.find_all('a')
		for j in content:
			path = j.get('href')
			label = j.string
			thumb = ''
			if label in ('Previous', 'Next'):
				items2 = {
						'label': label,
						'path': plugin.url_for('get_categorys', url=path),
						'thumbnail': thumb,
				}
				items.append(items2)
		
    return items


@plugin.route('/doco_categorys/get_categorys/<url>/')
def play_content(url):

    items = []

    content = topdocos.play_categorys(url)

    for i in content:
        items.append({
            'label': i['label'],
            'path': PLUGIN_URL + i['path'],
            'is_playable': True,
        })

    return items


if __name__ == '__main__':
    plugin.run()
