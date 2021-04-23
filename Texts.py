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
