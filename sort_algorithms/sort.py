

def bubble_sort(data: list) -> list:
    temp = data
    order = False
    while not order:
        order = True
        for i in range(len(temp) - 1):
            if temp[i] > temp[i + 1]:
                order = False
                temp[i], temp[i +1] = temp[i + 1], temp[i]
    
    return temp

def count_sort(data: list, min: int,  max: int):
    count_data = [0] * (max - min + 1)
    sorted_data = list()
    for i in data:
        count_data[i - min] += 1
    
    for i in range(len(count_data)):
        for j in range(count_data[i]):
            sorted_data.append(i + min)
    
    return sorted_data

