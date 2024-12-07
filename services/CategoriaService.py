from flask import request, jsonify
import sqlite3

from models.Categorias import Categorias


def findAll():
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
       
        cursor.execute(
            "select * from categorias")
        
        resultset = cursor.fetchall()
        
        categorias = []
        for cate in resultset:
            id = cate[0]
            nome = cate[1]
            categoria = Categorias(id,nome)
            categorias.append(categoria.toJson())
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return jsonify(categorias), 200


def findById(id):
    try:
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from categorias where id = ?", (id,))
        
        resultset = cursor.fetchone()
        
        if resultset is not None:
            categoria = {
                'id': resultset[0], 'nome': resultset[1]}
        else:
            return (jsonify({'mensagem': 'Categoria não encontrada'}), 404)
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(categoria), 200

def insert():

    categoriaNova = request.json

    connection = sqlite3.connect('supermercado.db')

    cursor = connection.cursor()

    cursor.execute(
        "insert into categorias(nome) values (?)", (categoriaNova['nome'],))

    connection.commit()

    id = cursor.lastrowid
    categoriaNova['id'] = id

    connection.close()

    return jsonify(categoriaNova), 200

def update(id, categoriaAtualizada):
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from categorias where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            cursor.execute("update categorias set nome=? where id=?",
                           (categoriaAtualizada['nome'], id))
            connection.commit()
            categoriaAtualizada['id'] = id

            return jsonify(categoriaAtualizada), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()

    return (jsonify({'mensagem': 'Categoria não encontrada'}), 404)

def delete(id):
    try:
        
        connection = sqlite3.connect('supermercado.db')
       
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from categorias where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            
            cursor.execute(
                "delete from categorias where id = ?", (id, ))
            
            connection.commit()
            return {'mensagem': "Removido com sucesso"}, 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return (jsonify({'mensagem': 'Categoria não encontrada'}), 404)