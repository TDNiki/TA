

class Labirint:

    lab: list = list()

    def __init__(self, path_to_txt_lab: str, start_cords: tuple, finish_cords: tuple):
        with open(path_to_txt_lab, 'r') as txt:
            for line in txt.readlines():
                row = [0 if i == " " else -1 for i in line.strip('\n')]
                self.lab.append(row)
        
        self._width = len(self.lab[0])
        self._height = len(self.lab)
        self._finish = finish_cords
        self.start = start_cords
        self.lab[start_cords[0]][start_cords[1]] = 1
    

    def printLab(self):
        for line in self.lab:
            for i in line:
                print("%3d" % i, end = ' ')
            print()
    
    def printResult(self, lab: list):
        for line in lab:
            for i in line:
                print("%3d" % i, end = ' ')
            print()



    def search_exist(self):
        step = 1
        lab = self.lab.copy()

        for i in range(self._height * self._width):
            step += 1
            for y in range(self._height):
                for x in range(self._width):
                    if lab[y][x] == step - 1:
                        if y > 0 and lab[y - 1][x] == 0:
                            lab[y - 1][x] = step
                        if y < self._height - 1 and lab[y + 1][x] == 0:
                            lab[y + 1][x] = step
                        if x > 0 and lab[y][x - 1] == 0:
                            lab[y][x - 1] = step
                        if x < self._width - 1 and lab[y][x + 1] == 0:
                            lab[y][x + 1] = step
                        if (y, x) == self._finish:
                            
                            return True, lab
                        
        return False, lab
    
    def way(self, lab_exist: list):
        row, col = self._finish
        step = lab_exist[row][col]
        result = [0] * (step + 1)
        while (step > 0):
            result[step] = [row, col]
            step -= 1

            if row > 0 and lab_exist[row - 1][col] == step:
                row -= 1
            elif row < self._height - 1 and lab_exist[row + 1][col] == step:
                row += 1
            elif col > 0 and lab_exist[row][col - 1] == step:
                col -= 1
            elif col < self._width - 1 and lab_exist[row][col + 1] == step:
                col += 1
        
        return result[1:]

    
        
"""a = Labirint("labirint2.txt", (4, 0), (9,0))
a.printLab()
print('\n\n')
work_lab = a.search_exist()
print(a.way(work_lab[1]))"""
a =  {'e2': 2}
a.remove("e2")