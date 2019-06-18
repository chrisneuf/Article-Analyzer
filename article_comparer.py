import numpy as np
from bert_serving.client import BertClient
from termcolor import colored


def compare_sentance_to_article(text, article, topk):
        
        article_list = article.split('.')
        article_list = [sentance.strip() for sentance in article_list]
        text = text.strip()    
        with BertClient(port=5556, port_out=5555) as bc:
                doc_vecs = bc.encode(article_list)

                query_vec = bc.encode(text)
                score = np.sum(query_vec * doc_vecs, axis=1) / np.linalg.norm(doc_vecs, axis=1)
                topk_idx = np.argsort(score)[::-1][:topk]
                print(f"top{topk} sentances  similar to '{text}'" )
                for idx in topk_idx:
                        print('> %s\t%s' % (colored('%.1f' % score[idx], 'cyan'), colored(article_list[idx], 'yellow')))