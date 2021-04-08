# import the required modules
import requests
from bs4 import BeautifulSoup
import pprint

# use the module requests to acces the url
res = requests.get('https://news.ycombinator.com/news')
# 'https://news.ycombinator.com/news?p=2'

# res.text transform all the information from url to a string
# BeautifulSoup convert that string into a html object
soup = BeautifulSoup(res.text, 'html.parser')

#.storylink allows us to grab the class that has the links of each news
links = soup.select('.storylink')

# Grab all the elements that have the score class
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse= True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))