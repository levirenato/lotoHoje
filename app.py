from flask import Flask, render_template
from loto_script import data, numbers, game

# Crie uma instância do aplicativo Flask
app = Flask(__name__)


# Defina uma rota para a página inicial
@app.route('/')
def hello_world():
    return render_template("index.html", dataframe=data, jogos=game, numeros=numbers)


# Executa o aplicativo quando este arquivo for executado
if __name__ == '__main__':
    app.run(port=8000, debug=True)
