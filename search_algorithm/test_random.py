from search import binary_search_all, simple_search
from time import time
from random import randint

data = sorted([randint(-100_000, 100_000) for i in range(100_000)])

while True:
    try:
        to_search = int(input('Enter the number:'))

        start = time()
        res = binary_search_all(data, to_search)
        end = time()

        """if res:
            print(data[res[0]])"""


        print(res, end - start)

        start = time()
        res = simple_search(data, to_search)
        end = time()
        print(res, end-start)
        
    except:
        print('Exists')
        break
