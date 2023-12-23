import tkinter as tk
from tkinter.colorchooser import askcolor


class WhiteboardControls(object):
    def __init__(self, root, whiteboard_canvas):
        self.whiteboard_canvas = whiteboard_canvas

        self.whiteboard_canvas.canvas.bind('<Button-3>',
                                           self.choose_color_on_canvas)

        self.whiteboard_canvas.canvas.bind('<MouseWheel>',
                                           self.change_brush_size)

        self.whiteboard_canvas.canvas.bind('<Button-1>',
                                           self.start_paint)
        self.whiteboard_canvas.canvas.bind('<B1-Motion>',
                                           self.paint)

    def choose_color_on_canvas(self, event):
        color = askcolor(title='Choose color')[1]
        if color:
            self.whiteboard_canvas.line_color = color

    def change_brush_size(self, event):
        if event.delta > 0:
            self.whiteboard_canvas.brush_radius = min(
                self.whiteboard_canvas.max_brush_radius,
                self.whiteboard_canvas.brush_radius + 1
            )
        else:
            self.whiteboard_canvas.brush_radius = max(
                self.whiteboard_canvas.min_brush_radius,
                self.whiteboard_canvas.brush_radius - 1
            )

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

        self.whiteboard_canvas.canvas.create_line(
            self.last_x,
            self.last_y,
            x,
            y,
            fill=self.whiteboard_canvas.line_color,
            width=1 * self.whiteboard_canvas.brush_radius,
            capstyle=tk.ROUND
        )

        self.last_x = x
        self.last_y = y
