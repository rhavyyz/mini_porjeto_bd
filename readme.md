For the setup.sh file to run you should install

	pip install virtualenv

And you also wants do run setup.sh as source

	source ./setup.sh

To go out of python environment just type 

	deactivate



if you are using windows then you need to follow those steps https://www.youtube.com/watch?v=4orYC5ARfn8


# Library API Documentation

### Client

- /client/                                              -   POST
    
    > Input Format
    > 
    
    ```json
    // IF YOU WANT TO INSERT JUST ONE ENTITY
    {
    	"cpf": string,
      "name": string,
      "phone_number": string
    }
    
    // IF YOU WANT TO INSET MULTIPLE ENTITIES AT THE SAME TIME
    [
    	{
    		"cpf": string,
    	  "name": string,
    	  "phone_number": string
    	},
    ...
    	{
    		"cpf": string,
    	  "name": string,
    	  "phone_number": string
    	}
    ]
    ```
    
    > Output
    > 
    
    ```json
    //With a 201 status code
    "OK"
    ```
    
- /client/                                              -   GET
    
    > Input Format
    > 
    
    ```
    Null
    ```
    
    > Output
    > 
    
    ```json
    {
    	"clients": [
    		[
    			cpf : string,
    			name : string,
    			phone_number : string
    	  ],
    	  ...
    	]
    }
    ```
    
- /client/name/<name>                                   -   GET
    
    > Input Format
    > 
    
    ```
    <name> : string
    ```
    
    > Output
    > 
    
    ```json
    {
    	"clients": [
    		[
    			cpf : string,
    			name : string,
    			phone_number : string
    	  ],
    	  ...
    	]
    }
    ```
    
- /client/cpf/<cpf>                                     -   GET
    
    > Input Format
    > 
    
    ```
    <cpf> :  string
    ```
    
    > Output
    > 
    
    ```json
    {
    	"clients": [
    		[
    			cpf : string,
    			name : string,
    			phone_number : string
    	  ],
    	  ...
    	]
    }
    ```
    
- /client/phone_number/                                 -   PUT
    
    > Input Format
    > 
    
    ```json
    {
    	"cpf": string,
    	"phone_number": string
    }
    ```
    
    > Output
    > 
    
    ```json
    //With a 200 status code
    "OK"
    ```
    
- /client/<cpf>                                         -  DELETE
    
    > Input Format
    > 
    
    ```
    <cpf> : string
    ```
    
    > Output
    > 
    
    ```json
    // With 200 status code
    "OK" 
    ```
    

### Book

- /book/                                                -   POST
    
    > Input Format
    > 
    
    ```json
    // IF YOU WANT TO INSERT JUST ONE ENTITY
    {
    	"title": string,
      "author": string,
      "release_date": string
    }
    
    // IF YOU WANT TO INSET MULTIPLE ENTITIES AT THE SAME TIME
    [
    	{
    		"title": string,
    	  "author": string,
    	  "release_date": string
    	},
    ...
    	{
    		"title": string,
    	  "author": string,
    	  "release_date": string
    	}
    ]
    ```
    
    > Output
    > 
    
    ```json
    //With a 200 status code
    "OK"
    ```
    
- /book/                                                -   GET
    
    > Input Format
    > 
    
    ```
    Null
    ```
    
    > Output
    > 
    
    ```json
    {
    	"books": [
    		[
    			"title": string,
    		  "author": string,
    		  "release_date": string
    	  ],
    	  ...
    	]
    }
    ```
    
- /book/title/<title>                                   -   GET
    
    > Input Format
    > 
    
    ```json
    <title> : string
    ```
    
    > Output
    > 
    
    ```json
    {
    	"books": [
    		[
    			"title": string,
    		  "author": string,
    		  "release_date": string
    	  ],
    	  ...
    	]
    }
    ```
    
- /book/author/<author>                                 -   GET
    
    > Input Format
    > 
    
    ```
    <author> : string
    ```
    
    > Output
    > 
    
    ```json
    {
    	"books": [
    		[
    			"title": string,
    		  "author": string,
    		  "release_date": string
    	  ],
    	  ...
    	]
    }
    ```
    
- /book/<id_book>                                       -  DELETE
    
    > Input Format
    > 
    
    ```
    <id_book> : int
    ```
    
    > Output
    > 
    
    ```json
    // With 200 status code
    "OK"
    ```
    

### Rent

- /rent/                                                -   POST
    
    > Input Format
    > 
    
    ```json
    // A rent can only be done once at the time
    {
    	"cpf": string,
      "id_book": int
    }
    ```
    
    > Output
    > 
    
    ```json
    //With a 200 status code
    "OK"
    ```
    
- /rent/                                                -   GET
    
    > Input Format
    > 
    
    ```
    Null
    ```
    
    > Output
    > 
    
    ```json
    {
    	"rents":
    	[
    		[
    			"id_book" : int,
    			"cpf" : string
    		],
    		...
    	]
    }
    ```
    
- /rent/id_book/<id_book>                               -   GET
    
    > Input Format
    > 
    
    ```json
    <id_book> : int
    ```
    
    > Output
    > 
    
    ```json
    {
    	"rents":
    	[
    		[
    			"id_book" : int,
    			"cpf" : string
    		],
    		...
    	]
    }
    ```
    
- /rent/cpf/<cpf>                                       -   GET
    
    > Input Format
    > 
    
    ```
    <cpf> : string
    ```
    
    > Output
    > 
    
    ```json
    {
    	"rents":
    	[
    		[
    			"id_book" : int,
    			"cpf" : string
    		],
    		...
    	]
    }
    ```
    
- /rent/<cpf>/<id_book>                                 -  DELETE
    
    > Input Format
    > 
    
    ```json
    <cpf> : string
    <id_book> : int
    ```
    
    > Output
    > 
    
    ```json
    // With 200 status code
    "OK"
    ```
    

<aside>
⚠️ In case you receive an 500: internal server error, it probably means the parameters you sent are wrong

</aside>
