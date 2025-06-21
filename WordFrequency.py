import pandas as pd

default_path=r'C:\Users\Stephen_Gonzales1\Documents\AdvPython\IntrotoVSCode'

with open(default_path+r'\sometext-1.txt','r') as file:
    text=file.read()

words=text.split()
some_text_data=pd.DataFrame(words,columns=['text'])

some_text_data['text']=some_text_data['text'].str.replace(r'[,.\-0-9]','',regex=True)

some_text_data=some_text_data[some_text_data['text']!='']

some_text_data['text']=some_text_data['text'].str.lower()

print(some_text_data['text'])

word_dictionary=some_text_data['text'].value_counts().to_dict()

print(word_dictionary)