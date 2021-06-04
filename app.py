from flask import Flask, render_template, request
import core_module

app = Flask(__name__)

input_name = ""

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


@app.route('/')
def home():
    return render_template("index.html")


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
        to_print = str(raw_display.extra) + str(raw_display.textblob) + str(raw_display.vader)
        return render_template("index.html", my_output=to_print)
    elif raw_display.type == "None":
        return render_template("index.html", my_output=str(raw_display.extra))
    elif raw_display.type == "Multiple":
        return render_template("index.html", my_output=str(raw_display.extra))


if __name__ == '__main__':
    app.run()
