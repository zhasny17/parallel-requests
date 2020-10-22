from aiohttp import ClientSession
import asyncio
import os

URLS = [f'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png' for number in range(1, 151)]


async def save_image(image_content: bytes, image_name: str) -> None:
    if not os.path.exists('images/async_alg/'):
        os.makedirs('images/async_alg/')
    with open(f'images/async_alg/{image_name}', 'wb') as f:
        f.write(image_content)


async def download_image(session: ClientSession, url: str) -> None:
    response = await session.request(method='GET', url=url)
    image_content = await response.content.read()
    image_name = url.split('pokemon/')[1]
    await save_image(image_content, image_name)


async def generate_consumers() -> None:
    tasks = []
    async with ClientSession() as session:
        for url in URLS:
            tasks.append(download_image(session, url))
        await asyncio.gather(*tasks)


def main():
    asyncio.run(generate_consumers())


if __name__ == "__main__":
    main()
