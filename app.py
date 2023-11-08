import sqlite3

from flask import Flask, request, jsonify
# from

from os.path import exists

from src.queries import *

from src.client import Client
from src.book import Book

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

@app.get("/book/title/<title>")
def get_book_by_title(title):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(SEARCH_BOOK_BY_TITLE.format(title=title)) 

    query_response = cursor.fetchall()

    cursor.close()
    connection.close()

    return { "books" : query_response} , 200

@app.get("/book/author/<author>")
def get_book_by_author(author):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(SEARCH_BOOK_BY_AUTHOR.format(author=author)) 

    query_response = cursor.fetchall()

    cursor.close()
    connection.close()

    return { "books" : query_response} , 200

@app.get("/client/name/<name>")
def get_client_by_name(name):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(SEARCH_CLIENT_BY_NAME.format(name=name)) 

    query_response = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return { "client" : query_response} , 200
     
@app.get("/client/cpf/<cpf>")
def get_client_by_cpf(cpf):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(SEARCH_CLIENT_BY_CPF.format(cpf=cpf)) 

    query_response = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return { "client" : query_response} , 200
     
@app.get("/rent/id_book/<id_book>")
def get_rent_by_id_book(id_book):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(SEARCH_RENTS_BY_ID_BOOK.format(id_book=id_book)) 

    query_response = cursor.fetchall()

    cursor.close()
    connection.close()
    
    return { "rent" : query_response} , 200
    
@app.get("/rent/cpf/<cpf>")
def get_rent_by_cpf(cpf):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    print(SEARCH_RENTS_BY_CPF.format(cpf=cpf))

    cursor.execute(SEARCH_RENTS_BY_CPF.format(cpf=cpf)) 

    query_response = cursor.fetchall()

    cursor.close()
    connection.close()

    return { "rent" : query_response} , 200

@app.post("/book/")
def post_book():

    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    data = request.json

    cursor.execute(ADD_BOOK.format(values=f'"{data["title"]}", "{data["author"]}", "{data["release_date"]}"'))
    
    connection.commit()

    cursor.close()
    connection.close()

    return "OK", 200

@app.post("/client/")
def post_client():
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    data = request.json

    cursor.execute(ADD_CLIENT.format(values=f'"{data["cpf"]}", "{data["name"]}", "{data["phone_number"]}"'))
    
    connection.commit()

    cursor.close()
    connection.close()

    return "OK", 200

@app.post("/rent/")
def post_rent():
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    data = request.json

    cursor.execute(MAKE_RENT.format(cpf=data["cpf"], id_book = data["id_book"]))
    
    connection.commit()

    cursor.close()
    connection.close()

    return "OK", 200

@app.delete("/book/<id>")
def delete_book_with_id_book(id):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(DELETE_BOOK.format(id=id))
    
    connection.commit()

    cursor.close()
    connection.close()

    return "OK", 200

@app.delete("/client/<cpf>")
def delete_book_with_cpf(cpf):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(DELETE_CLIENT.format(cpf=cpf))
    
    connection.commit()

    cursor.close()
    connection.close()

    return "OK", 200

@app.delete("/rent/<cpf>/<id_book>")
def delete_book_with_rent(cpf, id_book):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(REMOVE_RENT.format(cpf=cpf, id_book=id_book))
    
    connection.commit()

    cursor.close()
    connection.close()

    return "OK", 200

@app.put("/client/phone_number/<phone_number>")
def delete_book_with_phone_number(phone_number):
    connection = sqlite3.connect("./src/ismaylindo.db")
    cursor = connection.cursor() 

    cursor.execute(UPDATE_CLIENT.format(phone_number=phone_number))
    
    connection.commit()

    cursor.close()
    connection.close()

    return "OK", 200