from manim import *


class Galilean(Scene):
    def construct(self):
        d = Dot([0, -1, 0])
        d2 = Dot([-4, 2, 0], color= GREEN)
        d3 = Dot([-4, 0, 0], color= GREEN)
        line = Line(d2.get_center(), d3.get_center())

        b1 = Brace(line)

        self.add(b1)