import time
import sort
from random import randint
PATH = 'data.txt'
data: list

def import_file():
    with open(PATH, 'r') as data:
        return [int(i) for i in data.readline().split()]

def generate_random(a: int, b: int, count: int) -> None:
    """RETURNS: file with random int values. \n
    FORMAT: sep =  'SPACE', in line"""
    with open(PATH, 'w') as f:
        f.write(' '.join((str(randint(a, b)) for i in range(count))))

def check_sort(data: list) -> bool:
    """RETURNS: True - if correct | Else - if not"""
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]: return False
    
    return True
    
generate_random(-1000, 1000, 10000)
data = import_file()
start = time.time()
sorted_data = sort.count_sort(data, min(data), max(data))
end = time.time()

print('count:', end - start, check_sort(sorted_data))

start = time.time()
sorted_data = sort.bubble_sort(data)
end = time.time()

print('buble', end - start, check_sort(sorted_data))


start = time.time()
sorted_data = sorted(data)
end = time.time()

print('in-lib', end - start)