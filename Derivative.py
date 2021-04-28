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
        func_graph = self.get_graph(func,x_min=-1,x_max=9)
        x_start = ValueTracker(3)
        x_end = ValueTracker(7)

        dot_start = Dot(self.coords_to_point(x_start.get_value(),func(x_start.get_value())))
        dot_end = Dot(self.coords_to_point(x_end.get_value(),func(x_end.get_value())))
        
        def dot_updater(dot):
            x = x_end.get_value()
            dot.move_to(self.coords_to_point(x,func(x)))
        def deriv_func(a,x):
            line = 0.3 * x * (a**2-10*a+22) - 0.2 * (a**3-7.5*a**2+25)
            return line

        dot_end.add_updater(dot_updater)
        
        line = Line(dot_start.get_center(),dot_end.get_center(),color=YELLOW).scale(3)
        line_new = Line(ORIGIN,line.get_unit_vector()).scale(5).move_to(self.coords_to_point(x_end.get_value(),func(x_end.get_value())))
        line_another = self.get_graph(lambda x : deriv_func(x_start.get_value(),x),color=YELLOW)
        
        line.add_updater(
            lambda x : x.become(
                Line(
                    dot_start.get_center(),dot_end.get_center(),color=YELLOW
                ).scale(3)
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
        self.play(*list(map(GrowFromCenter,[dot_start,dot_end])),Write(line))
        self.wait()
        #self.play(Create(line_new))
        self.play(x_end.animate.set_value(3),ReplacementTransform(line,line_another))
        self.wait()