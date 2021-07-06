# libreria la cual nos sirve para crear un cliente api
import requests
# libreria la cual nos sirve para gestionar formatos JSON
import json

# diferencia cada script importado del principal
if __name__ == '__main__':
    url= 'https://imgur.com/download/ciwlCWa/Python%20Wallpaper'
    response = requests.get(url,stream=True)
    with open('image.jpg','wb') as file:
        for chunk in response.iter_content():
            file.write(chunk)
response.close()
