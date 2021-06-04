from flask import Flask, render_template, request
import core_module

app = Flask(__name__)

input_name = ""


@app.route('/')
def home():
    out = "Hello. Not sure if you should watch a certain movie? <br> Enter the name here. Using the best 2 Sentiment " \
          "Analysis " \
        "libraries (TextBlob and VaderSentiment), we will check the 10 top rated IMDB reviews so you can see if the " \
        "movie is perceived as good or bad. The more Positive results there are, the better."
    return render_template("index.html", image_path="/static/question.png", name_of_movie="Search for a movie name!",
                           extra_out=out)


@app.route('/about.html')
def about():
    return render_template("about.html")


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/search', methods=['GET', 'POST'])
def search():
    global input_name
    input_name = request.form['movie_name']
    print(input_name)

    raw_display = core_module.run_on_search(input_name)

    if raw_display.type == "One":
        return render_template("index.html", image_path=raw_display.image_path, name_of_movie=raw_display.name,
                               extra_out=raw_display.extra, textblob_out=raw_display.textblob,
                               vader_out=raw_display.vader)
    elif raw_display.type == "None":
        return render_template("index.html", image_path="/static/image-not-found.jpg", name_of_movie="Movie not found",
                               extra_out=raw_display.extra)
    elif raw_display.type == "Multiple":
        return render_template("index.html", image_path="/static/question.png", name_of_movie="Multiple entries",
                               extra_out=raw_display.extra)


if __name__ == '__main__':
    app.run()
