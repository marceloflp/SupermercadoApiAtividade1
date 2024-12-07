from flask import request, jsonify
from services.SetorService import findAll, findById, update, delete, insert
from helpers.application import app

@app.get('/setores')
def findAllSetores():
    return findAll()

@app.get('/setores/<int:id>')
def findByIdSetor(id):
    return findById(id)

@app.post('/setores')
def insertSetor():
    return insert()

@app.put('/setores/<int:id>')
def updateSetor(id):
    setorAtualizado = request.json
    return update(id,setorAtualizado )

@app.delete('/setores/<int:id>',)
def deleteSetor(id):
    return delete(id)

if __name__ == '__main__': 
    app.run(debug=True)
