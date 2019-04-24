import keyboard
from time import sleep

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# координаты епта
coordinates = {
    0: (5, 2),
    1: (4, 2),
    2: (3, 2),
    3: (2, 2),
    4: (1, 2),
}

# поле 6х6
y = 6
x = 6

# направление змейки
direction = 'up'  # пусть по уполчанию двигается вверх


print(coordinates)

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def move_after_head(current_head_position):
    for i in range(len(coordinates) - 1, -1, -1):
        if i != 0:
            coordinates[i] = coordinates[i - 1]
    coordinates[1] = current_head_position


def move_up():
    global direction
    if direction != 'down':
        current_head_position = coordinates[0]
        new_head_position = (coordinates[0][0], coordinates[0][1] + 1)
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'up'
        print(coordinates)


def move_down():
    global direction
    if direction != 'up':
        current_head_position = coordinates[0]
        new_head_position = (coordinates[0][0], coordinates[0][1] - 1)
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'down'
        print(coordinates)


def move_left():
    global direction
    if direction != 'right':
        current_head_position = coordinates[0]
        new_head_position = (coordinates[0][0] - 1, coordinates[0][1])
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'left'
        print(coordinates)


def move_right():
    global direction
    if direction != 'left':
        current_head_position = coordinates[0]
        new_head_position = (coordinates[0][0] + 1, coordinates[0][1])
        if collision(new_head_position):  # т.к. мы уже записали новую координату головы, берем прямо оттуда
            print('Game over epta.')
            exit(0)
        coordinates[0] = new_head_position
        move_after_head(current_head_position)
        direction = 'right'
        print(coordinates)


def collision(new_head_position):  # возвращает True, если координаты головы змейки равны координатам любой части тела
    # print(coordinates.values())
    for coordinate in coordinates.values():
        if new_head_position == coordinate:
            print(f'координата {coordinate} равна голове змейки {new_head_position}')
            return True
    return False


keyboard.add_hotkey('Ctrl + Up', move_up)
keyboard.add_hotkey('Ctrl + Down', move_down)
keyboard.add_hotkey('Ctrl + Left', move_left)
keyboard.add_hotkey('Ctrl + Right', move_right)
keyboard.wait('Ctrl + Q')
