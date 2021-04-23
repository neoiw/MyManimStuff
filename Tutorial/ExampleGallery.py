from manim import *

class BraceAnnotation(Scene):
    def construct(self):
        dot1 = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot1.get_center(), dot2.get_center()).set_color(ORANGE)

        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_2")
        self.add(line, dot1, dot2, b1, b1text, b2, b2text)


class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=GREEN)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        line = Line([3, 0, 0], [5, 0, 0])
        self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=2)
        self.wait()

class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN,[2,2,0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0,0)').next_to(dot,DOWN)
        tip_text = Text('(2,0)').next_to(arrow.get_end(),RIGHT)
        self.add(arrow,dot,numberplane,origin_text,tip_text)


class MoveBrace(Scene):
    def construct(self):
        text = MathTex(
            "\\frac{d}{dx}f(x)g(x)=",
            "f(x)\\frac{d}{dx}g(x)",
            "+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        brace1 = Brace(text[1],UP,buff=SMALL_BUFF).set_color(BLUE)
        brace2 = Brace(text[3],UP,buff=SMALL_BUFF).set_color(BLUE)
        text1 = brace1.get_text("$f'(x)g(x)$").set_color(BLUE)
        text2 = brace2.get_text("$g'(x)f(x)$").set_color(BLUE)

        self.play(Write(text))
        self.play(
            GrowFromCenter(brace1),
            FadeIn(text1),
        )
        self.wait()
        self.play(
            ReplacementTransform(brace1,brace2),
            ReplacementTransform(text1,text2),
        )
        self.wait()

class MovingAngle(Scene):
    def construct(self):
        rotation_center = LEFT
        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT,RIGHT)
        line_moving = Line(LEFT,RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(
            theta_tracker.get_value() * DEGREES, about_point=rotation_center
        )
        a = Angle(line1,line_moving,radius=0.5,other_angle=False)
        te = MathTex("\\theta").move_to(
            Angle(
                line1,line_moving,radius=0.5+3*SMALL_BUFF,other_angle=False
            ).point_from_proportion(0.5)
        )
        self.add(line1,line_moving,te,a)
        self.wait()

        line_moving.add_updater(
            lambda x : x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )

        a.add_updater(
            lambda x : x.become(Angle(line1,line_moving,radius=0.5,other_angle=False))
        )

        te.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1,line_moving,radius=0.5+3*SMALL_BUFF,other_angle=False
                ).point_from_proportion(0.5)
            )
        )
        self.play(theta_tracker.animate.set_value(30))
        self.play(theta_tracker.animate.increment_value(150))
        self.play(te.animate.set_color(RED), run_time=0.5)
        self.play(theta_tracker.animate.set_value(270))

class PointPath(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(),dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path,dot)
        self.play(Rotating(dot,radians=PI,about_point=RIGHT,run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))

class PointWithTrace(Scene):
    def construct(self):
        path = VMobject()
        dot = Dot()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dot)
        self.play(Rotating(dot, radians=PI, about_point=RIGHT, run_time=2))
        self.wait()
        self.play(dot.animate.shift(UP))
        self.play(dot.animate.shift(LEFT))
        self.wait()

class Updater1(Scene):
    def construct(self):
        dot = Dot()
        text = Text("Label").next_to(dot,RIGHT,buff=SMALL_BUFF)

        def update_text(smth):
            smth.next_to(dot,RIGHT,buff=SMALL_BUFF)
        text.add_updater(update_text)

        self.add(dot,text)

        self.play(dot.animate.shift(UP*2))

class Updater2(Scene):
    def construct(self):
        dot = Dot()
        text = Text("Test").next_to(dot,RIGHT,buff=SMALL_BUFF)

        text.add_updater(lambda x : x.next_to(dot,RIGHT,SMALL_BUFF))

        self.add(dot,text)
        self.play(dot.animate.shift(UP*2))

class Updater3(Scene):
    def construct(self):
        numberline = NumberLine(x_min=-1,x_max=+1)
        triangle = RegularPolygon(3,start_angle=-PI/2)
        triangle.scale(0.2)
        triangle.next_to(numberline.get_left(),UP,buff=SMALL_BUFF)
        decimal = DecimalNumber(0,num_decimal_places=3,include_sign=True,unit="\\rm cm")

        decimal.add_updater(lambda x : x.next_to(triangle,UP,buff=SMALL_BUFF))
        decimal.add_updater(lambda x : x.set_value(triangle.get_center()[0]))

        self.add(numberline,triangle,decimal)
        self.play(
            triangle.animate.shift(RIGHT*2),
            rate_func=there_and_back,
            run_time=5,
        )

class UpdaterValueTracker(Scene):
    def construct(self):
        theta = ValueTracker(PI/2)
        line1 = Line(ORIGIN,RIGHT,color=RED)
        line2 = Line(ORIGIN,RIGHT,color=GREEN)

        line2.rotate(theta.get_value(), about_point=ORIGIN)

        line2.add_updater(lambda x : x.set_angle(theta.get_value()))

        self.add(line1,line2)
        self.play(theta.animate.increment_value(PI/2))


class TwoLineCircle(Scene):
    def construct(self):
        theta = ValueTracker(0)
        line1 = Line(ORIGIN,RIGHT*3,color=RED)
        line2 = Line(ORIGIN,RIGHT*3,color=GREEN)
        line3 = Line(line1.get_end(),line2.get_end())
        line_ref = line2.copy()

        line2.add_updater(lambda x : x.become(line_ref.copy().rotate(
            theta.get_value(),about_point=ORIGIN)
        ))
        line3.add_updater(lambda x : x.become(
            Line(line1.get_end(),line2.get_end(),color=BLUE)
        ))

        arc = Arc(radius=3,start_angle=line1.get_angle(),angle=theta.get_value(),color=ORANGE)

        arc.add_updater(lambda x : x.become(Arc(radius=3,start_angle=line1.get_angle(),angle=theta.get_value(),color=ORANGE)))

        self.add(line1,line2,arc,line3)
        

        self.play(theta.animate.increment_value(PI*2),run_time=5)
        self.wait()

class ValueTracker1(Scene):
    def construct(self):
        x_value = ValueTracker(0)
        x2 = lambda x : x.get_value()**2
        x2_value = ValueTracker(x2(x_value))
        x_text = MathTex("x = ")
        x2_text = MathTex("x^2 = ")
        x_num = DecimalNumber(x_value.get_value(),num_decimal_places=2)
        x2_num = DecimalNumber(x2_value.get_value(),num_decimal_places=2)

        x_num.add_updater(lambda x : x.set_value(x_value.get_value()))
        x2_num.add_updater(lambda x : x.set_value((x2(x_value))))

        group = VGroup(x_text,x_num,x2_text,x2_num).scale(2.6)
        VGroup(x_num,x2_num).arrange_submobjects(DOWN,buff=3)

        x_text.next_to(x_num,LEFT,buff=0.7)
        x2_text.next_to(x2_num,LEFT,buff=0.7)

        self.play(Create(group.move_to(ORIGIN)))
        self.wait()
        self.play(
            x_value.animate.increment_value(30),
            rate_func=rate_functions.ease_in_out_quint,
            run_time = 10,
        )
        self.wait()
        self.play(
            x_value.animate.set_value(0),
            rate_func=rate_functions.ease_in_out_quint,
            run_time=10,
        )
        self.wait()

class BongoCat(Scene):
    def construct(self):
        cat = SVGMobject("bongocat_transparent")
        self.add(cat)