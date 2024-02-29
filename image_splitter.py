''' This script takes an image and splits it into a grid of smaller images. 
The grid size is specified as a tuple of two integers, 
where the first integer is the number of columns and the second integer is the number of rows. 
The script uses the Python Imaging Library (PIL) to open the image and crop it into grid squares. 
The grid squares are then saved as separate images in a new folder.
'''

import os
from PIL import Image

def split_image_into_grid(image_path: str, grid_size: tuple[int, int]) -> list[Image.Image]:
    '''grid_size: number of columns and rows in the grid.'''

    image = Image.open(image_path)
    width, height = image.size

    # Calculate the size of each grid square
    square_width = width // grid_size[0]
    square_height = height // grid_size[1]

    # Used to store the grid squares
    grid_squares = []

    for i in range(grid_size[1]):
        for j in range(grid_size[0]):
            # Calculate the coordinates of the current grid square
            left = j * square_width
            upper = i * square_height
            right = left + square_width
            lower = upper + square_height

            grid_square = image.crop((left, upper, right, lower))

            grid_squares.append(grid_square)

    return grid_squares


def save_grid_squares(grid_squares: list[Image.Image], output_folder: str) -> None:
    ''' This function saves each grid square as a separate image in the output folder.'''
    os.makedirs(output_folder, exist_ok=True)

    for i, grid_square in enumerate(grid_squares):
        output_path = os.path.join(output_folder, f"grid_square_{i}.png")
        grid_square.save(output_path)
