from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<word>")
def word_definition(word):
    df = pd.read_csv("dictionary.csv")
    word_row = df[df['word'] == word]
    definition = word_row['definition'].squeeze()
    dictionary = {"word": word, "definition": definition}
    return dictionary


if __name__ == "__main__":
    app.run(debug=True, port=5001)