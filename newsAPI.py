from newsapi import NewsApiClient
from aylienapiclient import textapi
import sys
import textcleaner as tc


#Setup API Keys
news_api = NewsApiClient(api_key='e65ead4cf44c49efa7eeac4a9fc4aa7c')
extraction_api = textapi.Client("a65d9a56", "1946036c4ab9e433a7f87a45405f6235")



#Get article from Url
url = firstarg=sys.argv[1]
article = extraction_api.Extract({'url': url})
title = article['title']
print()
print("Url article title")
print(article['title'])
print()



#Find Related Articles
# Early stages currently only does one word queries
headlines = []
for word in title:
        
        # /v2/top-headlines
        top_headlines = news_api.get_top_headlines(q=word,
                                                language='en',
                                                )

        for headline in top_headlines['articles']:
                if headline not in headlines:
                        headlines.append(headline)

# print(titles[:3])
# data = tc.document(titles)
# titles = data.remove_stpwrds()
# print(titles)
# print()
# print()
# print()


def similar(s1, s2):
    sameWords = set.intersection(set(s1.split(" ")), set(s2.split(" ")))
    return len(sameWords)
def getKey(item):
        return item[0]

currentSimilar = 0

rank = []

for headline in headlines:
        similiarity = similar(title.lower(), headline['title'].lower())
        rank.append([similiarity,headline])
        # print()
        # print(similiarity)
        # print(headline['title'])
        # print()

rank = sorted(rank, key=getKey, reverse = True)
print("Similar Articles")
for i in range(5):
        print()
        print(rank[i][1]['title'])
        print(rank[i][1]['url'])
        print()



#Compare Articles 






