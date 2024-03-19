from flask import Flask
from helpers import *

app = Flask(__name__)
app.secret_key = 'alura'
    
from views import *

def bot(prompt,historico):
    pass
if __name__ == "__main__":
    app.run(debug = True)
