from flask import request, jsonify
import sqlite3

from models.Setores import Setores


def findAll():
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
       
        cursor.execute(
            "select * from setores")
        
        resultset = cursor.fetchall()
        
        setores = []
        for st in resultset:
            id = st[0]
            nome = st[1]
            setor = Setores(id,nome)
            setores.append(setor.toJson())
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return jsonify(setores), 200


def findById(id):
    try:
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from setores where id = ?", (id,))
        
        resultset = cursor.fetchone()
        
        if resultset is not None:
            setor = {
                'id': resultset[0], 'nome': resultset[1]}
        else:
            return (jsonify({'mensagem': 'Setor não encontrado'}), 404)
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500

    return jsonify(setor), 200

def insert():

    setorNovo = request.json

    connection = sqlite3.connect('supermercado.db')

    cursor = connection.cursor()

    cursor.execute(
        "insert into setores(nome) values (?)", (setorNovo['nome'],))

    connection.commit()

    id = cursor.lastrowid
    setorNovo['id'] = id

    connection.close()

    return jsonify(setorNovo), 200

def update(id, setorAtualizado):
    try:
        
        connection = sqlite3.connect('supermercado.db')
        
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from setores where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            cursor.execute("update setores set nome=? where id=?",
                           (setorAtualizado['nome'], id))
            connection.commit()
            setorAtualizado['id'] = id

            return jsonify(setorAtualizado), 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()

    return (jsonify({'mensagem': 'Setor não encontrado'}), 404)

def delete(id):
    try:
        
        connection = sqlite3.connect('supermercado.db')
       
        cursor = connection.cursor()
        
        cursor.execute(
            "select * from setores where id = ?", (id,))
        
        resultset = cursor.fetchone()
        if resultset is not None:
            
            cursor.execute(
                "delete from setores where id = ?", (id, ))
            
            connection.commit()
            return {'mensagem': "Removido com sucesso"}, 200
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        
        connection.close()
    return (jsonify({'mensagem': 'Setor não encontrado'}), 404)