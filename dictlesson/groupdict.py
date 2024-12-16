PATH = 'group_data.txt'
group_dict = {}

def add_group(name: str, count: int = 0):
    if name in group_dict: raise KeyError(f"{name} группа уже в базе.")
    group_dict[name] = count

def delete_group(name: str):
    try:
        group_dict.pop(name)
    except KeyError:
        raise KeyError(f'Группы с названием {name} нет в базе.')

def edit_count(name: str, count: int):
    if name not in group_dict: raise KeyError(f'Группы с названием {name} нет в базе.')
    
    group_dict[name] = count

def import_file():
    with open(PATH, encoding = 'UTF-8') as data:
        for i in data.readlines():
            k, v = i.replace('\n', '').split(':')
            group_dict[k] = int(v)

def shut_down():
    with open(PATH, encoding = 'UTF-8', mode = 'w') as data:
        data.writelines((f'{k}:{v}\n' for k, v in group_dict.items()))

import_file()
while True:
    print(group_dict, end = '\n\n')
    try:
        selected = int(input('Menu. Select actions:\n 1. Add group\n 2. Edit group\n 3. Delete group\n 4. Exit\n\
Select one number: '))
        if selected == 1:
            name, count = input('Введите имя группы и число через пробел: ').split()
            add_group(name, int(count))
        elif selected == 2:
            name, count = input('Введите имя группы и число через пробел: ').split()
            edit_count(name, int(count))
        elif selected == 3:
            name = input('Введите имя группы: ')
            delete_group(name)
        elif selected == 4:
            shut_down()
            print(group_dict)
            break
        else: raise ValueError
    except KeyError as err:
        print(err)
    except ValueError:
        print('Введите корректные данные')

    print('----------------------')
    
        

    

