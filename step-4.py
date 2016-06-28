import json

from pyquery import PyQuery


def scrape_page(url):
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


if __name__ == '__main__':
    a_companies = list(scrape_page('https://www.rigzone.com/search/alpha/a/'))
    b_companies = list(scrape_page('https://www.rigzone.com/search/alpha/b/'))
    to_file = a_companies + b_companies

    with open('companies-4.json', 'w') as fh:
        json.dump(to_file, fh, indent=4, sort_keys=True)