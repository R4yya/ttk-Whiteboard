from tkinter import filedialog
from tkinter.colorchooser import askcolor
from PIL import ImageGrab


class WhiteboardControls(object):
    def __init__(self, root, whiteboard_canvas, notebook):
        self.root = root
        self.whiteboard_canvas = whiteboard_canvas
        self.notebook = notebook
        self.active_canvas = None

        self.whiteboard_canvas.canvas.bind('<Button-3>',
                                           self.choose_color_on_canvas)

        self.whiteboard_canvas.canvas.bind('<MouseWheel>',
                                           self.change_brush_size)

        self.whiteboard_canvas.canvas.bind('<Button-1>',
                                           self.start_paint)
        self.whiteboard_canvas.canvas.bind('<B1-Motion>',
                                           self.paint)

        # self.root.bind('<Control-z>', self.undo_last_action)

        self.notebook.bind('<Control-s>', self.save_board)

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

    def undo_last_action(self, event=None):
        self.whiteboard_canvas.undo_last_action()

    def save_board(self, event=None):
        current_tab_index = self.notebook.index(self.notebook.select())
        current_tab = self.notebook.winfo_children()[current_tab_index]

        file_path = filedialog.asksaveasfilename(
            defaultextension='.png',
            filetypes=[('PNG files', '*.png'),
                       ("JPEG files", "*.jpg"),
                       ("All files", "*.*")]
        )

        if file_path:
            x = current_tab.winfo_rootx()
            y = current_tab.winfo_rooty()
            x1 = x + current_tab.winfo_width()
            y1 = y + current_tab.winfo_height()

            image = ImageGrab.grab(bbox=(x, y, x1, y1))
            image.save(file_path)
