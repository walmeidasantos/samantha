from flask import Flask
from helpers import *
from mensagemAdapterApi import IAGenerativa

app = Flask(__name__)
app.secret_key = '4k'

from views import *



def bot(prompt, historico):
    return IAGenerativa.gerar_texto_personalizado(self=IAGenerativa,prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)
