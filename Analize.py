#!/usr/bin/python3
from textblob import TextBlob
import pandas as pd
import io
import matplotlib.pyplot as plt
import sys
import re
import requests as req
from bs4 import BeautifulSoup
from urllib.parse import urlsplit

if len(sys.argv) < 1:
    print("You should supply the name of a textfile with urls ")
    sys.exit()
else:
    print("Creating get_subjectivity method")
def get_subjectivity(text):
        try:
            return TextBlob(text).sentiment.subjectivity
        except Exception:
            print("An exception occurred.")
            return 'n/a'

print('Getting webpage 1')
parsed = urlsplit(sys.argv[1])

#GET WEBPAGES SO I DONT HAVE TO
resp1 = req.get(sys.argv[1], verify=False)

#PARSES THE HTML FILE
soup1 = BeautifulSoup(resp1.text, "html.parser")

#FIND ALL P TAGS
p_one = [p.text for p in soup1.findAll('p')]

#CONVERT TO STRING
txt1_string = ' '.join(p_one)

txt1 = txt1_string.replace('. ','\n')

text = txt1.splitlines()

#ADD NUMBERED LINES
print('Adding numbered lines')

i = 1
Rows = []
for line in text:
    new_row = {'line':i, 'text':line.strip()}
    Rows.append(new_row)
    i+=1
print('Creating the DataFrame')
df = pd.DataFrame(Rows, columns=['line','text','subjectivity','source'])

#APPLY get_subjectivity
df['subjectivity'] = df['text'].apply(get_subjectivity)
df['source'] = parsed.hostname


print('Getting webpage 2')
parsed = urlsplit(sys.argv[2])

#GET WEBPAGES SO I DONT HAVE TO
resp2 = req.get(sys.argv[2], verify=False)

#PARSES THE HTML FILE
soup2 = BeautifulSoup(resp2.text, "html.parser")

#FIND ALL P TAGS
p_two = [p.text for p in soup2.findAll('p')]

#CONVERT TO STRING
txt2_string = ' '.join(p_two)

txt2 = txt2_string.replace('. ','\n')

text2 = txt2.splitlines()

#ADD NUMBERED LINES
print('Adding numbered lines')
Rows = []
for line in text2:
    new_row = {'line':i, 'text':line.strip()}
    Rows.append(new_row)
    i+=1

print('Creating the DataFrame')
df2 = pd.DataFrame(Rows, columns=['line','text','subjectivity','source'])

#APPLY get_subjectivity
df2['subjectivity'] = df2['text'].apply(get_subjectivity)
df2['source'] = parsed.hostname
df = df.append(df2, ignore_index=True, sort=False)

print('Getting webpage 3')
parsed = urlsplit(sys.argv[3])

#GET WEBPAGES SO I DONT HAVE TO
resp3 = req.get(sys.argv[3], verify=False)

#PARSES THE HTML FILE
soup3 = BeautifulSoup(resp1.text, "html.parser")

#FIND ALL P TAGS
p_3 = [p.text for p in soup3.findAll('p')]

#CONVERT TO STRING
txt3_string = ' '.join(p_3)

txt3 = txt3_string.replace('. ','\n')

text3 = txt3.splitlines()

#ADD NUMBERED LINES
print('Adding numbered lines')
Rows = []
for line in text3:
    new_row = {'line':i, 'text':line.strip()}
    Rows.append(new_row)
    i+=1

print('Creating the DataFrame')
df3 = pd.DataFrame(Rows, columns=['line','text','subjectivity','source'])

#APPLY get_subjectivity
df3['subjectivity'] = df3['text'].apply(get_subjectivity)
df3['source'] = parsed.hostname
df = df.append(df3, ignore_index=True, sort=False)

print('Getting webpage 4')
parsed = urlsplit(sys.argv[4])

#GET WEBPAGES SO I DONT HAVE TO
resp1 = req.get(sys.argv[4], verify=False)

#PARSES THE HTML FILE
soup4 = BeautifulSoup(resp1.text, "html.parser")

#FIND ALL P TAGS
p_4 = [p.text for p in soup4.findAll('p')]

#CONVERT TO STRING
txt4_string = ' '.join(p_4)

txt4 = txt4_string.replace('. ','\n')

text4 = txt4.splitlines()

#ADD NUMBERED LINES
print('Adding numbered lines')
Rows = []
for line in text4:
    new_row = {'line':i, 'text':line.strip()}
    Rows.append(new_row)
    i+=1

print('Creating the DataFrame')
df4 = pd.DataFrame(Rows, columns=['line','text','subjectivity','source'])

#APPLY get_subjectivity
df4['subjectivity'] = df3['text'].apply(get_subjectivity)
df4['source'] = parsed.hostname
df = df.append(df4, ignore_index=True, sort=False)

print('Getting webpage 5')
parsed = urlsplit(sys.argv[5])

#GET WEBPAGES SO I DONT HAVE TO
resp1 = req.get(sys.argv[5], verify=False)

#PARSES THE HTML FILE
soup5 = BeautifulSoup(resp1.text, "html.parser")

#FIND ALL P TAGS
p_5 = [p.text for p in soup5.findAll('p')]

#CONVERT TO STRING
txt5_string = ' '.join(p_5)

txt5 = txt5_string.replace('. ','\n')

text5 = txt5.splitlines()

#ADD NUMBERED LINES
print('Adding numbered lines')
Rows = []
for line in text5:
    new_row = {'line':i, 'text':line.strip()}
    Rows.append(new_row)
    i+=1

print('Creating the DataFrame')
df5 = pd.DataFrame(Rows, columns=['line','text','subjectivity','source'])

#APPLY get_subjectivity
df5['subjectivity'] = df3['text'].apply(get_subjectivity)
df5['source'] = parsed.hostname
df = df.append(df5, ignore_index=True, sort=False)

#CREATE CSV
csvname = "Yeet.csv"
df.to_csv(csvname,encoding='utf-8', index=False)

#BAR GRAPH TIME BABY
title = input("What is the title of the graph?: ")
fig, ax = plt.subplots()
df.groupby('source')['subjectivity'].sum().plot(kind='bar',title=title)
plt.show()
