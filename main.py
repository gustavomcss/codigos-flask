from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('padrao.html',
                           docTitle = 'Liga PHSC')

@app.route('/sobre', methods = ['GET'])
def sobre():
    return render_template('sobre.html',
                           docTitle = 'Liga PHSC - Sobre')

@app.route('/contato', methods = ['GET'])
def contato():
    return render_template('contato.html',
                           docTitle = 'Liga PHSC - Contato')

@app.route('/teste', methods = ['GET'])
def teste():
    return render_template('teste_bootstrap.html',
                           docTitle = 'Liga PHSC - Testes')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

''' --- PARA HOSPEDAR NO HEROKU ---

1. pip install gunicorn

2. pip freeze > requirements.txt

3. CREATE Procfile WRITE INTO:
    web: gunicorn (nome_arquivo):(var_flask)

'''