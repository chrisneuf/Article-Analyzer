# Article-Analyzer

## Main Idea

- Article Analyzer is a service/website where a user can submit
 the url of a news article and receive comparisons to similar news 
 articles 

#### Other Ideas
- perform text analysis on the article to determine a score related to lingustics used in fake news articles
- compare fake news lingusitcs score to related articles 

## Run

### Start Bert-as-a-serivce
`bert-serving-start -num_worker=1 -model_dir=uncased_L-12_H-768_A-12`

### Run algorithm 
`python3 article_analyzer.py {article url}`

## Alogrithm

### Current State

- Pass an article URL into the python script
- Extract article from website through Aylien API
- Remove stop words from article Title
- Use Title with stop words reomoved a google search qeury
- Take top results and remove results with the same domain name 


### TODO

- [ ] **Submit an article and find similar articles**
    1. [x] Devlop method for finding similar articles
        - [ ] Remove certian words in query that influence results eg (numbers,   names?)
    2. [ ] Refactor query for broader search
        - [x] remove stop words
        - [ ] find key words
- [ ] **Compare the most similar articles by similar sentances**





