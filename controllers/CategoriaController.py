from flask import request, jsonify
from services.CategoriaService import findAll, findById, update, delete, insert
from helpers.application import app

@app.get('/categorias')
def findAllCategorias():
    return findAll()

@app.get('/categorias/<int:id>')
def findByIdCategoria(id):
    return findById(id)

@app.post('/categorias')
def insertCategoria():
    return insert()

@app.put('/categorias/<int:id>')
def updateCategoria(id):
    categoriaAtualizada = request.json
    return update(id, categoriaAtualizada )

@app.delete('/categorias/<int:id>',)
def deleteCategoria(id):
    return delete(id)

if __name__ == '__main__': 
    app.run(debug=True)
