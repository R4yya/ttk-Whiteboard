from tkinter.colorchooser import askcolor
import keyboard


class WhiteboardControls(object):
    def __init__(self, root, whiteboard_canvas):
        self.whiteboard_canvas = whiteboard_canvas
        self.root = root

        self.whiteboard_canvas.canvas.bind('<Button-3>',
                                           self.choose_color_on_canvas)

        self.whiteboard_canvas.canvas.bind('<MouseWheel>',
                                           self.change_brush_size)

        self.whiteboard_canvas.canvas.bind('<Button-1>',
                                           self.start_paint)
        self.whiteboard_canvas.canvas.bind('<B1-Motion>',
                                           self.paint)

        keyboard.add_hotkey('ctrl+z', self.undo_last_action)

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
        self.whiteboard_canvas.add_new_line_to_history()
        self.whiteboard_canvas.start_paint(event)

    def paint(self, event):
        self.whiteboard_canvas.paint(event)

    def undo_last_action(self):
        self.whiteboard_canvas.undo_last_action()
