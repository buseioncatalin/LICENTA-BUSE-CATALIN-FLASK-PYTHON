# import vaderSentiment
from textblob import TextBlob
import json

# #########################
# #### LOAD JSON FILE #####
with open('data.json') as f:
    JSON_FILE = json.load(f)
# #########################


# #########################
def analiza():
    y = input("Add text:\n")
    edu = TextBlob(y)
    x = edu.sentiment.polarity
    if x < 0:
        print(x, "Negative")
    elif x == 0:
        print(x, "Neutral")
    else:
        print(x, "Positive")
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
    name_query = get_movie_name()

    movie_name_list = create_list_of_names()
    results = []
    for i in movie_name_list:
        if name_query in i.lower():
            results.append(i)

    if len(results) == 0:
        print("No movies in database contained that keyword.")
    elif len(results) == 1:
        print("The movie found was: " + results[0])
    else:
        print("We found multiple movies with similar names. Please check and write again the exact name.")
        print("Movies found: ")
        for i in results:
            print(i)


# for i in list:
#     lista_review = i["reviews"]
#     print("Numele este " + i["movie_name"] + ", iar review-urile sunt " + lista_review)

def app_running():
    pass


# create_list_of_names()

search_for_movie()
