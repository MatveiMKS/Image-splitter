from image_splitter import split_image_into_grid, save_grid_squares

def main():
    image_path = "test image.png"
    grid_size = (3, 30)
    output_dir = "test folder"
    save_grid_squares(split_image_into_grid(image_path, grid_size), output_dir)

if __name__ == "__main__":
    main()
