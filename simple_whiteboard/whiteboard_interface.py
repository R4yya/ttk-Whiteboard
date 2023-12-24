import tkinter as tk
from tkinter import ttk
from whiteboard_canvas import WhiteboardCanvas
from whiteboard_controls import WhiteboardControls


class WhiteboardInterface:
    def __init__(self, root):
        self.root = root
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=tk.YES, fill=tk.BOTH)

        self.create_new_whiteboard()

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(
            label='Add New',
            command=self.create_new_whiteboard,
            accelerator='Ctrl+N'
        )
        file_menu.add_command(
            label='Save As',
            command=self.current_whiteboard_controls.save_board,
            accelerator='Ctrl+S'
        )

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(
            label='Undo',
            command=self.current_whiteboard_controls.undo_last_action,
            accelerator='Ctrl+Z'
        )

        self.root.bind('<Control-n>', self.create_new_whiteboard)

    def create_new_whiteboard(self, event=None):
        whiteboard_frame = ttk.Frame(self.notebook)
        whiteboard_frame.pack(expand=tk.YES, fill=tk.BOTH)

        canvas = WhiteboardCanvas(whiteboard_frame)
        controls = WhiteboardControls(
            whiteboard_frame,
            canvas,
            self.notebook
        )
        canvas.controls = controls

        self.notebook.add(
            whiteboard_frame,
            text=f'Board {self.notebook.index("end") + 1}'
        )
        self.notebook.select(whiteboard_frame)
        self.current_whiteboard_controls = controls
