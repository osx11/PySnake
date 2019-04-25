import keyboard
from time import sleep

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# координаты епта
snake_coordinates = {
    0: (8, 2),
    1: (7, 2),
    2: (6, 2),
    3: (5, 2),
    4: (4, 2),
    5: (3, 2),
    6: (2, 2),
    7: (1, 2),
}

# размеры поля
edge_y = 28
edge_x = 28

# направление змейки
direction = 'right'  # пусть по уполчанию двигается вверх

tail_coordinates = snake_coordinates[len(snake_coordinates) - 1]


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def move_after_head(current_head_position):
    for i in range(len(snake_coordinates) - 1, -1, -1):
        if i != 0:
            snake_coordinates[i] = snake_coordinates[i - 1]
    snake_coordinates[1] = current_head_position


def move_up():
    global direction, tail_coordinates
    if direction != 'down':
        tail_coordinates = snake_coordinates[len(snake_coordinates) - 1]
        current_head_position = snake_coordinates[0]
        new_head_position = (snake_coordinates[0][0], snake_coordinates[0][1] + 1)
        if field_edge(new_head_position):
            new_head_position = (snake_coordinates[0][0], 0)
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        snake_coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'up'
        # print(snake_coordinates)


def move_down():
    global direction, tail_coordinates
    if direction != 'up':
        tail_coordinates = snake_coordinates[len(snake_coordinates) - 1]
        current_head_position = snake_coordinates[0]
        new_head_position = (snake_coordinates[0][0], snake_coordinates[0][1] - 1)
        if field_edge(new_head_position):
            new_head_position = (snake_coordinates[0][0], edge_y)
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        snake_coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'down'
        # print(snake_coordinates)


def move_left():
    global direction, tail_coordinates
    if direction != 'right':
        tail_coordinates = snake_coordinates[len(snake_coordinates) - 1]
        current_head_position = snake_coordinates[0]
        new_head_position = (snake_coordinates[0][0] - 1, snake_coordinates[0][1])
        if field_edge(new_head_position):
            new_head_position = (edge_x, snake_coordinates[0][1])
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        snake_coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'left'
        # print(snake_coordinates)


def move_right():
    global direction, tail_coordinates
    if direction != 'left':
        tail_coordinates = snake_coordinates[len(snake_coordinates) - 1]
        current_head_position = snake_coordinates[0]
        new_head_position = (snake_coordinates[0][0] + 1, snake_coordinates[0][1])
        if field_edge(new_head_position):
            new_head_position = (0, snake_coordinates[0][1])
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        snake_coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'right'
        # print(snake_coordinates)


def collision(new_head_position):  # возвращает True, если координаты головы змейки равны координатам любой части тела
    for coordinate in snake_coordinates.values():
        if new_head_position == coordinate:
            return True
    return False


def field_edge(new_head_position):  # возвращает True, если координата головы по x или y равна границам поля
    return True if new_head_position[0] > edge_x or new_head_position[0] < 0 or new_head_position[1] > edge_y or new_head_position[1] < 0 else False


# keyboard.add_hotkey('Ctrl + Up', move_up)
# keyboard.add_hotkey('Ctrl + Down', move_down)
# keyboard.add_hotkey('Ctrl + Left', move_left)
# keyboard.add_hotkey('Ctrl + Right', move_right)
# keyboard.wait('Ctrl + Q')
