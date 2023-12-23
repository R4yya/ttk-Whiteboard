import tkinter as tk
from interface import WhiteboardInterface


class WhiteboardApp(object):
    def __init__(self, root):
        self.root = root
        self.root.title('Simple Whiteboard')

        self.whiteboard_interface = WhiteboardInterface(root)


if __name__ == '__main__':
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()
