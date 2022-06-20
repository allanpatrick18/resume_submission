from puzzle_solver import solve_puzzle


def test_puzzle():
    """This function will test solve puzzle"""
    _puzzle = """Please solve this puzzle:
     ABCD
    A=---
    B<---
    C--->
    D>---
    """

    matrix_str = solve_puzzle(_puzzle)
    assert 30 == len(list(matrix_str))

