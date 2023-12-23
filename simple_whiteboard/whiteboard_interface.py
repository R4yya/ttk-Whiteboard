from whiteboard_canvas import WhiteboardCanvas
from whiteboard_controls import WhiteboardControls


class WhiteboardInterface:
    def __init__(self, root):
        self.whiteboard_canvas = WhiteboardCanvas(root)
        self.whiteboard_controls = WhiteboardControls(root,
                                                      self.whiteboard_canvas)
