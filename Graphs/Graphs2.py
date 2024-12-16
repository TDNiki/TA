from collections import deque




def import_matrix(path: str):
    matrix = list()

    with open(path, 'r') as file:
        for line in file.readlines():
            matrix.append([int(i) for i in line.split()])
    
    return matrix


class Seadep:
    """Search in depth"""

    matrix: list[list]
    __visited: list
    __prev: list
    start: int


    def __init__(self, matrix: list[list], start: int = 0):
        self.matrix = matrix
        self.__visited = [False] * (len(matrix) + 1)
        self.__prev = [None] * (len(matrix) + 1)
        self.start = start
        self.__dfs(start)
    
    def is_way(self, finish: int ) -> bool:
        if self.__visited[finish]: return True
        return False
    
    def show_way_to_b(self, finish: int) -> list | None:
        step = finish
        if self.__visited[step]:
            way = [step]
            while step != self.start:
                way.append(self.__prev[step])
                step = self.__prev[step]

            way.reverse()
            return way

    def __dfs(self, start):
        self.__visited[start] = True
        for road in self.matrix[start]:
            if not self.__visited[road]:
                self.__prev[road] = start
                self.__dfs(road)

    def get_ncomp(self) -> int:
        nComp = 1
        visit  = self.__visited
        for i in range(len(visit)- 1):
            if not visit[i]:
                nComp += 1
                self.__dfs_com(visit, i)

        return nComp
    
    def __dfs_com(self, visit_matrix: list, start):
        visit_matrix[start] = True
        for round in self.matrix[start]:
            if not visit_matrix[round]:
                self.__dfs_com(visit_matrix, round)

    
class Seawid:
    """Search in width"""

    def __init__(self, matrix: list):
        self.matrix = matrix

    def min_road(self, start_v: int, finish_v: int) -> int:
        """:RETURNS: The minimum value of the vertices of the graph. If there's no roads to finish v, returns 0"""

        v_count = [None] * self.matrix.__len__()
        q = deque()
        road = [None] * self.matrix.__len__()
        q.append(start_v)
        v_count[0] = 0
        
        while q:

            current_v = q.popleft()
            for v in self.matrix[current_v]:
                if v_count[v] is None:
                    v_count[v] = v_count[current_v] + 1
                    q.append(v)
                    road[v] = current_v

        return v_count[finish_v], ' --> '.join((str(i) for i in self.__road_to(road, finish_v)))
    
    def __road_to(self, road: list, finish_v: int) -> deque:
        res = deque()

        current = finish_v
        while current is not None:
            res.appendleft(current)
            current = road[current]
        
        return res




test_data = import_matrix('matrix.txt')
attr = Seawid(test_data)
result = attr.min_road(0, 7)
print(result) if result[0] != None else print('Not found')



        


