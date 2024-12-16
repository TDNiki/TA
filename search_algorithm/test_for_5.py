from search import binary_search_one, binary_search_all

from test_for_13 import open_data

try:
    data = sorted(open_data('data.txt'))
    print(data)
    res = binary_search_one(data, int(input('Enter the value to find: ')))
    print(res if res != None else 'Not found')
except ValueError:
    print('Incorrect enter value')