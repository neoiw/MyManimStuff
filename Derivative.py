from manim import *

class Derivative(GraphScene):
    def __init__(self,**kwargs):
        GraphScene.__init__(
            self,
            x_min=-1,
            x_max=10,
            y_min=-1,
            y_max=6,
            graph_origin=[-4,-2,0],
            **kwargs
        )

    def construct(self):
        self.setup_axes(animate=True)
        func = lambda x : 0.1 * (x - 2) * (x - 8) * (x - 5) + 3
        func_graph = self.get_graph(func,x_min=0.8,x_max=9)
        x_start = 3
        x_end = ValueTracker(7)
        dot_start = Dot(self.coords_to_point(x_start,func(x_start)))
        dot_end = Dot(self.coords_to_point(x_end.get_value(),func(x_end.get_value())))
        
        def dot_updater(dot):
            x = x_end.get_value()
            dot.move_to(self.coords_to_point(x,func(x)))

        dot_end.add_updater(dot_updater)
        
        line = Line(dot_start.get_center(),dot_end.get_center(),color=BLACK)
        line_new = Line(ORIGIN,line.get_unit_vector()).scale(5).move_to(self.coords_to_point(x_end.get_value(),func(x_end.get_value())))
        line_another = TangentLine(func_graph,<This part>,length=5)
        
        line.add_updater(
            lambda x : x.become(
                Line(
                    dot_start.get_center(),dot_end.get_center(),color=BLACK
                )
            )
        )
        line_new.add_updater(lambda x : x.become(
            Line(ORIGIN,line.get_unit_vector()).scale(5).move_to(self.coords_to_point(x_end.get_value(),func(x_end.get_value())))
        ))
        #line_another.add_updater(lambda x : x.become(
        #    TangentLine(func_graph,x_end.get_value(),length=5)
        #))

        self.play(Create(func_graph))
        self.wait()
        self.play(*list(map(GrowFromCenter,[dot_start,dot_end])))
        self.wait()
        #self.play(Create(line_new))
        self.add(line_another)
        self.wait()

class Teset(Scene):
    def construct(self):
        x = ValueTracker(0)
        line = Line(RIGHT+UP,RIGHT+DOWN).rotate(x.get_value())
        line.add_updater(lambda v : v.become(Line(RIGHT+UP,RIGHT+DOWN).rotate(x.get_value())))
        line_new = Line(UP,line.get_unit_vector())
        line_new.add_updater(lambda v : v.become(Line(UP,line.get_unit_vector())))
        self.add(line_new,line.shift(UP+RIGHT))
        self.play(x.animate.increment_value(10),rate_func=linear,run_time=20)
        self.wait()

        np = NumberPlane()
        
