#!/usr/bin/env python3
"""
The program should print every possible
solution to the problem
"""
import sys


def print_usage_and_exit():
    """
    It prints usage and exit
    """
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """
    Prints number of n-queens
    """
    print("N must be a number")
    sys.exit(1)


def print_value_error_and_exit():
    """
    Checks value of n-queens
    """
    print("N must be at least 4")
    sys.exit(1)


def is_valid(board, row, col):
    """
    The program should print every possible
    solution to the problem
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """
    The program should print every possible
    solution to the problem
    """
    def solve(board, row):
        """
        Solves the board and row
        """
        if row == n:
            solutions.append([[i, board[i]] for i in range(n)])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                solve(board, row + 1)

    solutions = []
    board = [-1] * n
    solve(board, 0)
    return solutions


def main():
    """
    The program should print every possible
    solution to the problem.
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()
    try:
        n = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()
    if n < 4:
        print_value_error_and_exit()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
