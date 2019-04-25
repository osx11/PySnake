def create_grid(canvas_height, grid_width, grid_height):
    l_grid_coordinates = {}

    y1 = canvas_height-30
    y2 = canvas_height-10

    for y in range(grid_height):
        x1 = 10
        x2 = 30
        for x in range(grid_width):
            l_coordinate = x1, y1, x2, y2
            l_grid_coordinates[(x, y)] = l_coordinate
            x1 += 20
            x2 += 20
        y1 -= 20
        y2 -= 20

    return l_grid_coordinates
