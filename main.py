from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('padrao.html',
                           docTitle = 'Liga PHSC')

@app.route('/contato')
def contato():
    return render_template('contato.html',
                           docTitle = 'Liga PHSC - Contato')

app.run(debug = True)