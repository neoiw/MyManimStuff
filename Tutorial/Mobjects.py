from manim import *

class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)

class Shapes(Scene):
    def construct(self):
        circle = Circle()
        triangle = Triangle()
        square = Square()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle,triangle,square)
        self.wait(1)

class MobjectsPlacement(Scene):
    def construct(self):
        circle = Circle()
        triangle = Triangle()
        square = Square()

        circle.move_to(LEFT * 2)
        square.next_to(circle, LEFT)
        triangle.align_to(circle, LEFT)

        self.add(square,circle,triangle)
        self.wait(1)

class MobjectsStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        triangle = Triangle().shift(RIGHT)
        square = Square().shift(UP)

        circle.set_stroke(color=GREEN, width=20)
        triangle.set_fill(PINK, opacity= 0.5)
        triangle.set_stroke(PURPLE, width=10)
        square.set_fill(YELLOW, opacity=1.0)

        self.add(circle,triangle,square)
        self.wait(1)

class SomeAnimations(Scene):
    def construct(self):
        square = Square().set_stroke(RED)

        self.play(FadeIn(square))
        self.play(Rotate(square,PI*21/4), run_time=3)
        self.play(FadeOut(square))
        self.wait(1)