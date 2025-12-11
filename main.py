from manim import *


class HelloWorld(Scene):
    def construct(self):
        # 1. Create the text Mobject (Manim Object)
        hello = Text("Hello, World!")

        # 2. Display the text on the screen
        self.play(Write(hello))

        # 3. Wait for 1 second before the animation ends
        self.wait(1)
