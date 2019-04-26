import keyboard
import tkinter as tk
from time import sleep
from threading import Thread
from random import randint

import snake_logic as sl
import gridder
import consts

grid_coordinates = gridder.create_grid(canvas_height=consts.CANVAS_HEIGHT, grid_width=consts.GRID_WIDTH, grid_height=consts.GRID_HEIGHT)


def update_grid():
    for l_coordinate in sl.snake_coordinates.values():
        canvas.create_rectangle(grid_coordinates[l_coordinate], fill='#ff0000')
    if sl.apple_coordinates:
        draw_apple()


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

        if sl.eats_apple():
            draw_apple()
            label_score.configure(text=f'Score: {sl.score}')
            snake_size_label.configure(text=f'Size: {len(sl.snake_coordinates)}')
        sleep(consts.DELAY)


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


def draw_apple():
    canvas.create_rectangle(grid_coordinates[sl.apple_coordinates], fill='#00ff00')


def start():
    sl.generate_apple()
    draw_apple()
    Thread(target=continue_moving, daemon=True).start()


keyboard.add_hotkey('Up', move_up)
keyboard.add_hotkey('Down', move_down)
keyboard.add_hotkey('Left', move_left)
keyboard.add_hotkey('Right', move_right)


if __name__ == '__main__':
    root = tk.Tk()
    canvas = tk.Canvas(root, height=consts.CANVAS_HEIGHT, width=consts.CANVAS_WIDTH)
    root.title(consts.NAME)
    root.resizable(False, False)

    label_score = tk.Label(text='Score: 0', bg='#24252A', fg='#ffffff')
    label_score.pack()

    snake_size_label = tk.Label(text=f'Size: {len(sl.snake_coordinates)}', bg='#24252A', fg='#ffffff')
    snake_size_label.pack()

    for coordinate in grid_coordinates.values():
        canvas.create_rectangle(coordinate, fill='#ffffff')
    update_grid()
    canvas.pack()

    start()
    root.mainloop()
