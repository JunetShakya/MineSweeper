from tkinter import *

MAXM = 100
MAXN = 100

dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
dy = [0, 0, 0, -1, -1, -1, 1, 1, 1]


def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m


def create_minesweeper_grid(window, rows, cols, reveal_callback, flag_callback):
    grid = []
    for i in range(rows):
        row = []
        for j in range(cols):
            button = Button(window, text='', width=4, height=2,
                            command=lambda x=i, y=j: reveal_callback(x, y))
            button.grid(row=i, column=j)
            row.append(button)
        grid.append(row)
    return grid


def update_cell_text(cell, value):
    cell.config(text=str(value))


def update_gui(grid, minesweeper_grid):
    rows = len(minesweeper_grid)
    cols = len(minesweeper_grid[0])
    for i in range(rows):
        for j in range(cols):
            cell_value = minesweeper_grid[i][j]
            button = grid[i][j]
            if cell_value == -1:  # Mine
                button.config(text='M')
            elif cell_value >= 0:  # Number
                update_cell_text(button, cell_value)


def main():
    window = Tk()
    window.title("Minesweeper")

    rows = 5
    cols = 5

    minesweeper_grid = [[0, 1, -1, 2, -1],
                        [1, 3, -1, 3, 1],
                        [-1, 2, -1, 3, -1],
                        [2, 3, 2, 0, 1],
                        [-1, 1, -1, 1, 0]]

    revealed_grid = [[False] * cols for _ in range(rows)]

    def reveal_cell(x, y):
        if not revealed_grid[x][y]:
            revealed_grid[x][y] = True
            update_cell_text(grid[x][y], minesweeper_grid[x][y])

    grid = create_minesweeper_grid(window, rows, cols, reveal_cell, None)

    update_button = Button(window, text="Update GUI", command=lambda: update_gui(grid, minesweeper_grid))
    update_button.grid(row=rows, columnspan=cols)

    window.mainloop()


if __name__ == "__main__":
    main()
