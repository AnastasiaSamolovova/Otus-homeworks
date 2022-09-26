"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users/"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts/"
COMMENTS_DATA_URL = "https://jsonplaceholder.typicode.com/comments/"

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status)
            if (response.status == 200):
                json = await response.json()
                return json

async def get_users():
    return await fetch_json(USERS_DATA_URL)


async def get_posts():
    return await fetch_json(POSTS_DATA_URL)

    
async def get_post(post_id: int):
    return await fetch_json(POSTS_DATA_URL + str(post_id))
   