import requests
import asyncio
import aiohttp

url = "https://devsaadia-weemu-fastapi-backend.hf.space/recommend/"

async def recommend(movie_name):
    #response = requests.get(url + movie_name)
    async with aiohttp.ClientSession() as session:
        async with session.get(url + movie_name) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return {"error": "An error occurred"}