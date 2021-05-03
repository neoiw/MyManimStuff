from manim import *
from numpy import equal

class TextsTest(Scene):
    def construct(self):
        text1 = Text("This is test")
        text2 = Text("I just transformed this")

        self.play(Write(text1))
        self.wait()
        self.play(Transform(text1,text2))
        self.wait()

class TextxTest2(Scene):
    def construct(self):
        text1 = Text("Highlight Testing").shift(UP)
        lorem = Text("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",t2c={"ipsum" : BLUE}).scale(0.7)
        broken = Text("Currently `t2c` is broken smh").shift(DOWN)
        self.add(text1,lorem,broken)
        
class SomeGradients(Scene):
    def construct(self):
        text1 = Text("Some COOL Gradation",gradient=(YELLOW,RED))

        self.add(text1)

class SevenTwoSeven(Scene):
    def construct(self):
        funi1 = Text("727",stroke_width=2).set_stroke(color=RED)
        funi2 = Text("727",stroke_width=2).set_stroke(color=BLUE)
        funi3 = Text("727",stroke_width=2).set_stroke(color=YELLOW)
        funi4 = Text("727",stroke_width=2).set_stroke(color=GREEN)
        funi5 = Text("727",stroke_width=2).set_stroke(color=PINK)
        haha = Text("I have achieved comedy").scale(0.5).shift(DOWN)

        self.add(funi1,haha)
        self.wait(0.1)
        funi1.become(funi2)
        self.wait(0.1)
        funi1.become(funi3)
        self.wait(0.1)
        funi1.become(funi4)
        self.wait(0.1)
        funi1.become(funi5)
        self.wait(0.1)


class IntBySub(Scene):
    def construct(self):
        #Mobjects
        rightarrow = MathTex("\\Rightarrow")

        equation = MathTex("\\int \\frac{4-e^{3 x}}{e^{8 x}} \\mathrm{d}x")

        equation1 = MathTex("\\int \\frac{4-e^{3 x}}{e^{8 x}} \\mathrm{d}x")
        equation1[0][3].set_color(YELLOW)
        equation1[0][5].set_color(YELLOW)
        equation1[0][7].set_color(YELLOW)
        equation1[0][9].set_color(YELLOW)

        equation2 = MathTex("=\\int \\frac{1}{u}\\frac{4-u^3}{u^8}\\mathrm{d}u")
        equation2[0][4].set_color(BLUE)
        equation2[0][7].set_color(BLUE)

        equation3 = MathTex("=\\int 4u^{-9}\\mathrm{d}u - \\int u^{-6}\\mathrm{d}u")
        equation3[0][3].set_color(BLUE)
        equation3[0][10].set_color(BLUE)

        equation4 = MathTex("=-\\frac{4}{8}u^{-8}+\\frac{1}{5}u^{-5}+\\mathrm{C}")
        equation4[0][5].set_color(BLUE)
        equation4[0][12].set_color(BLUE)

        equation5 = MathTex("=-\\frac{1}{2e^{8x}}+\\frac{1}{5e^{5x}}+\\mathrm{C}")
        equation5[0][5].set_color(YELLOW)
        equation5[0][7].set_color(YELLOW)
        equation5[0][12].set_color(YELLOW)
        equation5[0][14].set_color(YELLOW)

        
        ex_is_u = MathTex("u","=","e^x").shift(UP*2+LEFT*3)
        ex_is_u.set_color_by_tex("e^x",YELLOW).set_color_by_tex("u",BLUE)

        ex_is_u_deriv = MathTex("\\mathrm{d}u=e^x\\mathrm{d}x,\\frac{1}{e^x}\\mathrm{d}u=\\mathrm{d}x").next_to(ex_is_u,RIGHT,buff=1)
        ex_is_u_deriv[0][1].set_color(BLUE)
        ex_is_u_deriv[0][13].set_color(BLUE)
        ex_is_u_deriv[0][3].set_color(YELLOW)
        ex_is_u_deriv[0][4].set_color(YELLOW)
        ex_is_u_deriv[0][10].set_color(YELLOW)
        ex_is_u_deriv[0][11].set_color(YELLOW)

        ex_is_u_deriv_u = MathTex("\\mathrm{d}u=u\\mathrm{d}x,\\frac{1}{u}\\mathrm{d}u=\\mathrm{d}x").next_to(ex_is_u,RIGHT,buff=1)
        ex_is_u_deriv_u[0][1].set_color(BLUE)
        ex_is_u_deriv_u[0][3].set_color(BLUE)
        ex_is_u_deriv_u[0][9].set_color(BLUE)
        ex_is_u_deriv_u[0][11].set_color(BLUE)

        sub = MathTex("\\frac{\\mathrm{d}F(x)}{\\mathrm{d}x}=\\frac{\\mathrm{d}F\\{g(t)\\}}{\\mathrm{d}x}*\\frac{\\mathrm{d}x}{\\mathrm{d}t}").shift(UP*3)
        sub[0][12].set_color(BLUE)
        sub[0][13].set_color(BLUE)
        sub[0][14].set_color(BLUE)
        sub[0][15].set_color(BLUE)


        #Animations
        self.play(Write(equation))
        self.play(ReplacementTransform(equation,equation1))
        self.wait()
        self.play(FadeIn(ex_is_u))
        self.wait()
        self.play(FadeIn(rightarrow.next_to(ex_is_u)))
        self.wait()
        self.play(Write(ex_is_u_deriv))
        self.wait()
        self.play(ReplacementTransform(ex_is_u_deriv,ex_is_u_deriv_u))
        self.wait()
        self.play(equation1.animate.shift(LEFT*3))
        self.play(Write(equation2.next_to(equation1)))
        self.wait()
        self.play(equation1.animate.shift(LEFT*5),equation2.animate.shift(LEFT*5))
        self.play(Write(equation3))
        self.wait()
        self.play(equation1.animate.shift(LEFT*5),equation2.animate.shift(LEFT*5),equation3.animate.shift(LEFT*5))
        self.play(Write(equation4.next_to(equation3)))
        self.wait()
        self.play(ReplacementTransform(equation4,equation5))
        self.wait()
        