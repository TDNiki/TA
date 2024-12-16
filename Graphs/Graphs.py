#from ..search_algorithm.search import binary_search_one


def import_matrix(path: str):
    matrix = list()

    with open(path, 'r') as matrix_data:
        for col in matrix_data.readlines():
            matrix.append([int(i) for i in col.replace('\n', '')])
    
    return matrix

def get_adjacency_matrix(matrix: list):
    """List adjacency of matrix"""
    res = list()
    for col in matrix:
        res.append([i for i in range(len(col)) if col[i]])
    
    return res
def get_matrix_from_adj(adj_matrix: list):
    matrix = [list(0 for j in range(len(adj_matrix))) for i in range(len(adj_matrix))]
    for row_index in range(len(adj_matrix)):
        for col_index in range(len(adj_matrix[row_index])):
            matrix[row_index][adj_matrix[row_index][col_index]] = 1

    return matrix
            
def export_matrix(path: str, matrix: list):
    """Export matrix to the file"""
    with open(path, 'w') as matrix_data:
        matrix_data.write(str(len(matrix)) + '\n')
        for col in matrix:
            for val in col:
                matrix_data.write(str(val) + ' ')
            matrix_data.write('\n')
            

def get_edge(path: str):
    """Get edge by matrix"""
    data = import_matrix(path)
    res = list()
    for col_index in range(len(data)):
        for row_index in range(len(data[col_index])):
            if data[col_index][row_index] and (row_index, col_index) not in res:
                res.append((col_index, row_index))

    return res

def get_matrix_from_edges(edges_list: list):
    """Gets matrix from edges list"""
    max_ = max(max(edges_list)) + 1
    matrix = list([[0 for j in range(max_)] for i in range(max_)]) 
    for i in edges_list:
        matrix[i[0]][i[1]] = 1
        matrix[i[1]][i[0]] = 1

    return matrix

def export_edge(path: str, edges: list):
    """Export the edges to file"""
    with open(path, 'w') as matrix_data:
        vert = len(edges)
        matrix_data.write(str(vert - 1) + ' ' + str(vert) + '\n')
        for col in edges:
            for val in col:
                matrix_data.write(str(val) + ' ')
            matrix_data.write('\n')
    
imported = import_matrix('data.txt')
ad_matrix = get_adjacency_matrix(imported)
print(ad_matrix)
export_matrix('output.txt', ad_matrix)
edges = get_edge('data.txt')
print(edges)
export_edge('effe.txt', edges)
rever_matrix = get_matrix_from_adj(ad_matrix)
print(rever_matrix)
export_matrix('output_matrix.txt', rever_matrix)
print(get_matrix_from_edges(edges))

        

            
        
