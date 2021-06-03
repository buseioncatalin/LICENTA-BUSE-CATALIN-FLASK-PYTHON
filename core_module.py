from textblob import TextBlob
import json

# ####      GLOBALS   #####
okay = None
return_to_flask = ""
# #########################

# #### LOAD JSON FILE #####
with open('data.json') as f:
    JSON_FILE = json.load(f)
# #########################

# ANALYSING THE GIVEN TEXT WITH TEXTBLOB


def analysis_textblob(text_to_analyse):
    result = TextBlob(text_to_analyse)
    result_polarity = result.polarity
    return result_polarity
# #########################

# ANALYSING THE TEXTBLOB RESULT


def rank_textblob_score(textblob_score):
    if textblob_score < 0:
        polarity = "Negative"
    elif textblob_score == 0:
        polarity = "Neutral"
    else:
        polarity = "Positive"
    return polarity
# #########################


# ANALYSING THE GIVEN TEXT WITH VADERSENTIMENT


def analysis_vadersentiment(text_to_analyse):
    pass
# #########################


# ANALYSING THE VADERSENTIMENT RESULT


def rank_vader_score(vader_score):
    pass
# #########################


# CREATING A LIST OF ALL MOVIE NAMES


def create_list_of_names():
    data = JSON_FILE
    movie_name_list = []
    temp = data["Movies"]
    for i in temp:
        movie_name_list.append(i["movie_name"])
    return movie_name_list
# #########################


# GETTING THE REVIEWS LIST FOR A SPECIFIC MOVIE


def get_movie_reviews_list(name):
    for i in JSON_FILE["Movies"]:
        if i["movie_name"] == name:
            return i["reviews"]
# #########################


# CHECKING LIST FOR MOVIE NAMES CONTAINING KEYWORD


def search_for_movie(movie_keyword):
    global okay

    movie_name_list = create_list_of_names()
    results = []
    for i in movie_name_list:
        if movie_keyword in i.lower():
            results.append(i)

    return results
# #########################


# CHECK THE LIST OF MOVIE NAMES CONTAINING THE INPUT KEYWORD


def check_similarities(results):
    global okay
    if len(results) == 0:
        okay = "None"
        print("No movies in database contained that keyword. \n")
        return okay
    elif len(results) == 1:
        okay = "One"
        print("The movie found was: " + results[0] + "\n")
        return results[0]
    else:
        okay = "Multiple"
        print("We found multiple movies with similar names. Please check and write again the exact name.")
        print("Movies found: ")
        for i in results:
            print(i)
        print("\n")
        return results
# #########################


# RUNS WHEN SEARCH BUTTON IS CLICKED


def run_on_search(user_input):
    print("Welcome. \n")

    global return_to_flask

    movie_list = search_for_movie(user_input)
    search_result = check_similarities(movie_list)

    if okay == "None":
        return_to_flask = "No movie names contained this keyword. Try again.\n"

    elif okay == "One":
        return_to_flask = ""
        actual_movie_name = search_result

        reviews = get_movie_reviews_list(actual_movie_name)

        for i in reviews:
            to_add = str(rank_textblob_score(analysis_textblob(i)))
            return_to_flask = return_to_flask + to_add + "<br>"

    elif okay == "Multiple":
        return_to_flask = "We found multiple movies with similar names. Please check and write again the exact name. <br>"
        list_of_names = search_result
        for i in list_of_names:
            return_to_flask = return_to_flask + i + "<br>"

    return return_to_flask
# #########################
