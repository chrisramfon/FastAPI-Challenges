from fastapi import FastAPI, Depends, Query
from difflib import SequenceMatcher
from typing import Annotated

import json

app = FastAPI()


def readBooksJson():

    try:
        file = open( 'books.json' )
        yield file.read()
    finally:
        file.close()



@app.get( '/books' )
def getBooks( books: Annotated[ str, Depends( readBooksJson ) ] ) -> dict:
    
    booksAsDict = json.loads( books )
    return booksAsDict


@app.get( '/search' )
def search( query: Annotated[ str, Query( alias = 'q' ) ], books: Annotated[ str, Depends( readBooksJson ) ] ):

    booksAsDict = json.loads( books )

    result = searchBook( query, booksAsDict )

    return result


def searchBook( query: str, books: dict ) -> list:

    toReturn = []

    for book in books:

        titleComparation = SequenceMatcher( a = query, b = book[ 'title' ] ).ratio()

        if titleComparation >= 0.6: toReturn.append( book )

        authorComparation = SequenceMatcher( a = query, b = book[ 'author' ] ).ratio()

        if authorComparation >= 0.6: toReturn.append( book )

    return toReturn