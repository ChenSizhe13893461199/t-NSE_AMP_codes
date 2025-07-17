# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 16:53:33 2025

@author: 24226
"""

from gensim.models import KeyedVectors
import csv
import numpy as np
import keras.utils.np_utils as kutils

wv = KeyedVectors.load_word2vec_format('word2vec11.bin', binary=True)


def getMatrixLabelnlp(positive_position_file_name, window_size=51, empty_aa = '*'):
    # input format   label, proteinName, postion, shortsequence
    # label存储0/1值
    #positive_position_file_name='trainingAMP.csv'
    #window_size=50
    prot = []  #
    pos = []  #
    rawseq = [] #
    all_label = [] #
    all_labela = []
    length=[]
    short_seqs = []
    #half_len = (window_size - 1) / 2

    with open(positive_position_file_name, 'r') as rf:
        reader = csv.reader(rf)
        for row in reader:

                #position = int(row[2])
                a=window_size-len(row[1])
                sseq = row[1]#+a*' '
                rawseq.append(sseq)
                b=len(row[1])
                length.append(b)
                #center = sseq[position - 1]
            # 
                all_label.append(int(row[0]))
                #all_labela.append(int(row[2])) 
                #prot.append(row[1])
                #pos.append(row[2])

        
        # Keras的utilities，用于“Converts a class vector (integers) to binary class matrix.”
        # “A binary matrix representation of the input”
        targetY = kutils.to_categorical(all_label)
        #targetYa = kutils.to_categorical(all_labela)

        ONE_HOT_SIZE = 20
        # _aminos = 'ACDEFGHIKLMNPQRSTVWY*'
        letterDict = {}
        letterDict["A"] = 0;
        letterDict["C"] = 1;
        letterDict["D"] = 2;
        letterDict["E"] = 3;
        letterDict["F"] = 4;
        letterDict["G"] = 5;
        letterDict["H"] = 6;
        letterDict["I"] = 7;
        letterDict["K"] = 8;
        letterDict["L"] = 9;
        letterDict["M"] = 10;
        letterDict["N"] = 11;
        letterDict["P"] = 12;
        letterDict["Q"] = 13;
        letterDict["R"] = 14;
        letterDict["S"] = 15;
        letterDict["T"] = 16;
        letterDict["V"] = 17;
        letterDict["W"] = 18;
        letterDict["Y"] = 19;

    return rawseq,length

train_file_name = 'your file.csv'
win1 = 50

nlp, lengthnlp = getMatrixLabelnlp(train_file_name, win1)




#for example, the Word2Vec for amino acid A is calculated by the following codes
a=wv["A"]

#By using the codes, you can represent the Word2Vec of any given sequences








