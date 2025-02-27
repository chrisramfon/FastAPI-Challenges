from fastapi import FastAPI, Depends
from typing import Annotated
import json

app = FastAPI()


def readUsersJson( ):

    try:
        file = open( 'users.json', 'r' )
        yield file.read()
    finally:
        file.close()



@app.get( '/users' )
def getUsers( data: Annotated[ str, Depends( readUsersJson ) ] ):

    data = json.loads( data )
    return data


@app.get( '/users/{userId}' )
def getUser( userId: int, data: Annotated[ str, Depends( readUsersJson ) ] ):

    data = json.loads( data )

    for user in data:
        if user[ 'id' ] == userId: return user
