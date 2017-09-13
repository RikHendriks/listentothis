from listentothis import *
from listentothis import *

import bs4 as bs
import urllib.request

# Open the sauce and the soup for the subreddit
sauce = urllib.request.urlopen('https://www.reddit.com/r/listentothis/').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# Find all the urls with class title
url_list = soup.find_all('a', attrs={'class': ['title']})

# Filter on https links
url_list = filter(lambda x: 'https' in x.get('href'), url_list)

# Get the song list
song_list = [Song(url) for url in url_list]

# Print the url list
for song in song_list:
    print(str(song) + '\n')