
from aylienapiclient import textapi
import aylienapiclient
from googlesearch import search
from nltk.corpus import stopwords
import sys
import tldextract
import config
import exclusions
import article_comparer as ac


#Setup API Keys
extraction_api = textapi.Client("a65d9a56", config.aylien_api_key)

def main():
        
        url = firstarg=sys.argv[1]
        root = get_root(url)
        article = extraction_api.Extract({'url': url})
        title = article['title']
        print(article)
        data = article['article'].split('.')
        query = remove_stop_words(title)

        print("\nFinding related articles for:\n")
        print(f"Title: {article['title']}")
        print(f"Source: {url}")
        print(f"Search query: {query}\n")
        # Find Related articles
        related_articles = get_related_articles(query, root, 5)
        
        print("Related articles:\n")
        for article in related_articles:
                print(f"Title: {article['title']}")
                print(f"Source: {article['url']}\n")
              
        ac.compare_sentance_to_article(data[5], related_articles[0]['article'],5)


# Returns the root of url
def get_root(url):
      ext = tldextract.extract(url)
      return ext[1]

# Returns a list of  articles related to title less than max size
# Exludes articles with the same domain name
def get_related_articles(title, root, max):

        related_articles = []
        for url in search(title, stop=max):
                url_root = get_root(url)
                if root != url_root and url_root not in exclusions.domain_list :
                        try:
                                article = extraction_api.Extract({'url': url})
                                article['url'] = url
                                related_articles.append(article)
                        except aylienapiclient.errors.HttpError:
                                print(f"Timed out on {url}\n")


                                
        return related_articles

# Remove stop words from text
# TODO: might have to edit stop word data for better results
def remove_stop_words(text):
        text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])
        return text

#Compares 2 articles to find similarites and differences
def compare_articles(article1, article2):
        x = "void"

if __name__ == "__main__":
        main() 







