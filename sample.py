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
import pickle


app = Flask(__name__) 


maxlen_questions=22
maxlen_answers=74
questions=[]
answers=[]
with open(r"C:\Users\nupur\Desktop\bot\questions.txt", "rb") as fp:
  questions=pickle.load(fp)
with open(r"C:\Users\nupur\Desktop\bot\ans.txt", "rb") as fp:
  answers=pickle.load(fp)
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts( questions + answers )
VOCAB_SIZE = len( tokenizer.word_index )+1
print( 'VOCAB SIZE : {}'.format( VOCAB_SIZE ))

def str_to_tokens(sentence:str):
    sentence=re.sub(r'[^\w\s]', '',sentence) 
    words = sentence.lower().split()
    tokens_list = list()
    for word in words:
        tokens_list.append( tokenizer.word_index[ word ] ) 
    return preprocessing.sequence.pad_sequences( [tokens_list] , maxlen=maxlen_questions , padding='post')

def load_model(model_filename, model_weights_filename):
    with open(model_filename, 'r', encoding='utf8') as f:
        model = tf.keras.models.model_from_json(f.read())
    model.load_weights(model_weights_filename)
    return model
encoder = load_model(r'C:\Users\nupur\Desktop\bot\encoder_model\encoder_model2.json', r'C:\Users\nupur\Desktop\bot\encoder_model\encoder_model_weights2.h5')
decoder = load_model(r'C:\Users\nupur\Desktop\bot\decoder_model\decoder_model2.json', r'C:\Users\nupur\Desktop\bot\decoder_model\decoder_model_weights2.h5')

@app.route("/")
def index():
     return render_template("index.html") #to send context to html

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg")
     print('Usertext: ',userText)
     userText=str(userText)
     enc_model = encoder
     
     dec_model=decoder
     for _ in range(10):
          states_values = enc_model.predict( str_to_tokens( userText))
          empty_target_seq = np.zeros( ( 1 , 1 ) )
          empty_target_seq[0, 0] = tokenizer.word_index['start']
          stop_condition = False
          decoded_translation = ''
   
          while not stop_condition :
               dec_outputs , h , c = dec_model.predict([ empty_target_seq ] + states_values )
               sampled_word_index = np.argmax( dec_outputs[0, -1, :] )
               sampled_word = None
               for word , index in tokenizer.word_index.items() :
                    if sampled_word_index == index :
                         decoded_translation += ' {}'.format( word )
                         sampled_word = word
               if sampled_word == 'end' or len(decoded_translation.split()) > maxlen_answers:
                         stop_condition = True
               empty_target_seq = np.zeros( ( 1 , 1 ) )  
               empty_target_seq[ 0 , 0 ] = sampled_word_index
               states_values = [ h , c ] 
          if ('https' in decoded_translation):
               decoded_translation=decoded_translation.split('https')
               s1=decoded_translation[1].split(' ')
               s1.remove('')
               for i in range(len(s1)-2):
                  s1[i]=s1[i].replace(s1[i],s1[i]+'.')
               s1.remove('end')
               s2='https://'+('').join(s1)
               return(decoded_translation[0]+s2+'.')
          else:
               return(decoded_translation[:-3]+'.' )

          

          

if __name__ == "__main__":
     app.run(debug = True)


