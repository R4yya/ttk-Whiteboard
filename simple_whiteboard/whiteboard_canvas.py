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

        self.history = []

    def start_paint(self, event):
        self.last_x = event.x
        self.last_y = event.y
        self.new_line = True

    def paint(self, event):
        x, y = event.x, event.y

        if self.new_line:
            self.last_x = x
            self.last_y = y
            self.new_line = False

        segment = self.canvas.create_line(
            self.last_x,
            self.last_y,
            x,
            y,
            fill=self.line_color,
            width=1 * self.brush_radius,
            capstyle=tk.ROUND
        )

        self.last_x = x
        self.last_y = y

        self.history[-1].append(segment)

    def add_new_line_to_history(self):
        self.history.append([])

    def undo_last_action(self):
        if self.history:
            segments = self.history.pop()
            for segment in segments:
                self.canvas.delete(segment)
