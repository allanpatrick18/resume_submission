

def compare_nodes(dict_words: dict, start: str, end: str) -> str:
    """
    Compare which is higher or lower
    :param dict_words: {A:B,C:D,D:C}
    :param start: str ex: A
    :param end: str ex: C
    :return: str
    ex:'>' or '<'
    """
    if start not in dict_words:
        dict_words[start] = None

    if end not in dict_words:
        dict_words[end] = None

    new_start = end
    new_end = start
    count = 0
    while count <= dict_words.__len__():
        if new_start is not None:
            new_start = dict_words[new_start]
        if new_end is not None:
            new_end = dict_words[new_end]
        if new_start == start:
            return '<'
        if new_end == end:
            return '>'
        count += 1

    return '?'


def create_matrix(puzzle: str):
    """
    Create the matrix from string puzzle
    :param puzzle: str
    :return: matrix[][], dict, symbols
    """
    matrix = []
    symbols = ['A', 'B', 'C', 'D']
    tree = dict()
    puzzle_array = list(puzzle.split(':')[1].replace(' ', '').replace('\n', ''))
    puzzle_array.insert(0, ' ')
    index = 0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(puzzle_array[index])
            if puzzle_array[index] == '>':
                tree[symbols[i-1]] = symbols[j-1]
            elif puzzle_array[index] == '<':
                tree[symbols[j-1]] = symbols[i-1]
            index += 1
        matrix.append(row)
    return matrix, tree, symbols


def solve_puzzle(puzzle: str):
    """
    This function will solve the puzzle
    :param puzzle: str
    ex:
    'Please solve this puzzle:
     ABCD
    A=---
    B<---
    C--->
    D>---'
    :return: str
    ex:
     ABCD
    A=><<
    B<=<<
    C>>=>
    D>><=
    """
    matrix, tree, symbols = create_matrix(puzzle)
    str_matrix = ''
    for i in range(0, 5):
        for j in range(0, 5):
            if matrix[i][j] == '-' and i != j:
                matrix[i][j] = compare_nodes(tree, symbols[i-1], symbols[j-1])
            if i == j and i != 0:
                matrix[i][j] = '='
            str_matrix += matrix[i][j]
        str_matrix += '\n'
    return str_matrix





