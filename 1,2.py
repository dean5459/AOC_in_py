import requests as req

header = {'Accept':
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Cookie':
	'_ga=GA1.2.1613308035.1722532346;' +
    '_gid=GA1.2.209903692.1722532346;' +
    '_ga_MHSNPJKWC7=GS1.2.1722532345.1.1.1722533679.0.0.0;' +
    'session=53616c7465645f5f08f8b9b3c6fd51a99552502d101b4d746c095de0429f0c046fc1ece62996ee357f84e092e3eb5a6383550cdc89b13f26c8ced3cd2b47ec65'}
# both 'x-test' and 'x-test2' are sent
directions = str(req.get('https://adventofcode.com/2015/day/1/input', headers=header).content)

starting_floor = 0
index = 0
for symbol in directions:
    if symbol == '(' or symbol == ')':
        index = index + 1
        if symbol == '(':
            starting_floor = starting_floor + 1
        elif symbol == ')':
            starting_floor = starting_floor - 1
        
        if starting_floor < 0:
            break

print(index)