from manim import *

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