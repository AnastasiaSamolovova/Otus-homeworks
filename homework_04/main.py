"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""


import asyncio
from models import create_users, create_tables, create_posts, Session
from jsonplaceholder_requests import get_users, get_posts


        
        
async def async_main():
    users_data: list[dict]
    posts_data: list[dict]
    
    users_data, posts_data= await asyncio.gather(get_users(), get_posts())
    
    await create_tables()
    
    async with Session as session:
        await create_users(session, *users_data)
        await create_posts(session, *posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_main())
