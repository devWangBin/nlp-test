# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:22:59 2020
@author: devWangBin
processing the data for BERT-BiLSTM-CRF-NER
get the basic information of the data set
"""

data_path = "C:\\Users\\93568\\Documents\\GitHub\\BERT-CH-NER\\tmp\\"

data_list = ["dev.txt","source.txt","test1.txt"]
data_label_list = ["dev-lable.txt","target.txt","test_tgt.txt"]

def main():
    
    data_compute()
    data_process()
    
def data_process():
    
    for i in range(len(data_list)):
        
    #    print(data_list[i])
    #    print(data_label_list[i])
        
        count_lines = 0
        count_words = 0
        
        file_path1 = data_path + data_list[i]
        file_path2 = data_path + data_label_list[i]
        
        f1 = open(file_path1,"r",encoding='utf_8')
        lines = f1.readlines()
        f1.close()
        
        f2 = open(file_path2,"r",encoding='utf_8')
        label_lines = f2.readlines()
        f2.close()
        
    #    print(len(lines),len(label_lines))
    #    print(lines[0],label_lines[0])
    #    l1 = lines[0]
    #    l2 = label_lines[0]
    #    print(len(l1.split()),len(l2.split()))
    #    print(l1.split())
    #    print(l2.split())
        
        f3 = open("./data32/" + data_list[i],'w',encoding='utf-8')
        
        for l1,l2 in zip(lines,label_lines):
            
            list1 = l1.split()
            list2 = l2.split()
            
            if len(list1) != len(list2):
                print("not match error!")
            
            if len(list1) <= 32:
                count_lines += 1
                count_words += len(list1)
                for j in range(len(list1)): 
                    f3.write(list1[j]+" "+list2[j]+"\n")
            
                f3.write("\n")
        
        f3.close()
        print("***********" + data_list[i] + "**********")
        print("after processing the number lines is:",count_lines)
        print("after processing the average length of lines is:",count_words/count_lines)
        print()

def data_compute():
    #compute the basic information of the data set

    for i in range(len(data_list)):
        
        maxlen = 0
        totallen = 0
        avelen = 0 
        
        file_path1 = data_path + data_list[i]

        f1 = open(file_path1,"r",encoding='utf_8')
        lines = f1.readlines()
        f1.close()
        
        for l1 in lines:
            
            list1 = l1.split()
            
            if maxlen < len(list1):
                maxlen = len(list1)
            
            totallen += len(list1)
        
        avelen = totallen/len(lines)
        
        print("***********" + data_list[i] + "**********")
        print("the total number of the lines of the is:",len(lines))
        print("the average length of the is:",avelen)
        print("the maximum length of the is:",maxlen)
        print()
        
if __name__ == "__main__":
    main()