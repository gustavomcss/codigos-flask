from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('padrao.html',
                           docTitle = 'Liga PHSC')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html',
                           docTitle = 'Liga PHSC - Sobre')

@app.route('/contato')
def contato():
    return render_template('contato.html',
                           docTitle = 'Liga PHSC - Contato')

app.run(debug = True)