import numpy as np
from bert_serving.client import BertClient



def compare_sentance_to_article(text, article):

    article_list = article.split('.')

    with BertClient(port=4000, port_out=4001) as bc:
        doc_vecs = bc.encode(questions)