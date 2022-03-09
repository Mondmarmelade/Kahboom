#Here we import all resources
import json
import urllib.request as ur, json
import urllib
from waitress import serve
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    #Returns index.html
    return render_template("index.html")

@app.route('/quizID/<ID>')
def quizIDURL(ID):
    try:
        response = ur.urlopen("https://play.kahoot.it/rest/kahoots/" + ID)
        q = json.loads(response.read())["questions"]

        answers = []

        number = 0

        for answer in q:
            number += 1
            if answer.get("type") == "quiz":
                for i in range(len(answer.get("choices"))):
                    if answer["choices"][i]["correct"] == True:

                        colors = ["Red", "Blue", "Yellow", "Green"]

                        Color = colors[i]

                        newAnswer = {
                            "number": number,
                            "answer": answer["choices"][i].get("answer"),
                            "color": Color,
                        }
                        answers.append(newAnswer)

        return render_template("answers.html", answers=answers)
        #Returns awnsers.html

    except urllib.error.HTTPError as exception:
        #This returns an error if there is an HTTPError
        return "Check if the Quiz-ID is correct or try again later"

@app.route('/quizName/<Name>')
def quizName(Name):
    try:
        response = ur.urlopen("https://kahoot.it/rest/kahoots/?query=" + Name + "&limit=10")
        q = json.loads(response.read())["entities"]

        selects = []

        for select in q:

            newSelect = {
                "name": select["card"]["title"],
                "id": select["card"]["uuid"],
                "creator": select["card"]["creator_username"]
            }

            selects.append(newSelect)


        return render_template("select.html", selects=selects)
        #Returns select.html

    except urllib.error.HTTPError as exception:
        #This returns an error if there is an HTTPError
        return "Check if the Quiz-Name has correct synatx or try again later"

if __name__ == "__main__":
    #This runs the flask process
    serve(app, host='0.0.0.0', port=5000, url_scheme='https')