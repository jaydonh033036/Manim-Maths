'''
Renders the scense from chapter one of Mathmatics for Physicists.
'''
from manim import *


class Test(Scene):
    '''
    This is to test scenes before being added to the main video.
    '''

    def construct(self):
        self.wait(0.5)
        number_line = NumberLine(
            x_range=[0, 11, 1],
            length=10,
            color=RED,
            include_numbers=True,
            font_size=30,
            include_tip=True
        )

        self.add(number_line)

        self.wait(1)


class NumberTypes(Scene):
    '''
    Shows The different types of numbers.
    '''

    def construct(self):
        self.wait(0.5)
        initial_title = Text(
            "Numbers, Variables and Functions", font_size=60, color=BLUE_B)
        self.play(Write(initial_title, run_time=2))
        self.wait(1)

        target_title = initial_title.copy()
        target_title.scale(0.5)
        target_title.to_edge(UP)

        self.play(Transform(initial_title, target_title), run_time=1.5)

        natural_numbers = Text(
            'Natural Numbers',
            font_size=42,
            color=BLUE
        ).shift(DOWN*2)

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
                Write(natural_numbers, run_time=3),
                FadeOut(initial_title, shift=UP, run_time=3),
                Create(number_line, run_time=2)
            )
        )

        number_line_position = number_line.n2p(0)

        pointer = Dot(point=number_line_position, color=YELLOW)

        number = DecimalNumber(
            0,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=YELLOW
        ).shift(UP*1.5)

        self.play(FadeIn(pointer))
        self.play(Write(number))

        for i in range(1, 11):
            number_line_position = number_line.n2p(i)
            new_number = DecimalNumber(
                i,
                num_decimal_places=0,
                include_sign=False,
                font_size=90,
                color=YELLOW
            ).shift(UP*1.5)

            self.play(
                pointer.animate.move_to(number_line_position),
                run_time=2 ** (-0.3*i),
                rate_func=linear
            )
            self.play(Transform(number, new_number), run_time=0.01)
        self.wait(0.5)
