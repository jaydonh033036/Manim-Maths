from manim import *


class HelloWorld(Scene):
    def construct(self):
        # 1. Create the text Mobject (Manim Object)
        hello = Text("Hello, World!")

        # 2. Display the text on the screen
        self.play(Write(hello))

        # 3. Wait for 1 second before the animation ends
        self.wait(1)


class SquareToCircle(Scene):
    def construct(self):

        square = Square(color=BLUE)
        circle = Circle(color=GREEN)

        self.play(Create(square))

        self.play(Transform(square, circle))

        self.wait(1)
