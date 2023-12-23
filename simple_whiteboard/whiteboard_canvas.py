import tkinter as tk


class WhiteboardCanvas(object):
    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.last_x = 0
        self.last_y = 0
        self.new_line = True
        self.line_color = 'black'
        self.min_brush_radius = 1
        self.max_brush_radius = 25
        self.brush_radius = 3
