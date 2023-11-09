SETUP_BOOKS = '''

CREATE TABLE Book
(
  	id INTEGER PRIMARY KEY AUTOINCREMENT,
  	title char(50) NOT NULL,
  	author char(50) NOT NULL,
    release_date varchar(9)
);

'''

SETUP_CLIENT = '''

CREATE TABLE Client
(
  	cpf varchar(11),
  	name char(50) NOT NULL,
  	phone_number varchar(11) UNIQUE,
	PRIMARY KEY(cpf) 
);

'''

SETUP_RENT = '''

CREATE TABLE Rent
(
    id_book int,
  	id_client varchar(11),
    PRIMARY KEY(id_book, id_client),
    FOREIGN key(id_book) REFERENCES Book(id) ON UPDATE CASCADE ,
    FOREIGN key(id_client) REFERENCES Client(CPF) ON UPDATE CASCADE
); 

'''

############ Adding data in data base ############

ADD_BOOK = '''

INSERT INTO Book (title, author, release_date) values ({values});

''' 

ADD_CLIENT = '''

INSERT INTO Client (cpf, name, phone_number) values ({values});

''' 

MAKE_RENT = '''

IF (SELECT COUNT(*) FROM Rent WHERE id_client = {cpf}) < {MAX} 
    AND
(SELECT COUNT(*) FROM Rent WHERE id_book = {id_book}) = 0

BEGIN
    INSERT INTO Rent values ({id_book}, {cpf});
END

'''

############ Deleting data in data base ############

DELETE_BOOK = '''

DELETE FROM Book WHERE id = {id};

'''

DELETE_CLIENT = '''

DELETE FROM Book WHERE cpf = {cpf};

'''

REMOVE_RENT = '''

DELETE FROM Rent WHERE id_client = {cpf} and id_book = {id_book};

'''

############ Updating data in data base ############


UPDATE_CLIENT = '''

UPDATE Client set phone_number = {phone_number} WHERE id = {cpf};  

'''

############ Search data in data base ############

SEARCH_BOOK_BY_TITLE = '''

SELECT * FROM Book WHERE title LIKE "%{title}%";

'''

SEARCH_BOOK_BY_AUTHOR = '''

SELECT * FROM Book WHERE author LIKE "%{author}%";

'''

SEARCH_CLIENT_BY_NAME = '''

SELECT * FROM Client WHERE name LIKE "%{name}%";

'''

SEARCH_CLIENT_BY_CPF = '''

SELECT * FROM Client WHERE cpf = {cpf};

'''

SEARCH_RENTS_BY_ID_BOOK = '''

SELECT * FROM Rent WHERE id_book = {id_book};

'''

SEARCH_RENTS_BY_CPF = '''

SELECT * FROM Rent WHERE id_client = {cpf};

'''        

def INSERT_MULTIPLE_INTO(table: str, columns: list[str], values: list[dict[str, any]]):
    query = f"INSERT INTO {table} {*columns ,} values "
    for value in values:
        query += '( '
        for column in columns:
            if isinstance(value[column], str):
                query +=  f'"{value[column]}" ,' 
            else:
                query +=  str(value[column]) + ' ,'
        query = query[:-1] + ') ,'
    query=  query[:-1] + ';'

    print(query)

    return query

