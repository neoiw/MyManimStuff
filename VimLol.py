from manim import *

class VimCodingLOL(Scene):
    def construct(self):
        circle = Circle()

        self.play(FadeIn(circle))

class IDunoHowThisWorks(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=3,
            y_min=-1,
            y_max=9,
            **kwargs
        )
    def construct(self):
        self.setup_axes()
        func = lambda x : x**2-1
        graf =  DashedVMobject(self.get_graph(func,x_min=-1,x_max=3))

        self.play(Create(graf))
