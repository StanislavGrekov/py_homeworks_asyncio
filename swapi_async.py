import aiohttp
import asyncio
import asyncpg
import datetime
from more_itertools import chunked
from model import SwapiPeople, Base, engine, Session


async def get_people(people_id, client):
        response = await client.get(f'https://swapi.dev/api/people/{people_id}')
        json_data = await response.json()
        return json_data


async def paste_to_db(people_json):
    async with Session() as session:
        orm_object = [SwapiPeople(json=item) for item in people_json]
        print(orm_object)
        session.add_all(orm_object)
        await session.commit()


MAX_REQ = 5
async def main():
    async with engine.begin() as con:
        await con.run_sync(Base.metadata.create_all)

    tasks = []
    async with aiohttp.ClientSession() as client:

        for i in chunked(range(1,51), MAX_REQ):

            person_coros = []
            for people_id in i:
                person_coro = get_people(people_id, client)
                person_coros.append(person_coro)
            result = await asyncio.gather(*person_coros)
            print(result)
            paste_to_db_coro = paste_to_db(result)
            paste_to_db_task = asyncio.create_task(paste_to_db_coro)
            tasks.append(paste_to_db_task)

    tasks = asyncio.all_tasks() - {asyncio.current_task(), }
    for task in tasks:
        await task



if __name__=='__main__':
    start = datetime.datetime.now()
    asyncio.run(main())
    print(datetime.datetime.now() - start)
