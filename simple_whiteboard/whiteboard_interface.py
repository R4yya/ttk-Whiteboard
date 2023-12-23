import tkinter as tk
from whiteboard_canvas import WhiteboardCanvas
from whiteboard_controls import WhiteboardControls


class WhiteboardInterface:
    def __init__(self, root):
        self.whiteboard_canvas = WhiteboardCanvas(root)
        self.whiteboard_controls = WhiteboardControls(root,
                                                      self.whiteboard_canvas)

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(
            label='Save As',
            command=self.whiteboard_controls.save_board,
            accelerator='Ctrl+S'
        )

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='Edit', menu=edit_menu)
        edit_menu.add_command(
            label='Undo',
            command=self.whiteboard_controls.undo_last_action,
            accelerator='Ctrl+Z'
        )
