# all quearies are stored at src/queries.py
# this file represents just a webapi to interact 
# with the database

import sqlite3
from flask import Flask, request
from src.sqlite_connection import SqliteOperation
from os.path import exists
from src.queries import *

app = Flask(__name__)

# def main():

need_set_up = not exists("./src/ismaylindo.db")

if need_set_up:
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(SETUP_BOOKS)
    cursor.execute(SETUP_CLIENT)
    cursor.execute(SETUP_RENT)
    connection.commit()

    cursor.close()
    connection.close()

def get_books():

    cursor = SqliteOperation()

    cursor.execute(GET_ALL_BOOKS) 

    query_response = cursor.fetchall()

    return { "books" : query_response} , 200


@app.get("/book/title/<title>")
def get_book_by_title(title):

    cursor = SqliteOperation()

    cursor.execute(SEARCH_BOOK_BY_TITLE.format(title=title)) 

    query_response = cursor.fetchall()

    return { "books" : query_response} , 200

@app.get("/book/author/<author>")
def get_book_by_author(author):

    cursor = SqliteOperation()

    cursor.execute(SEARCH_BOOK_BY_AUTHOR.format(author=author)) 

    query_response = cursor.fetchall()

    return { "books" : query_response} , 200

def get_clients():

    cursor = SqliteOperation()

    cursor.execute(GET_ALL_CLIENTS) 

    query_response = cursor.fetchall()

    return { "clients" : query_response} , 200

@app.get("/client/name/<name>")
def get_client_by_name(name):

    cursor = SqliteOperation()

    cursor.execute(SEARCH_CLIENT_BY_NAME.format(name=name)) 

    query_response = cursor.fetchall()
    
    return { "clients" : query_response} , 200
     
@app.get("/client/cpf/<cpf>")
def get_client_by_cpf(cpf):

    cursor = SqliteOperation()


    cursor.execute(SEARCH_CLIENT_BY_CPF.format(cpf=cpf)) 

    query_response = cursor.fetchall()

    
    return { "clients" : query_response} , 200
     
def get_rents():

    cursor = SqliteOperation()

    cursor.execute(GET_ALL_RENTS) 

    query_response = cursor.fetchall()

    return { "rents" : query_response} , 200

@app.get("/rent/id_book/<id_book>")
def get_rent_by_id_book(id_book):

    cursor = SqliteOperation()

    cursor.execute(SEARCH_RENTS_BY_ID_BOOK.format(id_book=id_book)) 

    query_response = cursor.fetchall()
    
    return { "rents" : query_response} , 200
    
@app.get("/rent/cpf/<cpf>")
def get_rent_by_cpf(cpf):

    cursor = SqliteOperation()

    cursor.execute(SEARCH_RENTS_BY_CPF.format(cpf=cpf)) 

    query_response = cursor.fetchall()

    return { "rents" : query_response} , 200

@app.route("/book/", methods=['GET', 'POST'])
def books():

    if request.method == 'GET':
        return get_books()

    cursor = SqliteOperation()

    data = request.json

    if isinstance(data, dict):
        cursor.execute(ADD_BOOK.format(values=f'"{data["title"]}", "{data["author"]}", "{data["release_date"]}"'))
    elif isinstance(data, list):
        cursor.execute(
            INSERT_MULTIPLE_INTO("Book", ["title", 'author', "release_date"], data)
        )
    else: 
        return "", 400 

    cursor.commit()

    return "OK", 201

@app.route("/client/", methods = ['GET', 'POST'])
def clients():

    if request.method == 'GET':
        return get_clients()

    cursor = SqliteOperation()

    data = request.json

    if isinstance(data, dict):
        cursor.execute(ADD_CLIENT.format(values=f'"{data["cpf"]}", "{data["name"]}", "{data["phone_number"]}"'))
    elif isinstance(data, list):
        cursor.execute(
            INSERT_MULTIPLE_INTO("Client", ["cpf", 'name', "phone_number"], data)
        )
    else: 
        return "", 400 

    cursor.commit()

    return "OK", 201

@app.route("/rent/", methods = ['GET', 'POST'])
def rents():

    if request.method == 'GET':
        return get_rents()

    cursor = SqliteOperation()

    data = request.json
    if isinstance(data, dict):

        MAKE_RENT(cursor=cursor , cpf=data["cpf"], id_book = data["id_book"], max = 4)

    elif isinstance(data, list):
        pass
        for sample in data:
            MAKE_RENT(cursor=cursor , cpf=sample["cpf"], id_book = sample["id_book"], max = 4)

    else: 
        return "", 400 


    cursor.commit()

    return "OK", 201

@app.delete("/book/<id_book>")
def delete_book_with_id_book(id_book):
    cursor = SqliteOperation()

    cursor.execute(DELETE_BOOK.format(id=id_book))
    
    cursor.commit()

    return "OK", 200

@app.delete("/client/<cpf>")
def delete_client_with_cpf(cpf):
    cursor = SqliteOperation()

    cursor.execute(DELETE_CLIENT.format(cpf=cpf))
    
    cursor.commit()

    return "OK", 200

@app.delete("/rent/<cpf>/<id_book>")
def delete_rent(cpf, id_book):
    cursor = SqliteOperation()

    cursor.execute(REMOVE_RENT.format(cpf=cpf, id_book=id_book))
    
    cursor.commit()

    return "OK", 200

@app.put("/client/phone_number/")
def update_phone_number():
    cursor = SqliteOperation()

    data = request.json

    cursor.execute(UPDATE_CLIENT.format(phone_number=data["phone_number"], cpf = data["cpf"]))
    
    cursor.commit()

    return "OK", 200
