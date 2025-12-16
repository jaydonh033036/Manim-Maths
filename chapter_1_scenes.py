'''
Renders the scense from chapter one of Mathmatics for Physicists
'''
from manim import *


class Test(Scene):
    def construct(self):
        self.wait(0.5)
        initial_title = Text(
            "Numbers, Variables and Functions", font_size=60)
        self.play(Write(initial_title, run_time=2))
        self.wait(1)

        target_title = initial_title.copy()
        target_title.scale(0.5)
        target_title.to_edge(UP)

        self.play(Transform(initial_title, target_title), run_time=1.5)

        self.play(FadeOut(initial_title, shift=UP), run_time=1)


class NumberTypes(Scene):
    '''
    Shows The different types of numbers.
    '''

    def construct(self):
        self.wait(0.5)
        initial_title = Text(
            "Numbers, Variables and Functions", font_size=60, color=GREEN)
        self.play(Write(initial_title, run_time=2))
        self.wait(1)

        target_title = initial_title.copy()
        target_title.scale(0.5)
        target_title.to_edge(UP)

        self.play(Transform(initial_title, target_title), run_time=1.5)

        number_line = NumberLine(
            x_range=[0, 11, 1],
            length=10,
            color=RED,
            include_numbers=True,
            font_size=30,
            include_tip=True
        )

        self.play(
            AnimationGroup(
                FadeOut(initial_title, shift=UP, run_time=3),
                Create(number_line, run_time=2)
            )
        )
        self.wait(0.5)
