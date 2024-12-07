from flask import request, jsonify
import sqlite3

from models.Usuarios import Usuarios


def findAll():
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
       
        cursor.execute(
            "select * from usuarios")
        
        resultset = cursor.fetchall()
        
        usuarios = []
        for user in resultset:
            id = user[0]
            nome = user[1]
            usuario = Usuarios(id,nome)
            usuarios.append(usuario.toJson())
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return jsonify(usuarios), 200


def findById(id):
    try:
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from usuarios where id = ?", (id,))
        
        resultset = cursor.fetchone()
        
        if resultset is not None:
            usuario = {
                'id': resultset[0], 'nome': resultset[1]}
        else:
            return (jsonify({'mensagem': 'Usuário não encontrado'}), 404)
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(usuario), 200

def insert():

    usuarioNovo = request.json

    connection = sqlite3.connect('supermercado.db')

    cursor = connection.cursor()

    cursor.execute(
        "insert into usuarios(nome) values (?)", (usuarioNovo['nome'],))

    connection.commit()

    id = cursor.lastrowid
    usuarioNovo['id'] = id

    connection.close()

    return jsonify(usuarioNovo), 200

def update(id, usuarioAtualizado):
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from usuarios where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            cursor.execute("update usuarios set nome=? where id=?",
                           (usuarioAtualizado['nome'], id))
            connection.commit()
            usuarioAtualizado['id'] = id

            return jsonify(usuarioAtualizado), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()

    return (jsonify({'mensagem': 'Usuário não encontrado'}), 404)

def delete(id):
    try:
        
        connection = sqlite3.connect('supermercado.db')
       
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from usuarios where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            
            cursor.execute(
                "delete from usuarios where id = ?", (id, ))
            
            connection.commit()
            return {'mensagem': "Removido com sucesso"}, 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return (jsonify({'mensagem': 'Usuário não encontrado'}), 404)