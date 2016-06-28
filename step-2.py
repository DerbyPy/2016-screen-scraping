from pyquery import PyQuery


doc = PyQuery('https://www.python.org/')

event_widget = doc('.event-widget')
assert len(event_widget) == 1

event_list = event_widget('ul.menu')

# lxml elements
for item in event_list('li a'):
    print(item.text)

# PyQuery items
for item in event_list.items('li a'):
    print(item.text())

# PyQuery items (same as above)
for item in event_list('li a').items():
    print(item.text())