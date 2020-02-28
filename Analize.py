#!/usr/bin/python3
from textblob import TextBlob
import pandas as pd
import io
import matplotlib.pyplot as plt
import sys
import re
import urllib.request, urllib.error, urllib.parse
import requests as req
from bs4 import BeautifulSoup

n = 1

print ("You are currently running %s" % (sys.argv[1]))
print ("You are currently running %s" % (sys.argv[2]))


if len(sys.argv) < 2:
    print("You should supply the name of a textfile with urls ")
    sys.exit()
else:
    #GET WEBPAGES SO I DONT HAVE TO.by 11:59pm
    n = 1
while(true)(
    resp1 = req.get(sys.argv[n], verify=False)
    #resp2 = req.get(sys.argv[2], verify=False)

    #PARSES THE HTML FILE
    soup = BeautifulSoup(resp1.text,features="html.parser")
    #soup2 = BeautifulSoup(resp2.text, features="html.parser")


    #Webpage1 = soup1.get_text(' ', strip=True)
    #Webpage2 = soup2.get_text(' ', strip=True)


    #FIND ALL P TAGS
    p_one = [p.text for p in soup.findAll('p')]
    #p_two = [p.text for p in soup2.findAll('p')]

    #FIND ALL TITLE TAGS
    t_one = soup1.findAll()
    #CONVERT TO STRING
    txt1_string = ' '.join(p_one)
    #txt2_string = ' '.join(p_two)


    txt1 = txt1_string.replace('. ','\n')
    #txt2 = txt2_string.replace('. ','\n')
    df['subjectivity'] = df['text'].apply(get_subjectivity)
    text = txt1.splitlines() + txt2.splitlines()

    #ADD NUMBERED LINES
    Rows = []
    i = 1
    for line in text:
        new_row = {'line':i, 'text':line.strip()}
        Rows.append(new_row)
        i+=1

    #CREATE DATAFRAME
    df = pd.DataFrame(Rows, columns=['line','text','subjectivity','source'])
    def get_subjectivity(text):
        try:
            return TextBlob(text).sentiment.subjectivity
        except Exception:
            print("An exception occurred.")
            return 'n/a'

    #APPLY get_subjectivity
    df['subjectivity'] = df['text'].apply(get_subjectivity)

    df['source'] = sys.argv[n]

    #CREATE CSV
    csvname = "Yeet.csv"
    df.to_csv(csvname, encoding='utf-8', index=False)
    n + 1)

    #BAR GRAPH TIME BABY
    df = df.groupby("source").sum()
    df.plot.bar()
    plt.show()
