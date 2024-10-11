import requests
import json
from credentials import RAPIDAPI_KEY

async def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response.text)
    return json_data['url']

async def get_new_meme():

    url = "https://programming-memes-images.p.rapidapi.com/v1/memes"

    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "programming-memes-images.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    return response.json()[0]['image']