from pyquery import PyQuery

html = """
<html>
    <body>
        <p>Apple</p>
        <p>Banana</p>
        <p>Carrot</p>
    </body>
</html>
"""

doc = PyQuery(html)

print(doc)
print(doc('p'))
print(doc('p').eq(2))
print(doc('p').eq(2).text())