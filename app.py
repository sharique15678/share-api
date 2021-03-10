from flask import Flask,redirect,render_template ,request
from flask.helpers import url_for
app = Flask(__name__)
@app.route('/')
def login():
   return "hello in flask"
if __name__ == "__main__" :
    FLASK_APP = "app"
    app.run(debug=True)