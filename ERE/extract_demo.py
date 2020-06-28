import os
import re

import sys
sys.path.append("..")
from core.nlp import NLP
from core.extractor import Extractor

if __name__ == '__main__':
    input_path = '../../data/dev.txt'  # input path
    output_path = '../../data/knowledge_triple.json'  # output path of json file 
    output_path2 = '../../data/triple_result.txt'  # output path of triple txt file 
    if os.path.isfile(output_path):
        os.remove(output_path)
    # os.mkdir(output_path)

    print('Start extracting...')

    nlp = NLP()
    num = 1  # Number of triples


    with open(input_path, 'r', encoding='utf-8') as f_in:
        # divide sentences
        origin_sentences = re.split('[。？！；]|\n', f_in.read())
    
        for origin_sentence in origin_sentences:
            # delete sentences less than 6 in length
            if (len(origin_sentence) < 6):
                continue
            #print('*****')
            # print(origin_sentence)
            # segment
            lemmas = nlp.segment(origin_sentence)
            #  POS Tagging
            words_postag = nlp.postag(lemmas)
            # Named Entity Recognition
            words_netag = nlp.netag(words_postag)
            # dependency parsing
            sentence = nlp.parse(words_netag)
            #sprint(sentence.to_string())
			
			#start extract entity and relation
            extractor = Extractor()
            num = extractor.extract(origin_sentence, sentence, output_path,output_path2, num)
