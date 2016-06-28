from pyquery import PyQuery


doc = PyQuery('https://www.rigzone.com/search/alpha/a/')
doc.make_links_absolute()

table = doc('#rz-main-container section:eq(1) .WriteSmallTableTop table:eq(1)')

for row in table.items('tr:gt(0)'):
    company_col = row('td').eq(0)
    phone_col = row('td').eq(1)
    website_col = row('td').eq(2)

    details_url = company_col('a').attr('href')
    company_name = company_col.text()
    company_phone = phone_col.text()
    company_url = website_col('a').attr('href')

    print(company_name, company_phone, company_url, details_url)
    break