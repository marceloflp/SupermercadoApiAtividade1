from flask import request, jsonify
import sqlite3

from models.Produtos import Produtos


def findAll():
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
       
        cursor.execute(
            "select * from produtos")
        
        resultset = cursor.fetchall()
        
        produtos = []
        for prod in resultset:
            id = prod[0]
            nome = prod[1]
            produto = Produtos(id,nome)
            produtos.append(produto.toJson())
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return jsonify(produtos), 200


def findById(id):
    try:
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from produtos where id = ?", (id,))
        
        resultset = cursor.fetchone()
        
        if resultset is not None:
            produto = {
                'id': resultset[0], 'nome': resultset[1]}
        else:
            return (jsonify({'mensagem': 'Produto não encontrado'}), 404)
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(produto), 200

def insert():

    produtoNovo = request.json

    connection = sqlite3.connect('supermercado.db')

    cursor = connection.cursor()

    cursor.execute(
        "insert into produtos(nome) values (?)", (produtoNovo['nome'],))

    connection.commit()

    id = cursor.lastrowid
    produtoNovo['id'] = id

    connection.close()

    return jsonify(produtoNovo), 200

def update(id, produtoAtualizado):
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from produtos where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            cursor.execute("update produtos set nome=? where id=?",
                           (produtoAtualizado['nome'], id))
            connection.commit()
            produtoAtualizado['id'] = id

            return jsonify(produtoAtualizado), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()

    return (jsonify({'mensagem': 'Produto não encontrado'}), 404)

def delete(id):
    try:
        
        connection = sqlite3.connect('supermercado.db')
       
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from produtos where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            
            cursor.execute(
                "delete from produtos where id = ?", (id, ))
            
            connection.commit()
            return {'mensagem': "Removido com sucesso"}, 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return (jsonify({'mensagem': 'Produto não encontrado'}), 404)