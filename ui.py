import tkinter as tk
from tkinter import filedialog, messagebox
from image_splitter import split_image_into_grid, save_grid_squares, add_margin

def create_ui():
    """
    Creates the user interface for the image splitter application.
    """
    def browse_file():
        filename = filedialog.askopenfilename()
        file_path_entry.delete(0, tk.END)
        file_path_entry.insert(tk.END, filename)
        validate_inputs()

    def browse_directory():
        directory = filedialog.askdirectory()
        output_dir_entry.delete(0, tk.END)
        output_dir_entry.insert(tk.END, directory)
        validate_inputs()

    def validate_inputs():
        """
        Validates if all required fields are filled and enables/disables the Split Image button.
        """
        if (file_path_entry.get() and columns_entry.get().isdigit() and rows_entry.get().isdigit() and output_dir_entry.get()):
            split_button.config(state=tk.NORMAL)
        else:
            split_button.config(state=tk.DISABLED)

    def set_margin_color(color_hex):
        """
        Sets the margin color entry field with the specified HEX color code.
        """
        margin_color_entry.delete(0, tk.END)
        margin_color_entry.insert(tk.END, color_hex)

    def split_image():
        image_path = file_path_entry.get()
        grid_size = (int(columns_entry.get()), int(rows_entry.get()))
        output_dir = output_dir_entry.get()
        add_margin_flag = margin_var.get()
        margin_size = int(margin_size_entry.get()) if add_margin_flag else 0
        margin_color = margin_color_entry.get() if add_margin_flag else None

        grid_squares = split_image_into_grid(image_path, grid_size)
        
        if add_margin_flag:
            grid_squares = [add_margin(square, margin_size, margin_color) for square in grid_squares]

        save_grid_squares(grid_squares, output_dir)

        messagebox.showinfo("Status", "Process finished")

    root = tk.Tk()

    tk.Label(root, text="Image Path").grid(row=0)
    file_path_entry = tk.Entry(root)
    file_path_entry.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=(10, 10))

    tk.Label(root, text="Columns").grid(row=1)
    columns_entry = tk.Entry(root)
    columns_entry.grid(row=1, column=1)
    columns_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    tk.Label(root, text="Rows").grid(row=2)
    rows_entry = tk.Entry(root)
    rows_entry.grid(row=2, column=1)
    rows_entry.bind("<KeyRelease>", lambda event: validate_inputs())

    tk.Label(root, text="Output Directory").grid(row=3)
    output_dir_entry = tk.Entry(root)
    output_dir_entry.grid(row=3, column=1)
    tk.Button(root, text="Browse", command=browse_directory).grid(row=3, column=2, padx=(10, 10))

    margin_var = tk.IntVar()
    tk.Checkbutton(root, text="Add Margin", variable=margin_var).grid(row=4, column=0, columnspan=3)
    
    def toggle_margin_options():
        state = tk.NORMAL if margin_var.get() else tk.DISABLED
        margin_size_label.grid_remove() if state == tk.DISABLED else margin_size_label.grid()
        margin_size_entry.grid_remove() if state == tk.DISABLED else margin_size_entry.grid()
        margin_color_label.grid_remove() if state == tk.DISABLED else margin_color_label.grid()
        margin_color_entry.grid_remove() if state == tk.DISABLED else margin_color_entry.grid()
        for button in color_buttons:
            button.grid_remove() if state == tk.DISABLED else button.grid()

    margin_var.trace_add("write", lambda *args: toggle_margin_options())

    margin_size_label = tk.Label(root, text="Margin Size")
    margin_size_label.grid(row=5, column=0)
    margin_size_entry = tk.Entry(root)
    margin_size_entry.grid(row=5, column=1)

    margin_color_label = tk.Label(root, text="Margin Color (HEX)")
    margin_color_label.grid(row=6, column=0)
    margin_color_entry = tk.Entry(root)
    margin_color_entry.grid(row=6, column=1)

    color_buttons = [
        tk.Button(root, bg="#000000", width=5, command=lambda: set_margin_color("#000000")),
        tk.Button(root, bg="#FFFFFF", width=5, command=lambda: set_margin_color("#FFFFFF")),
        tk.Button(root, bg="#FF0000", width=5, command=lambda: set_margin_color("#FF0000")),
        tk.Button(root, bg="#FFFF00", width=5, command=lambda: set_margin_color("#FFFF00")),
        tk.Button(root, bg="#00FF00", width=5, command=lambda: set_margin_color("#00FF00")),
        tk.Button(root, bg="#0000FF", width=5, command=lambda: set_margin_color("#0000FF")),
    ]

    color_buttons[0].grid(row=7, column=0)
    color_buttons[1].grid(row=7, column=1)
    color_buttons[2].grid(row=7, column=2)
    color_buttons[3].grid(row=8, column=0)
    color_buttons[4].grid(row=8, column=1)
    color_buttons[5].grid(row=8, column=2)

    toggle_margin_options()

    split_button = tk.Button(root, text="Split Image", command=split_image, state=tk.DISABLED)
    split_button.grid(row=9, column=1)

    root.mainloop()
