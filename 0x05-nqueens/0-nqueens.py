#!/usr/bin/python3
"""
This module solves the N queens problem.
"""
import sys


def validate_args():
    """
    Validates the command line arguments.
    Exits with a status of 1 if the arguments are invalid.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_safe(board, row, col):
    """
    Checks if it's safe to place a queen at board[row][col].
    Returns True if it's safe, otherwise False.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col, solutions):
    """
    Solves the N queens problem using backtracking.
    Appends each valid solution to the solutions list.
    """
    if col >= len(board):
        solutions.append(
                [
                    [r, c]
                    for r in range(len(board))
                    for c in range(len(board))
                    if board[r][c] == 1
                ]
        )
        return
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens(board, col + 1, solutions)
            board[i][col] = 0


def main():
    """
    Main function to solve the N queens problem.
    """
    n = validate_args()
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
