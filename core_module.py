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

# #####    OBJECTS    #####


class Returns:
    def __init__(self, display_type="", display_textblob="", display_vader="", display_extra="", display_img="/static/",
                 display_name=""):
        self.type = display_type
        self.textblob = display_textblob
        self.vader = display_vader
        self.extra = display_extra
        self.image_path = display_img
        self.name = display_name
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
    analyser = SentimentIntensityAnalyzer()
    result = analyser.polarity_scores(text_to_analyse)
    return result["compound"]
# #########################


# ANALYSING THE VADERSENTIMENT RESULT


def rank_vader_score(vader_score):
    if vader_score >= 0.5:
        polarity = "Positive"
    elif vader_score <= -0.5:
        polarity = "Negative"
    else:
        polarity = "Neutral"

    return polarity
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
        if movie_keyword.lower() in i.lower():
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

    return_to_flask_textblob = "According to TextBlob, we got the following results for this movie: <br>"
    return_to_flask_vader = "According to VaderSentiment, we got the following results for this movie: <br>"
    movie_list = search_for_movie(user_input)
    search_result = check_similarities(movie_list)

    flask_returns = Returns()

    if okay == "None":
        flask_returns.extra = "No movie names contained this keyword. Try again. <br>"\

    elif okay == "One":
        actual_movie_name = search_result
        flask_returns.extra = "Results for movie " + str(actual_movie_name) + ": <br>"

        reviews = get_movie_reviews_list(actual_movie_name)

        textblob_positives = 0
        textblob_negatives = 0
        textblob_neutrals = 0

        vader_positives = 0
        vader_negatives = 0
        vader_neutrals = 0

        for i in reviews:

            to_check = rank_textblob_score(analysis_textblob(i))

            if to_check == "Positive":
                textblob_positives += 1
            elif to_check == "Negative":
                textblob_negatives += 1
            elif to_check == "Neutral":
                textblob_neutrals += 1

            to_check = rank_vader_score(analysis_vadersentiment(i))

            if to_check == "Positive":
                vader_positives += 1
            elif to_check == "Negative":
                vader_negatives += 1
            elif to_check == "Neutral":
                vader_neutrals += 1

        total = textblob_neutrals + textblob_negatives + textblob_positives

        return_to_flask_textblob += "Out of " + str(total) + " reviews, we got: <br>"
        return_to_flask_textblob += "<h4> {} Positives, {} Negatives and {} Neutrals " \
                                    "</h4>".format(textblob_positives, textblob_negatives, textblob_neutrals)

        return_to_flask_vader += "Out of " + str(total) + " reviews, we got: <br>"
        return_to_flask_vader += "<h4> {} Positives, {} Negatives and {} Neutrals " \
                                 "</h4>".format(vader_positives, vader_negatives, vader_neutrals)

        image_path = actual_movie_name
        image_path = image_path.replace(" ", "-")

        flask_returns.textblob = return_to_flask_textblob
        flask_returns.vader = return_to_flask_vader

        flask_returns.image_path = flask_returns.image_path + image_path + ".jpg"
        flask_returns.name = actual_movie_name

    elif okay == "Multiple":
        flask_returns.extra = "We found multiple movies with similar names. " \
                          "Please check the list and write again the exact name. <br>"
        list_of_names = search_result
        list_of_names.sort()
        for i in list_of_names:
            flask_returns.extra = flask_returns.extra + i + "<br>"

    flask_returns.type = okay

    return flask_returns
# #########################
