from manimlib import *


class Test(Scene):

    def construct(self):
        circle = Circle()
        self.play(ShowCreation(circle))
        square = Square()
        self.add(square)
        self.wait(2)