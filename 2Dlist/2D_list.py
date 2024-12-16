from random import randint


class D2_list:
    
    @staticmethod
    def generate_2dList(random_range: tuple[int, int], size: tuple[int, int]) -> list[list[int]]:
        """Generate 2D list"""
        res = list()
        for _ in range(size[0]):
            res.append([randint(*random_range) for i in range(size[1])])

        return res
    
    @staticmethod
    def sum_list(d2_list: list[list]) -> tuple[int, int]:

        negative = positive = 0
        for i in d2_list:
            for j in i:
                if j < 0: 
                    negative += j 
                else: 
                    positive += j
        
        return negative, positive
    

    @staticmethod
    def sum_border(d2_list: list[list]) -> int:
        
        sum_ = 0

        for i in [0, -1]:
            for j in range(len(d2_list)):
                sum_ += d2_list[j][i]

        return sum_ + sum(d2_list[0]) + sum(d2_list[-1])
    
    @staticmethod
    def sum_inbox(d2_list):
        sum_ = 0
        for i in range(1, len(d2_list) - 1):
            for j in range(1, len(d2_list[0]) - 1):
                sum_ += d2_list[i][j]

        return sum_
    
    @staticmethod
    def sum_dia(d2_list):
        sum_ = 0
        for i in range(len(d2_list)):
            sum_ += d2_list[i][i]

        return sum_
    
    @staticmethod
    def sum_dia_downup(d2_list):
        down = up = 0
        
        for i in range(len(d2_list) - 1):
            for j in range(i + 1, len(d2_list)):
                up += d2_list[i][j]


        for i in range(1, len(d2_list)):
            for j in range(i):
                down += d2_list[i][j]
        
        return up, down



        


list_ = D2_list.generate_2dList((-10, 10), (3, 3))
for i in range(len(list_)):
    print(*list_[i])
    
print('------------')
print(D2_list.sum_list(list_))
print('------------')
print(D2_list.sum_border(list_))
print('------------')
print(D2_list.sum_inbox(list_))
print('------------')
print(D2_list.sum_dia(list_))
print('------------')
print(D2_list.sum_dia_downup(list_))
