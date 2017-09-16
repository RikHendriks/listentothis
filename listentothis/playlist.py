from .song import *

import bs4 as bs
import urllib.request


class PlayList:
    def __init__(self, url, user_agent):
        self.url = url
        # Open the sauce and the soup for the subreddit
        hdr = {'User-Agent': user_agent}
        req = urllib.request.Request(url=self.url, headers=hdr)
        self.sauce = urllib.request.urlopen(req).read()
        self.soup = bs.BeautifulSoup(self.sauce, 'lxml')
        # Find all the urls with class title
        url_list = self.soup.find_all('a', attrs={'class': ['title']})
        # Filter on https links
        self.url_list = filter(lambda x: 'https' in x.get('href'), url_list)
        # Get the song list
        self.song_list = [Song(s_url) for s_url in self.url_list]

    def __str__(self):
        output = ''
        # Print the url list
        for i in range(0, len(self.song_list)):
            output += str(self.song_list[i])
            if i is not len(self.song_list)-1:
                output += '\n\n'
        return output