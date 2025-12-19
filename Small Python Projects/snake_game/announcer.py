from turtle import Turtle

class ModeAnnouncer:
    def __init__(self, pos=(0, 0), color="white"):
        self.t = Turtle(visible=False)
        self.t.penup()
        self.t.color(color)
        self.t.goto(pos)
        self._ticks_left = 0
        self._text = ""
        self._dirty = False

    def pop(self, text, ticks=60):
        self._text = text
        self._ticks_left = ticks
        self._dirty = True
        self.t.clear()

    def update(self):
        if self._ticks_left <= 0:
            return

        if self._dirty:
            self.t.write(self._text, align="center", font=("Courier", 24, "bold"))
            self._dirty = False

        self._ticks_left -= 1

        if self._ticks_left <= 0:
            self.t.clear()

    def clear(self):
        self._ticks_left = 0
        self._dirty = False
        self.t.clear()
