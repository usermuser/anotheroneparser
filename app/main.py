import asyncio
import pathlib

import aiofiles
from aiohttp import ClientSession
from bs4 import BeautifulSoup

urls_todo = ['https://docs.python.org/3/']
urls_seen = set()
depth = 3


async def write(html: str, filename='test.html'):
    async with aiofiles.open(filename, mode='w') as f:
        await f.write(html)


async def fetch_html(url: str, session: ClientSession, **kwargs) -> str:
    # можно ли использовать ту же сессию для запросов?
    # по идее да, так как на сайте может использоваться авторизация.
    # а мы можем ходить через прокси, поэтому используем одну сессию
    # пока не возникнет необходимость сменить сессию.
    response = await session.request(method='GET', url=url, **kwargs)
    response.raise_for_status()
    return await response.text()


async def add_urls(urls, dest: set) -> None:
    for url in urls:
        dest.add(url)


def get_urls(page):  # cpu bound task, runs synchronously
    soup = BeautifulSoup(page, 'html.parser')
    urls = soup.find_all('a')
    return urls


async def main():
    done = False
    # for i in range(depth):
    while True:
        if len(urls_todo) <= 0:
            break

        url = urls_todo.pop()
        async with ClientSession() as session:
            page = await fetch_html(url, session)
            # await write(html=page, filename=f"{depth}_{url}.html")
            # await write(html=page, filename=f"{i}.html")
            print(f"Recieved page with url: {url}, assume written to file.")
            urls = get_urls(page)  # blocking operation
            print(f"Got {len(urls)} urls from page")
            urls_seen.add(url)
            urls_todo.extend(urls)
            # await add_urls(urls, urls_todo)


if __name__ == '__main__':
    # asyncio.run(main())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_until_complete(asyncio.sleep(0))  # Zero-sleep to allow underlying connections to close
    loop.close()
