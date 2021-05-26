from .graphql.characters_generated import execute_async_get_characters_gql, execute_get_character_gql
import asyncio

async def start_async() -> None:
    res = await execute_async_get_characters_gql()
    print(res.characters.results[1].name)

def start_sync() -> None:
    res = execute_get_character_gql(id="6")
    print(res.character.name)

def start() -> None:
    start_sync()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_async())