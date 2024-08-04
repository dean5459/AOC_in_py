import requests as req

header = {'Accept':
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Cookie':
	'_ga=GA1.2.2069303857.1722620088; _gid=GA1.2.1026249312.1722620088; _ga_MHSNPJKWC7=GS1.2.1722620088.1.1.1722620128.0.0.0; session=53616c7465645f5f044b3ea6cc4c731a941482de5e7a058a039f3998ffb77344b2d632bbcefa7c7c65f09f51d71846387d1abf5e9506c8e9fb440562565abac5'}
# both 'x-test' and 'x-test2' are sent
grid_instructions = req.get('https://adventofcode.com/2015/day/6/input', headers=header).content.decode('UTF-8')

light_grid = [[False] * 999] * 999


for instr_in_question in grid_instructions.splitlines():
    instructions = instr_in_question.split(' ')
    
    if len(instructions) == 4:
        x = int(instructions[1].split(',')[0])
        y = int(instructions[1].split(',')[1])
        light_grid[x][y] = not(light_grid[x][y])
    else:
        x = int(instructions[2].split(',')[0])
        y = int(instructions[2].split(',')[1])
        if instructions[1] == 'on':
            light_grid[x][y] = True
        else:
            light_grid[x][y] = False

num_of_lights_on = 0

for i in light_grid:
    for j in i:
        if j == True:
            num_of_lights_on = num_of_lights_on + 1

print(num_of_lights_on)