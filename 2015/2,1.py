import requests as req

header = {'Accept':
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Cookie':
	'_ga=GA1.2.2069303857.1722620088; _gid=GA1.2.1026249312.1722620088; _ga_MHSNPJKWC7=GS1.2.1722620088.1.1.1722620128.0.0.0; session=53616c7465645f5f044b3ea6cc4c731a941482de5e7a058a039f3998ffb77344b2d632bbcefa7c7c65f09f51d71846387d1abf5e9506c8e9fb440562565abac5'}
# both 'x-test' and 'x-test2' are sent
dimensions = req.get('https://adventofcode.com/2015/day/2/input', headers=header).content.decode('UTF-8')

full_area = 0
for present_size in dimensions.splitlines():
    current_dimensions = present_size.split("x")
    l = int(current_dimensions[0])
    w = int(current_dimensions[1])
    h = int(current_dimensions[2])
    area_without_slack = 2 * l * w + 2 * w * h + 2 * h * l
    slack = min(l * w, w * h, h * l)
    full_area = full_area + area_without_slack + slack

print(full_area)