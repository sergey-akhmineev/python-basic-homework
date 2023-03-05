"""
Домашнее задание №3
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
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from homework_04.models import User, Post, Base, engine, async_session


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_users(users_data):
    users_list = []
    for user in users_data:
        users_list.append(User(id=user['id'],
                               name=user['name'],
                               username=user['username'],
                               email=user['email']))
    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            session.add_all(users_list)


async def create_posts(posts_data):
    posts_list = []
    for post in posts_data:
        posts_list.append(Post(id=post['id'],
                               title=post['title'],
                               user_id=post['userId'],
                               body=post['body']))
    async with async_session() as session:  # type: AsyncSession
        async with session.begin():
            session.add_all(posts_list)


async def async_main():
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    await create_tables()
    await create_users(users_data)
    await create_posts(posts_data)


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(async_main())


if __name__ == '__main__':
    main()
