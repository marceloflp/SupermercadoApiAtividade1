from helpers.application import app
from controllers.UsuarioController import *
from controllers.CategoriaController import *
from controllers.ProdutoController import *
from controllers.SetorController import *

@app.route('/')
def hello_world():
    return 'API para supermercado!'

if __name__ == '__main__':
    app.run(debug=True)
