from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',
                           docTitle = 'Liga PHSC')

app.run(debug=True)