import tkinter as tk
from tkinter import filedialog, messagebox
from image_splitter import split_image_into_grid, save_grid_squares

def create_ui():
    def browse_file():
        filename = filedialog.askopenfilename()
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(tk.END, filename)

    def browse_directory():
        directory = filedialog.askdirectory()
        output_dir_entry.delete(0, tk.END)
        output_dir_entry.insert(tk.END, directory)

    def split_image():
        image_path = file_path_entry.get()
        grid_size = (int(columns_entry.get()), int(rows_entry.get()))
        output_dir = output_dir_entry.get()

        grid_squares = split_image_into_grid(image_path, grid_size)
        save_grid_squares(grid_squares, output_dir)

        messagebox.showinfo("Status", "Process finished")

    root = tk.Tk()

    tk.Label(root, text="Image Path").grid(row=0)
    file_path_entry = tk.Entry(root)
    file_path_entry.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

    tk.Label(root, text="Columns").grid(row=1)
    columns_entry = tk.Entry(root)
    columns_entry.grid(row=1, column=1)

    tk.Label(root, text="Rows").grid(row=2)
    rows_entry = tk.Entry(root)
    rows_entry.grid(row=2, column=1)

    tk.Label(root, text="Output Directory").grid(row=3)
    output_dir_entry = tk.Entry(root)
    output_dir_entry.grid(row=3, column=1)
    tk.Button(root, text="Browse", command=browse_directory).grid(row=3, column=2)

    tk.Button(root, text="Split Image", command=split_image).grid(row=4, column=1)

    root.mainloop()
