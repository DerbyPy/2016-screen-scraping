import asyncio
import itertools
import json
import string

import aiohttp
from pyquery import PyQuery


async def scrape_page(session, url):
    async with session.get(url) as resp:
        content = await resp.text()

    print('parsing url: {}'.format(url))
    doc = PyQuery(content)
    doc.make_links_absolute(base_url=url)

    table = doc('#rz-main-container section:eq(1) .WriteSmallTableTop table:eq(1)')

    results = []

    for row in table.items('tr:gt(0)'):
        company_col = row('td').eq(0)
        phone_col = row('td').eq(1)
        website_col = row('td').eq(2)

        company = {
            'name': company_col.text(),
            'phone': phone_col.text(),
            'url': website_col('a').attr('href'),
            'details_url': company_col('a').attr('href'),
        }

        results.append(company)

    return results


async def scrape_urls():
    letters_and_nums = list(string.ascii_lowercase[:22]) + ['wxyz']
    print(letters_and_nums)
    urls = map(lambda x: 'https://www.rigzone.com/search/alpha/{}/'.format(x), letters_and_nums)

    with aiohttp.ClientSession() as session:
        scrapers = [scrape_page(session, url) for url in urls]
        done, pending = await asyncio.wait(scrapers)

    return list(itertools.chain.from_iterable(map(lambda task: task.result(), done)))


def save_to_file(fname, data):
    with open(fname, 'w') as fh:
        json.dump(data, fh, indent=4, sort_keys=True)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(scrape_urls())
    print(data[0])
    save_to_file('companies-6.json', data)