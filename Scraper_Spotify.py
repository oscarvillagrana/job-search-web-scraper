Spodify_Setlist_Scraper.py

from bs4 import BeautifulSoup
import json

#
## example stacko 46258597
#

# data = '''
# </div>
#     </div>
#     <div data-integration-name="redux-container" data-payload='{"name":"LocationsMapList","props":{"locations":[{"id":17305,"company_id":106906,"description":"","city":"New York","country":"United States","address":"5 Crosby St  3rd Floor","state":"New York","region":"","latitude":40.719753,"longitude":-74.0001954,"hq":true,"created_at":"2015-01-19T01:32:16.317Z","updated_at":"2016-05-05T07:57:19.282Z","zip_code":"10013","country_code":"US","full_address":"5 Crosby St  3rd Floor, New York, 10013, New York, USA","dirty":false,"to_params":"new-york-us"}]},"storeName":null}' data-rwr-element="true">
# '''

# soup = BeautifulSoup(data, 'html.parser')
# for i in soup.find_all('div', attrs={'data-integration-name':'redux-container'}):
#     info = json.loads(i.get('data-payload'))
#     for i in info['props']['locations']:
#         print i['address']

#
## HTML to be scraped 
#

# <div class="tracklist-name ellipsis-one-line" dir="auto">Sigue Felíz</div>
# <div class="second-line">
# <span class="TrackListRow__artists ellipsis-one-line" dir="auto">
# <span class="react-contextmenu-wrapper"><span draggable="true">
# <a tabindex="-1" class="tracklist-row__artist-name-link" href="/artist/7x5Slu7yTE5icZjNsc3OzW">Willie Colón</a>
# </span></span>
# </span>
# <span class="second-line-separator" aria-label="in album">•</span>
# <span class="TrackListRow__album ellipsis-one-line" dir="auto">
# <span class="react-contextmenu-wrapper"><span draggable="true">
# <a tabindex="-1" class="tracklist-row__album-name-link" href="/album/5fY6IgtUM14tFh6iHwbT6l">La Gran Fuga</a>
# </span></span>
# </span></div>

class Playlist(object)

    def __init__(self, soup, track_name, artist_name, album_name)
        soup = BeautifulSoup(open(input("Enter a file to read: ")), "html.parser")
        track_name = soup.find_all('div', class_='tracklist-name ellipsis-one-line')
        artist_name = soup.find_all('div', class_='tracklist-row__artist-name-link')
        album_name = soup.find_all('div', class_='tracklist-row__album-name-link')


    # getters
    def get_track_name(self):
        for span in track_name:
            return span.text

    def get_artist_name(self):
        for a in artist_name:
            print(a.text)

    def get_album_name(self)
        for a in album_name:
            print(a.text)


#
## this is the same loop I came up with
#

# track name in playlist
track_name = soup.find_all('div', class_='tracklist-name ellipsis-one-line')
for span in track_name:
    print(span.text)

# because one row may have multiple artist, the list I am getting is not linening up with the number of tracks and albums collected
# I will need to find a way to put one tracks' artist in the same row

artist_name = soup.find_all('a', class_='tracklist-row__artist-name-link')
for a in artist_name:
    print(a.text)

album_name = soup.find_all('a', class_='tracklist-row__album-name-link')
for a in album_name:
    print(a.text)