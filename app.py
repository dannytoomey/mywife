# run from terminal with 
# FLASK_APP=app.py flask run
from flask import Flask 
from flask import render_template, request, jsonify

app = Flask(__name__, template_folder='./templates', static_folder='./static')

#setup a homepage
@app.route("/")
def home():
    return render_template("home.html")

# run the game. port 33507 is specficially for flask, 
# but it doesn't have to be 33507 
if __name__ == "__main__":
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 33507), processes=2)