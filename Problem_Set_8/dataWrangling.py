#Worked with Aaron Roberts
import pandas as pd
import numpy as np

df = pd.read_csv('./dd-comment-profile.csv')

chars = ('$', '%', '*', '<div>', '</div>', 'FREE', 'app', 'check out my page',
'<', '>', '@', '=', '#', '&', '!', '.com')

comments = []

for text in df['comment_msg']:
    clean_text = str(text)
    for char in chars:
        if char in clean_text:
            clean_text = ''

    comments.append(clean_text)

df['comment_msg'] = comments

df['comment_msg'].replace('', np.nan,inplace=True)
df['comment_msg'].replace('nan',np.nan,inplace=True)

df.dropna(subset=['comment_msg'], inplace=True)

df.to_csv('output.csv')
