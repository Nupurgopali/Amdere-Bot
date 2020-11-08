from flask import Flask,render_template,request
import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras import layers , activations , models , preprocessing
from keras.layers.wrappers import TimeDistributed
from keras.layers import Activation, Dense
import nltk
from tensorflow.keras import preprocessing , utils
import os
import yaml
from keras.preprocessing.text import Tokenizer
import re

dir_path = 'C:/Users/nupur/Desktop/bot/data'
files_list = os.listdir(dir_path + os.sep)

questions =[]
answers =[]
for filepath in files_list:
    stream = open( dir_path + os.sep + filepath , 'rb')
    docs = yaml.safe_load(stream)
    conversations = docs['conversations']
    for con in conversations:
        if len( con ) > 2 :
            questions.append(con[0])
            replies = con[ 1 : ]
            ans = ''
            for rep in replies:
                ans += ' ' + rep
            answers.append( ans )
        elif len( con )> 1:
            questions.append(con[0])
            answers.append(con[1])
print(len(answers))
print(len(questions))
answers_with_tags = list()
for i in range(len(answers)):
    if type( answers[i] ) == str:
        answers_with_tags.append( answers[i] )
    else:
        questions.pop(i)

answers = list()
for i in range( len( answers_with_tags ) ) :
    answers.append( '<START> ' + answers_with_tags[i] + ' <END>' )

tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts( questions + answers )
VOCAB_SIZE = len( tokenizer.word_index )+1
print( 'VOCAB SIZE : {}'.format( VOCAB_SIZE ))