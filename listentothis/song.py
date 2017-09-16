import re


class Song:
    def __init__(self, url):
        self.url = url
        # Title
        t = re.search('(?<=- ).+(?= [[])', self.url.string)
        self.title = None if t is None else t.group(0)
        # Artist
        a = re.search('.+(?= -)', self.url.string)
        self.artist = None if a is None else a.group(0)
        # Genre list
        self.genre_list = []
        bracket = re.findall('\[(.*?)\]', self.url.string)
        # Filtering out the years
        bracket = [b for b in bracket if re.search('[a-zA-Z]', b) is not None]
        for b in bracket:
            # Find all the genres
            self.genre_list += re.findall('[\w| |-]+', b)
            # Remove spaces if they are present before or after the genre name
            # Code needs to be put here!!!
        # Year
        y = re.search('\d{4}', self.url.string)
        self.year = None if y is None else y.group(0)
        # Link
        self.link = self.url.get('href')

    def __str__(self):
        output = ''
        output += 'title: ' + str(self.title) + '\n'
        output += 'artist: ' + str(self.artist) + '\n'
        output += 'genre/s: ' + str(self.genre_list) + '\n'
        output += 'year: ' + str(self.year) + '\n'
        output += 'link: ' + str(self.link)
        return output