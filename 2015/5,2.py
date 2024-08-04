import requests as req

def two_pairs(stringy):
    for pair in range(0, len(stringy) - 1, 1):
        if stringy.count(stringy[pair:pair + 2]) > 1:
            return True
    return False

def letter_in_between_letters(stringy):
    index = 0
    for letter in stringy:
        if index + 2 < len(stringy):
            if stringy[index + 2] == letter:
                return True
            else:
                index = index + 1
    return False


header = {'Accept':
	'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
    'Cookie':
	'_ga=GA1.2.2069303857.1722620088; _gid=GA1.2.1026249312.1722620088; _ga_MHSNPJKWC7=GS1.2.1722620088.1.1.1722620128.0.0.0; session=53616c7465645f5f044b3ea6cc4c731a941482de5e7a058a039f3998ffb77344b2d632bbcefa7c7c65f09f51d71846387d1abf5e9506c8e9fb440562565abac5'}
# both 'x-test' and 'x-test2' are sent
nice_or_naughty = req.get('https://adventofcode.com/2015/day/5/input', headers=header).content.decode('UTF-8')

nice_str_count = 0
nice_str_array = []
naughty_str_array = []
for str_in_question in nice_or_naughty.splitlines():
    first_criteria = two_pairs(str_in_question.lower())
    second_criteria = letter_in_between_letters(str_in_question.lower())
    
    if first_criteria and second_criteria:
        nice_str_count = nice_str_count + 1
        nice_str_array.append(str_in_question.lower())
    else:
        naughty_str_array.append(str_in_question.lower())

print(nice_str_count)

'''f = open("checkstrings.txt", "a")
for string in naughty_str_array:
    f.write(string + '\n')
f.close()'''