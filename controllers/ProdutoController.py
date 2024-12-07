from flask import request, jsonify
from services.ProdutoService import findAll, findById, update, delete, insert
from helpers.application import app

@app.get('/produtos')
def findAllProduto():
    return findAll()

@app.get('/produtos/<int:id>')
def findByIdProduto(id):
    return findById(id)

@app.post('/produtos')
def insertProduto():
    return insert()

@app.put('/produtos/<int:id>')
def updateProduto(id):
    produtoAtualizado = request.json
    return update(id,produtoAtualizado )

@app.delete('/produtos/<int:id>',)
def deleteProduto(id):
    return delete(id)

if __name__ == '__main__': 
    app.run(debug=True)
