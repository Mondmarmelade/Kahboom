import json
import urllib.request as ur, json
import urllib
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    return render_template("search.html")

@app.route('/quizID')
def quizID():
    return render_template("quizID.html")

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

                        if i == 0:
                            Color = "Red"
                        elif i == 1:
                            Color = "Blue"
                        elif i == 2:
                            Color = "Yellow"
                        elif i == 3:
                            Color = "Green"

                        newAnswer = {
                            "number": number,
                            "answer": answer["choices"][i].get("answer"),
                            "color": Color,
                        }
                        answers.append(newAnswer)

        return render_template("answers.html", answers=answers)
        # return answers

    except urllib.error.HTTPError as exception:
        print("\nCheck if the Quiz-ID is correct or try again later")
    # # print(q, file=sys.stderr)
    # return jsonify(q["choices"])

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
        # return selects

    except urllib.error.HTTPError as exception:
        print("\nCheck if the Quiz-Name has correct synatx or try again later")
    # # print(q, file=sys.stderr)
    # return jsonify(q["choices"])

if __name__ == "__main__":
    app.run(debug=True)