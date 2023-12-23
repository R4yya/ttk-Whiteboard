import tkinter as tk


class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Simple Whiteboard')


if __name__ == '__main__':
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()
