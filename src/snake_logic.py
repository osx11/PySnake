from random import randint
from src import consts

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

# направление змейки
direction = 'right'  # пусть по уполчанию двигается вверх

tail_coordinates = snake_coordinates[len(snake_coordinates) - 1]
apple_coordinates = None
score = 0

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
            new_head_position = (snake_coordinates[0][0], consts.GRID_HEIGHT-1)
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
            new_head_position = (consts.GRID_WIDTH-1, snake_coordinates[0][1])
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
    return True if new_head_position[0] > consts.GRID_WIDTH-1 or new_head_position[0] < 0 or new_head_position[1] > consts.GRID_HEIGHT-1 or new_head_position[1] < 0 else False


def generate_apple():
    global apple_coordinates
    apple_coordinates = randint(0, consts.GRID_HEIGHT), randint(0, consts.GRID_HEIGHT)


def eats_apple():
    global score
    if snake_coordinates[0] == apple_coordinates:
        score += 1
        generate_apple()
        return True
