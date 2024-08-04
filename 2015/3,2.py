import requests as req

header = {'Accept':
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Cookie':
	'_ga=GA1.2.2069303857.1722620088; _gid=GA1.2.1026249312.1722620088; _ga_MHSNPJKWC7=GS1.2.1722620088.1.1.1722620128.0.0.0; session=53616c7465645f5f044b3ea6cc4c731a941482de5e7a058a039f3998ffb77344b2d632bbcefa7c7c65f09f51d71846387d1abf5e9506c8e9fb440562565abac5'}
# both 'x-test' and 'x-test2' are sent
directions = req.get('https://adventofcode.com/2015/day/3/input', headers=header).content.decode('UTF-8')

xs = 0
ys = 0
xr = 0
yr = 0
index = 0
visited_coordinates_santa = [(xs, ys)]
visited_coordinates_robot = []
for move in directions:
    index = index + 1
    if index % 2 == 0:
        if move == '^':
            yr = yr + 1
        elif move == 'v':
            yr = yr - 1
        elif move == '>':
            xr = xr + 1
        elif move == '<':
            xr = xr - 1
        visited_coordinates_robot.append((xr, yr))
    else:
        if move == '^':
            ys = ys + 1
        elif move == 'v':
            ys = ys - 1
        elif move == '>':
            xs = xs + 1
        elif move == '<':
            xs = xs - 1
        visited_coordinates_santa.append((xs, ys))

visited_coordinates = visited_coordinates_robot + visited_coordinates_santa

finished_result = set(visited_coordinates)
finished_list = list(finished_result)

print(len(finished_list))