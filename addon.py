from xbmcswift2 import Plugin, xbmcgui
from resources.lib import topdocos


PLUGIN_URL = 'plugin://plugin.video.youtube/?action=play_video&videoid='

plugin = Plugin()


@plugin.route('/')
def main_menu():

    items = [
        { 
            'label': plugin.get_string(30000),
            'path': plugin.url_for('doco_categorys'),
        }
    ]
    
    return items


@plugin.route('/doco_categorys/')
def doco_categorys():
    url = 'http://topdocumentaryfilms.com/all/'

    items = []

    content = topdocos.get_categorys(url)
   
    for i in content:
        items.append({
            'label': i['label'],
            'path': plugin.url_for('play_categorys', url=i['path']),
        })

    return items


@plugin.route('/doco_categorys/<url>')
def play_categorys(url):

    items = []

    content = 

if __name__ == '__main__':
    plugin.run()
