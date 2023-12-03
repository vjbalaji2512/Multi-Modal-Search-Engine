
from rank_bm25 import BM25Okapi
import pickle
from flask import Flask,request, jsonify

app = Flask(__name__)
class Results:
    def __init__(self, obj):
        self.bm25 = obj
        
def getDocs():
    return
    
def getAudio():
    return

@app.route('/result')
def getQueryList():

    corpusText = {}
    corpusImg = {}
    corpusAud = {}
    with open('corpusText.pkl', 'rb') as f:
        corpusText = pickle.load(f)

    with open('corpusImg.pkl', 'rb') as f:
        corpusImg = pickle.load(f)
    text_mapping = image_mapping = audio_mapping = {}
    with open('meta.pkl', 'rb') as f:
        text_mapping, image_mapping, audio_mapping = pickle.load(f)

    """
    Ref : How the pickled data would look like
    text_mapping = {1:{"title":"MS Dhoni - Wikipedia", "url":"https://en.wikipedia.org/wiki/MS_Dhoni", "brief":"Mahendra Singh Dhoni (born 7 July 1981), is a former international cricketer who captained the Indian national team in limited-overs formats from 2007 to ..."}
                    , 2:{"title" : "Virat Kohli - Wikipedia", "url":"https://en.wikipedia.org/wiki/Virat_Kohli", "brief":"born 5 November 1988) is an Indian cricketer and the captain of India national cricket team in ODIs and Tests. ... He plays for Delhi in domestic cricket ..."}
                    , 3:{"title" : "MS Dhoni profile and biography, stats, records ... - ESPNcricinfo", "url" : "https://www.espncricinfo.com/player/ms-dhoni-28081", "brief":"Barring Sachin Tendulkar and Virat Kohli, MS Dhoni is probably the most popular and definitely the most scrutinised cricketer from India."},
                    4:{"title" : "M.S. Dhoni | Biography, Facts, & Awards | Britannica", "url": "https://www.britannica.com/biography/Mahendra-Dhoni", "brief" : "M.S. Dhoni, in full Mahendra Singh Dhoni, (born July 7, 1981, Ranchi, Bihar [now Jharkhand] state, India), Indian cricketer whose rise to prominence in the"},
                    5:{"title" : "Who is MS Dhoni - Profile, News, Career, Stats, ICC Ranking ...", "url" : "https://www.business-standard.com/about/who-is-ms-dhoni", "brief" : "Who is MS Dhoni - Check out MS Dhoni cricket career here at Business Standard. Find information about his age, batting bowling stats, MS Dhoni photos, runs, ..."},
                    6:{"title" : "Chennai Super Kings Share Epic Throwback Pic Of MS Dhoni ...", "url" : "https://sports.ndtv.com/ipl-2022/chennai-super-kings-share-epic-throwback-pic-of-ms-dhoni-from-his-test-debut-16-years-ago-2634655", "brief" : "hennai Super Kings Share Epic Throwback Pic Of MS Dhoni From His Test Debut 16 Years Ago. Dhoni retired from Test cricket December 2014."},
                    7:{"title" : "MS Dhoni - Sportzwiki", "url" : "https://sportzwiki.com/wiki/ms-dhoni", "brief" : "Explore MS Dhoni Profile on SportzWiki. Follow Former Indian team Captain for latest news, Biography, Records, Career Info & his ICC Ranking,"},
                    8:{"title" : "'Absolute joke': Cricket world rages over Virat Kohli 'disgrace'", "url" : "https://au.sports.yahoo.com/cricket-2021-uproar-virat-kohli-dismissal-disgrace-210757489.html", "brief" : "irat Kohli's controversial dismissal. The India captain appeared to be dudded against New Zealand. Source: BCCI."},
                    9:{"title" : "Virat Kohli profile and biography, stats, records, averages ...", "url" : "https://www.espncricinfo.com/player/virat-kohli-253802", "brief" : "India has given to the world many a great cricketer but perhaps none as ambitious as Virat Kohli. To meet his ambition, Kohli employed the technical ..."},
                    10:{"title" : "Virat Kohli Profile - ICC Ranking, Age, Career Info & Stats", "url" : "https://www.cricbuzz.com/profiles/1413/virat-kohli", "brief" : "Looking for Virat Kohli's career stats? Get all the information of his performance in ODI, T20, IPL & personal info about Age, height & latest ICC Rankings."}}
    image_mapping = {1:{"title":"Dhoni wicket keeping", "path" : "./images/1.jpg"}, 2: {"title" : "Dhoni on the cover", "path" : "./images/2.jpg"},
                     3 : {"title" : "Dhoni - the untold story", "path" : "./images/3.jpg"}, 4 : {"title" : "Dhoni and Kohli", "path" : "./images/4.jpg"},
                     5 : {"title" : "Dhoni and Jadeja in CSK jersey", "path" : "./images/5.jpg", 6 : {"title" : "Dhoni - the untold story", "path" : "./images/6.jpg"}}
    """
    
                    
    audio_mapping= {}
    tokenized_corpus_text = [doc.split(" ") for doc in corpusText.keys()]

    tokenized_corpus_audio = [doc.split(" ") for doc in corpusAud.keys()]

    tokenized_corpus_image = [doc.split(" ") for doc in corpusImg.keys()]
    
    bm25 = None
    with open('bm25text.pkl', 'rb') as f:
        bm25 = pickle.load(f)
        
    query = request.args.get('q')
    tokenized_query = query.split(" ")


    tempText = bm25.get_top_n(tokenized_query, list(corpusText.keys()), n=3)

    print(corpusImg.keys())
    with open('bm25img.pkl', 'rb') as f:
        bm25 = pickle.load(f)
    #tempAud = bm25.get_top_n(tokenized_query, list(corpusImg.keys()), n=3)
    tempImg = bm25.get_top_n(tokenized_query, list(corpusImg.keys()), n=3)
    
    return_obj = {"text":[], "audio":[], "image":[]}
    for i in range(len(tempText)):
        print(corpusText[tempText[i]])
        return_obj["text"].append(text_mapping[corpusText[tempText[i]]])
        #return_obj["audio"].append(audio_mapping[corpusText[tempAud[i]]])
        return_obj["image"].append(image_mapping[corpusImg[tempImg[i]]])

    return(jsonify(return_obj))
    #return(return_obj)
    

app.run(host='0.0.0.0', port=5000)
