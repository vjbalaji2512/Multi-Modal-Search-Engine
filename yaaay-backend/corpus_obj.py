from urllib.request import urlopen
from urllib import request
import nltk, re, pprint
from bs4 import BeautifulSoup
import pickle
"""
quote_page = 'http://https://en.wikipedia.org/wiki/MS_Dhoni'

page = urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

print(soup)
"""

from bs4 import BeautifulSoup
import requests
import nltk
def fun(url):
  response = requests.get(url).content
  soup = BeautifulSoup(response, "html.parser")
  text_tokens = nltk.tokenize.word_tokenize(soup.get_text())

  #print(text_tokens)
  stop_words = set(nltk.corpus.stopwords.words('english'))
  filtered_sentence = []
   
  for w in text_tokens:
      if w not in stop_words:
          filtered_sentence.append(w)

  return(filtered_sentence)

urls = ['https://en.wikipedia.org/wiki/MS_Dhoni', 'https://en.wikipedia.org/wiki/Virat_Kohli',
        'https://www.espncricinfo.com/player/ms-dhoni-28081', 'https://www.britannica.com/biography/Mahendra-Dhoni',
        'https://www.business-standard.com/about/who-is-ms-dhoni',
        'https://sports.ndtv.com/ipl-2022/chennai-super-kings-share-epic-throwback-pic-of-ms-dhoni-from-his-test-debut-16-years-ago-2634655',
        'https://sportzwiki.com/wiki/ms-dhoni', 'https://au.sports.yahoo.com/cricket-2021-uproar-virat-kohli-dismissal-disgrace-210757489.html',
        'https://www.espncricinfo.com/player/virat-kohli-253802', 'https://www.cricbuzz.com/profiles/1413/virat-kohli']
with open('corpusText.pkl', 'wb') as f:
  j = 1
  t = {}
  for i in urls:
    t[' '.join(fun(i))] = j
    j += 1
  pickle.dump(t, f)

with open('corpusImg.pkl', 'wb') as f:
  t = {}
  with open("./images/meta.txt", "r") as file:
    st = file.read()
    arr = st.split('\n')

  for i in range(len(arr)):
    t[arr[i]] = i+1

  pickle.dump(t,f)



