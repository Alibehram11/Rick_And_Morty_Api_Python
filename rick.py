import requests

def get_rick_and_morty():
    url="https://rickandmortyapi.com/api/character/"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json() 
        characters=data["results"]

        for character in characters:
            name=character["name"]
            species=character["species"]
            status=character["status"]
            nickname=character["name"]
            print(f"Nam: {name},Species: {species},Status: {status},Nickname: {nickname}")
    else:
        print("Durum kodu olumsuz!!!",response.status_code)

get_rick_and_morty()
