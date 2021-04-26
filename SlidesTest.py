from manim import *
from manim_presentation import Slide

class SlideTest1(Slide):
    def construct(self):
        dot = Dot(UP)
        circle = Circle(radius = 1,color=GREEN)
        

        self.play(Create(dot),Create(circle))
        self.pause()

        self.play(MoveAlongPath(dot,circle))
        self.wait()


class Example(Slide):
    def construct(self):
        circle = Circle(radius=3, color=BLUE)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.pause()

        self.start_loop()
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.end_loop()

        self.play(dot.animate.move_to(ORIGIN))
        self.pause()

        self.wait()