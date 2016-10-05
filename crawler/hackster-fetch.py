from lxml import html
import requests

page = requests.get('https://www.hackster.io/projects?ref=topnav')
tree = html.fromstring(page.content)
print(type(tree))

#mobile-scroll-row-item project-thumb-container col-sm-6 col-md-4 has-data link-added
projects = tree.xpath('//div[@class="card-text"]/h4/a/text()')
print('type of projects variable is {0}'.format(type(projects)))

authors = tree.xpath('//div[@class="card-text"]/p/span/a/text()')
print('type of authors variable is {0}'.format(type(authors)))

print('length of projects is {0}'.format(len(projects)))
print('length of authors is {0}'.format(len(authors)))

if len(projects) == len(authors) + 1:
	for name, author in zip(projects, authors):
		print('{0} ----- {1}'.format(name, author))
else:
	print('whoops...')