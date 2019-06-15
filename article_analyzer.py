
from aylienapiclient import textapi
from googlesearch import search
import sys
import textcleaner as tc
import tldextract


#Setup API Keys
extraction_api = textapi.Client("a65d9a56", "1946036c4ab9e433a7f87a45405f6235")





def main():
        
        url = firstarg=sys.argv[1]
        root = get_root(url)
        article = extraction_api.Extract({'url': url})
        title = article['title']

        
        print("\nUrl article title")
        print(f"{article['title']}\n")
        
        # Find Related articles
        related_articles = get_related_articles(title, root, 5)


# Returns the root of url
def get_root(url):
      ext = tldextract.extract(url)
      return ext[1]

# Returns a list of  articles related to title less than max size
def get_related_articles(title, root, max):

        related_articles = []
        for url in search(title, stop=max):
                if root != get_root(url):
                        article = extraction_api.Extract({'url': url})
                        related_articles.append(article)
                        print(article['title'])
                        print(f"{url}\n")
        return related_articles

if __name__ == "__main__":
        main() 

#Compare Articles 






