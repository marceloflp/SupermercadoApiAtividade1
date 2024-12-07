from flask import request, jsonify
from services.UsuarioService import findAll, findById, update, delete, insert
from helpers.application import app

@app.get('/usuarios')
def findAllUsuarios():
    return findAll()

@app.get('/usuarios/<int:id>')
def findByIdUsuario(id):
    return findById(id)

@app.post('/usuarios')
def insertUsuario():
    return insert()

@app.put('/usuarios/<int:id>')
def updateUsuario(id):
    usuarioAtualizado = request.json
    return update(id,usuarioAtualizado )

@app.delete('/usuarios/<int:id>',)
def deleteUsuario(id):
    return delete(id)

if __name__ == '__main__': 
    app.run(debug=True)
