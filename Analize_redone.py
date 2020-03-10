#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
import pandas as pd
import requests as req
from urllib.parse import urlsplit
from bs4 import BeautifulSoup
from textblob import TextBlob

#Creating subjectivity method :: Written by Don Davis
def get_subjectivity(text):
        try:
            return TextBlob(text).sentiment.subjectivity
        except Exception:
            print("An exception occurred.")
            return 'n/a'

#Asking the user how many webpages they want to scrape
HM = int(input("How many webpages do you want to scrape? : "))
#Creating rotation variable
nor = 1
#A little magic. I did this so that you didnt have to add one to the inputed number.
HM = HM + 1

#Create DataFrame number 1. This will be the collective DataFrame.
rows = []
df = pd.DataFrame(rows, columns=['line','text','subjectivity','source'])

while nor != HM:
    print("Getting subjectivity for " + sys.argv[nor])
    parsed = urlsplit(sys.argv[nor])

    #GET WEBPAGES SO I DONT HAVE TO
    resp = req.get(sys.argv[nor], verify=False)

    #PARSES THE HTML FILE
    soup = BeautifulSoup(resp.text, "html.parser")

    #FIND ALL P TAGS
    p = [p.text for p in soup.findAll('p')]

    #CONVERT TO STRING
    txt_string = ' '.join(p)

    txt = txt_string.replace('. ','\n')

    text = txt.splitlines()

    #ADD NUMBERED LINES
    print('Adding numbered lines')

    i = 1
    Rows = []
    for line in text:
        new_row = {'line':i, 'text':line.strip()}
        Rows.append(new_row)
        i+=1

    df1 = pd.DataFrame(Rows, columns=['line','text','subjectivity','source'])

    #APPLY get_subjectivity
    df1['subjectivity'] = df1['text'].apply(get_subjectivity)
    df1['source'] = parsed.hostname
    df = df.append(df1, ignore_index=True, sort=False)
    nor = nor + 1
    if nor == HM:
        #BAR GRAPH TIME BABY
        title = input("What is the title of the graph?: ")
        fig, ax = plt.subplots()
        df.groupby('source')['subjectivity'].sum().plot(kind='bar',title=title)
        plt.subplots_adjust(bottom=0.51)
        plt.savefig(title +".png")
        break
    if nor != HM:
        continue
