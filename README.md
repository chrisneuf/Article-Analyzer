# Article-Analyzer

## Main Idea

- Article Analyzer is a service/website where a user can submit
 the url of a news article and receive comparisons to similar news 
 articles 

#### Other Ideas
- perform text analysis on the article to determine a score related to lingustics used in fake news articles
- compare fake news lingusitcs score to related articles 

## Run

`python3 article_analyzer.py url`


## Todo

- [ ] **Submit an article and find similar articles**
    1. [x] Devlop method for finding similar articles
        - [ ] Remove certian words in query that influence results eg (numbers,   names?)
    2. [ ] Refactor query for broader search
        - [x] remove stop words
        - [ ] find key words
- [ ] **Compare the most similar articles by similar sentances**

