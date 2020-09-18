import scholarly

search_query = scholarly.search_author('Marty Banks, Berkeley')

print(next(search_query))
