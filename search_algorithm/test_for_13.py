from search import simple_search
def open_data(path) -> list:

    with open(path) as data:
        return [int(i) for i in data.readline().split()]
    
def main():
    DATA = open_data('data.txt')

    try:
        
        res = simple_search(DATA, int(input("Enter the value to searh: ")))
        print(res if res != None else "Not found")
        
    except ValueError:
        print('Incorrect enter value')



if __name__ == "__main__":
    main()
