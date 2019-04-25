# https://hastebin.com/inorojuruy.py

import keyboard
import tkinter as tk
from time import sleep
import threading

from src import snake_logic as sl
from src import gridder

NAME = 'PySnake'
WIDTH = 600
HEIGHT = 600


# возвращает словарь, в котором ключи являются нормальными координатами (x, y),
# а значения - ебанутые координаты для дальнейшего рисования пикселей 20х20.
# В дальнейшем можно перекрашивать/рисовать квадраты 20х20 методом
# canvas.create_rectangle(grid_coordinates[(x, y)])
#
# высота поля, количество квадратов по x и y могут быть произвольными

grid_coordinates = gridder.create_grid(canvas_height=HEIGHT, grid_width=29, grid_height=29)


def update_grid():
    for l_coordinate in sl.snake_coordinates.values():
        canvas.create_rectangle(grid_coordinates[l_coordinate], fill='#ff0000')


def continue_moving():
    while True:
        if sl.direction == 'up':
            move_up()
        elif sl.direction == 'down':
            move_down()
        elif sl.direction == 'left':
            move_left()
        elif sl.direction == 'right':
            move_right()
        sleep(0.5)


def move_up():
    canvas.create_rectangle(grid_coordinates[sl.tail_coordinates], fill='#ffffff')
    sl.move_up()
    update_grid()


def move_down():
    canvas.create_rectangle(grid_coordinates[sl.tail_coordinates], fill='#ffffff')
    sl.move_down()
    update_grid()


def move_left():
    canvas.create_rectangle(grid_coordinates[sl.tail_coordinates], fill='#ffffff')
    sl.move_left()
    update_grid()


def move_right():
    canvas.create_rectangle(grid_coordinates[sl.tail_coordinates], fill='#ffffff')
    sl.move_right()
    update_grid()


def start():
    for i in range(3, -1, -1):
        print(f'Starting in {i}...')
        sleep(1)
    threading.Thread(target=continue_moving, daemon=True).start()


# keyboard.add_hotkey('Ctrl + Alt', start)
keyboard.add_hotkey('Up', move_up)
keyboard.add_hotkey('Down', move_down)
keyboard.add_hotkey('Left', move_left)
keyboard.add_hotkey('Right', move_right)


if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    root.title(NAME)
    root.resizable(False, False)

    for coordinate in grid_coordinates.values():
        canvas.create_rectangle(coordinate, fill='#ffffff')
    update_grid()
    canvas.pack()

    start()
    root.mainloop()
