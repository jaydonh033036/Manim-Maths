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

        integers = Text(
            'Integers',
            font_size=42,
            color=BLUE
        ).shift(DOWN*2)

        negative_number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            color=RED,
            include_numbers=True,
            font_size=30,
        )

        self.add(integers, negative_number_line)

        zero_position = negative_number_line.n2p(0)
        pointer = Dot(zero_position, color=WHITE)
        pos_pointer = Dot(zero_position, color=YELLOW)
        neg_ponter = Dot(zero_position, color=PURPLE)

        zero_number = DecimalNumber(
            0,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=WHITE
        ).shift(UP*1.5)
        zero_neg_number = DecimalNumber(
            0,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=WHITE
        ).move_to(zero_number)

        pos_number = DecimalNumber(
            1,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=YELLOW
        ).move_to(zero_number).shift(RIGHT*3)
        neg_number = DecimalNumber(
            -1,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=PURPLE
        ).move_to(zero_number).shift(LEFT*3)

        self.play(FadeIn(pointer), Write(zero_number))

        self.remove(pointer)
        self.remove(zero_number)
        self.play(
            pos_pointer.animate.move_to(negative_number_line.n2p(1)),
            neg_ponter.animate.move_to(negative_number_line.n2p(-1)),
            ClockwiseTransform(zero_number, pos_number),
            CounterclockwiseTransform(zero_neg_number, neg_number)
        )

        for i in range(2, 6):
            pos_number_line_position = negative_number_line.n2p(i)
            neg_number_line_position = negative_number_line.n2p(-i)
            new_pos_number = DecimalNumber(
                i,
                num_decimal_places=0,
                include_sign=False,
                font_size=90,
                color=YELLOW
            ).shift(UP*1.5).shift(RIGHT*3)
            new_neg_number = DecimalNumber(
                -i,
                num_decimal_places=0,
                include_sign=False,
                font_size=90,
                color=PURPLE
            ).shift(UP*1.5).shift(LEFT*3)

            self.play(
                pos_pointer.animate.move_to(pos_number_line_position),
                neg_ponter.animate.move_to(neg_number_line_position),
                run_time=2 ** (-0.3*i),
                rate_func=linear
            )
            self.play(
                Transform(zero_neg_number, new_neg_number),
                Transform(zero_number, new_pos_number),
                run_time=0.01
            )

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
            x_range=[1, 11, 1],
            length=10,
            color=RED,
            include_numbers=True,
            font_size=30,
        )

        self.play(
            AnimationGroup(
                Write(natural_numbers, run_time=3),
                FadeOut(initial_title, shift=UP, run_time=3),
                Create(number_line, run_time=2)
            )
        )

        number_line_position = number_line.n2p(1)

        pointer = Dot(point=number_line_position, color=YELLOW)

        number = DecimalNumber(
            1,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=YELLOW
        ).shift(UP*1.5)

        self.play(FadeIn(pointer))
        self.play(Write(number))

        for i in range(2, 11):
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

        self.play(FadeOut(pointer))

        integers = Text(
            'Integers',
            font_size=42,
            color=BLUE
        ).shift(DOWN*2)

        negative_number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            color=RED,
            include_numbers=True,
            font_size=30,
        )

        self.play(
            AnimationGroup(
                Transform(number_line, negative_number_line),
                FadeOut(natural_numbers, shift=DOWN),
                FadeIn(integers, shift=DOWN),
                FadeOut(number)
            ),
            run_time=1.5
        )

        zero_position = negative_number_line.n2p(0)
        pointer = Dot(zero_position, color=WHITE)
        pos_pointer = Dot(zero_position, color=YELLOW)
        neg_ponter = Dot(zero_position, color=PURPLE)

        zero_number = DecimalNumber(
            0,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=WHITE
        ).shift(UP*1.5)
        zero_neg_number = DecimalNumber(
            0,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=WHITE
        ).move_to(zero_number)

        pos_number = DecimalNumber(
            1,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=YELLOW
        ).move_to(zero_number).shift(RIGHT*3)
        neg_number = DecimalNumber(
            -1,
            num_decimal_places=0,
            include_sign=False,
            font_size=90,
            color=PURPLE
        ).move_to(zero_number).shift(LEFT*3)

        self.play(FadeIn(pointer), Write(zero_number))

        self.remove(pointer)
        self.remove(zero_number)
        self.play(
            pos_pointer.animate.move_to(negative_number_line.n2p(1)),
            neg_ponter.animate.move_to(negative_number_line.n2p(-1)),
            ClockwiseTransform(zero_number, pos_number),
            CounterclockwiseTransform(zero_neg_number, neg_number)
        )

        for i in range(2, 6):
            pos_number_line_position = negative_number_line.n2p(i)
            neg_number_line_position = negative_number_line.n2p(-i)
            new_pos_number = DecimalNumber(
                i,
                num_decimal_places=0,
                include_sign=False,
                font_size=90,
                color=YELLOW
            ).shift(UP*1.5).shift(RIGHT*3)
            new_neg_number = DecimalNumber(
                -i,
                num_decimal_places=0,
                include_sign=False,
                font_size=90,
                color=PURPLE
            ).shift(UP*1.5).shift(LEFT*3)

            self.play(
                pos_pointer.animate.move_to(pos_number_line_position),
                neg_ponter.animate.move_to(neg_number_line_position),
                run_time=2 ** (-0.3*i),
                rate_func=linear
            )
            self.play(
                Transform(zero_neg_number, new_neg_number),
                Transform(zero_number, new_pos_number),
                run_time=0.01
            )
