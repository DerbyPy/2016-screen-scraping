import itertools
import json
import string

from pyquery import PyQuery


def scrape_page(url):
    print('getting url: {}'.format(url))
    doc = PyQuery(url)
    doc.make_links_absolute()

    table = doc('#rz-main-container section:eq(1) .WriteSmallTableTop table:eq(1)')

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

        yield company

def scrape_urls():
    letters_and_nums = list(string.ascii_lowercase[:22]) + ['wxyz']
    print(letters_and_nums)
    urls = map(lambda x: 'https://www.rigzone.com/search/alpha/{}/'.format(x), letters_and_nums)
    return list(itertools.chain.from_iterable(map(scrape_page, urls)))


def save_to_file(fname, data):
    with open(fname, 'w') as fh:
        json.dump(data, fh, indent=4, sort_keys=True)

if __name__ == '__main__':
    data = scrape_urls()
    print(data)
    save_to_file('companies-5.json', data)