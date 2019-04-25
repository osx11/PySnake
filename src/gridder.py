def create_grid(canvas_width, canvas_height, grid_width, grid_height, pixel_side):
    grid_coordinates = {}
    x1 = 10
    x2 = pixel_side+10
    for i in range(grid_width):
        coordinate = x1, canvas_height-30, x2, canvas_height-10
        grid_coordinates[(0, i)] = coordinate
        x1 += 20
        x2 += 20
    return grid_coordinates
