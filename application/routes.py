from flask.templating import render_template
from application import app

@app.route('/')
def home():
    return render_template("home.html", title="Home")

@app.route('/references')
def references():
    return render_template("references.html", title="References")
