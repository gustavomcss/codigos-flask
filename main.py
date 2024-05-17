from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',
                           docTitle = 'Liga PHSC - Home')

app.run(debug=True)