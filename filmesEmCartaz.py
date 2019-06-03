'''
    Feito em flask basicão msm
'''
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
app.debug = True


@app.route("/teste")
def hello():
    return "Acesse <a href='/'>aqui</a>"


@app.route('/', methods=['GET'])
def filmes():
    res = requests.get('http://www.adorocinema.com/filmes/numero-cinemas/')
    soup = BeautifulSoup(res.content)

    data = []
    lista_filmes = soup.find_all('li', {'class': 'mdl'})
    for filme in lista_filmes:
        nome = filme.find('h2', {'class': 'meta-title'}).text.strip()
        info = filme.find(
            'div', {'class': 'meta-body-item meta-body-info'}).text.strip()
        info = " ".join(info.split())
        direcao = filme.find(
            'div', {'class':
                    'meta-body-item meta-body-direction light'}).text.strip()
        direcao = " ".join(direcao.split())
        sinopse = filme.find('div', {'class': 'synopsis'}).text.strip()
        cartaz = filme.find(
            'figure', {'class': 'thumbnail'}).find('img')['src']

        data.append({
            'nome': nome,
            'info': info,
            'direcao': direcao,
            'sinopse': sinopse,
            'cartaz': cartaz
        })

    return jsonify({'filmes': data})


if __name__ == "__main__":
    app.run()
