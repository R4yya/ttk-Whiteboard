import tkinter as tk
from tkinter import ttk
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

        self.style = ttk.Style()
        self.style.configure('TButton',
                             padding=6,
                             relief='flat',
                             background='#ccc')

        self.color_button = ttk.Button(root,
                                       text='Choose color',
                                       command=self.choose_color_on_button)
        self.color_button.pack(side=tk.LEFT, padx=10)

        self.radius_label = ttk.Label(root, text=f'Brush size: {self.whiteboard_canvas.brush_radius}')
        self.radius_label.pack(side=tk.LEFT, padx=10)

    def choose_color_on_canvas(self, event):
        color = askcolor(title='Выберите цвет')[1]
        if color:
            self.whiteboard_canvas.line_color = color

    def choose_color_on_button(self):
        color = askcolor(title='Выберите цвет')[1]
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

        self.radius_label.config(text=f'Brush size: {self.whiteboard_canvas.brush_radius}')

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
