# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:54:07 2020
@author: devWangBin

get the result of json file of ERE model

"""
import json

def main():
    f = open("./triple_result.txt",'w',encoding='utf-8')
    
    output_path = './knowledge_triple.json'  #path of Json file
    
    triples = {}

    with open(output_path, 'r') as f:

        triples = json.load(f)    #triples is a dictionary object

    print(triples)
    f.write(triples)
    f.close()


if __name__ == "__main__":
    main()
