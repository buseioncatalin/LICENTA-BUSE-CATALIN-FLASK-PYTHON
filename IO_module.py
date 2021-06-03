# import vaderSentiment
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

# ####      GLOBALS   #####
okay = None
# #########################

# #### LOAD JSON FILE #####
with open('data.json') as f:
    JSON_FILE = json.load(f)
# #########################


# #########################
def analysis_textblob(text):
    y = text
    edu = TextBlob(y)
    x = edu.sentiment.polarity
    return x

# ##########################
def rank_textblob_score(textblob_score):
    if textblob_score < 0:
        polarity = "Negative"
    elif textblob_score == 0:
        polarity = "Neutral"
    else:
        polarity = "Positive"
    return polarity
# ##########################
# ##########################


# ##########################
def analysis_vadersentiment():
    pass
# ##########################


def create_list_of_names():
    data = JSON_FILE
    movie_name_list = []
    temp = data["Movies"]
    for i in temp:
        movie_name_list.append(i["movie_name"])
    return movie_name_list


def get_movie_name():
    name = input("Please input the name of the movie you want to search for: ")
    name = name.lower()
    return name


def search_for_movie():
    global okay
    name_query = get_movie_name()

    movie_name_list = create_list_of_names()
    results = []
    for i in movie_name_list:
        if name_query in i.lower():
            results.append(i)

    if len(results) == 0:
        okay = False
        print("No movies in database contained that keyword. \n")
    elif len(results) == 1:
        okay = True
        print("The movie found was: " + results[0] + "\n")
        return results[0]
    else:
        okay = False
        print("We found multiple movies with similar names. Please check and write again the exact name.")
        print("Movies found: ")
        for i in results:
            print(i)
        print("\n")


# for i in list:
#     lista_review = i["reviews"]
#     print("Numele este " + i["movie_name"] + ", iar review-urile sunt " + lista_review)

def get_movie_reviews_list(name):
    for i in JSON_FILE["Movies"]:
        if i["movie_name"] == name:
            return i["reviews"]

def app_running():
    print("Welcome. \n")
    reviews = []
    while(1):
        actual_movie_name = search_for_movie()
        if okay == True:
            break
        else:
            print("Please write again. \n")

    reviews = get_movie_reviews_list(actual_movie_name)

    for i in reviews:
        print(str(rank_textblob_score(analysis_textblob(i))))



# create_list_of_names()

app_running()
