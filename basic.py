import re
import os
import pandas as pd 
from nltk.corpus import stopwords

data = pd.read_csv('final_data.csv')

def clean_text(df):
    '''
    Clean the body and title cols in the dataframe to get rid of:
    1. Stopwords
    2. Special Symbols - not inclusive of numbers
    3. Convert to lower case
    '''

    REPLACE_BY_SPACE = re.compile('[/()\{\}\[\][\|@,;*\#\+\?\=\-\:\.\"\&]')
    STOPWORDS =re.compile(r'\b(' + r'|'.join(stopwords.words('english')) + r')\b')

    df['body']=df['body'].str.lower()
    df['title']=df['title'].str.lower()
    df['body']=df['body'].str.replace('x200b', '')
    df['body']=df['body'].str.replace('\"', '')
    df['body']=df['body'].str.replace("\'", '')
    df['body']=df['body'].str.replace("\n", '')
    df['body']=df['body'].str.replace("!", '')
    df['body']=df['body'].str.replace(REPLACE_BY_SPACE, '')
    df['body']=df['body'].str.replace(STOPWORDS, '')
    
    df['title']=df['title'].str.replace('\"', '')
    df['title']=df['title'].str.replace("\'", '')
    df['title']=df['title'].str.replace("!", '')
    df['title']=df['title'].str.replace("\n", '')
    df['title']=df['title'].str.replace(STOPWORDS, '')
    df['title']=df['title'].str.replace(REPLACE_BY_SPACE, '')
    df['title']=df['title'].str.replace('x200b', ' ')
    

    return df

final_data = clean_text(data)

final_data.to_csv('data_processed.csv')
 





