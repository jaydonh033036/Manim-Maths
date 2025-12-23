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

        rational_numbers = MathTex(
            r'\text{Rational Numbers}\ \{\mathbb{R}\}',
            font_size=60,
            color=BLUE
        ).shift(DOWN*2)

        negative_number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            color=RED,
            include_numbers=True,
            font_size=30,
        )

        self.add(rational_numbers, negative_number_line)

        one_point = negative_number_line.n2p(1)
        pointer = Dot(point=one_point, color=YELLOW)

        number = MathTex(
            '1',
            color=YELLOW,
            font_size=90
        ).shift(UP*1.5)

        self.play(FadeIn(pointer))
        self.play(Write(number))

        half_point = negative_number_line.n2p(0.5)
        new_number = MathTex(
            r'\frac{1}{2}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2)

        self.play(
            pointer.animate.move_to(half_point),
            Transform(number, new_number),
            run_time=1.5
        )

        general_frac = MathTex(
            r'\frac{A}{B}',
            color=PURPLE,
            font_size=90
        ).shift(UP*2).shift(LEFT)
        equals = MathTex(
            r'=',
            color=PURPLE,
            font_size=90
        ).shift(UP*2)

        self.remove(new_number)
        self.play(number.animate.shift(RIGHT))
        self.play(Write(general_frac))
        self.play(Write(equals))

        self.play(
            number.animate.shift(LEFT*3),
            general_frac.animate.shift(LEFT*3),
            equals.animate.shift(LEFT*3)
        )

        part_of_intagers = MathTex(
            r'A,\ B\in \mathbb{Z}',
            color=PURPLE,
            font_size=90
        ).shift(UP*2).shift(RIGHT*3)

        self.play(Write(part_of_intagers))

        self.wait(1)

        self.play(
            AnimationGroup(
                FadeOut(part_of_intagers, shift=RIGHT),
                number.animate.shift(RIGHT*3),
                general_frac.animate.shift(RIGHT*3),
                equals.animate.shift(RIGHT*3)
            )
        )

        new_point = negative_number_line.n2p(0.25)
        new_number = MathTex(
            r'\frac{1}{4}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(11/4)
        new_number = MathTex(
            r'\frac{11}{4}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(-17/4)
        new_number = MathTex(
            r'-\frac{17}{4}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT*1.4)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(3)
        new_number = MathTex(
            r'\frac{9}{3}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(-2/9)
        new_number = MathTex(
            r'-\frac{2}{9}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT*1.2)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

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

        sub_title = Text(
            'Types of Numbers', font_size=60, color=BLUE_B
        )
        self.play(
            FadeOut(initial_title, shift=DOWN),
            FadeIn(sub_title, shift=DOWN)
        )

        target_title = sub_title.copy()
        target_title.scale(0.5)
        target_title.to_edge(UP)

        self.play(Transform(sub_title, target_title), run_time=1.5)

        natural_numbers = MathTex(
            r'\text{Natural Numbers}\ \{\mathbb{N}\}',
            font_size=60,
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
                FadeOut(sub_title, shift=UP, run_time=3),
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

        integers = MathTex(
            r'\text{Integers}\ \{\mathbb{Z}\}',
            font_size=60,
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

        self.play(
            FadeOut(pos_pointer),
            FadeOut(neg_ponter)
        )
        rational_numbers = MathTex(
            r'\text{Rational Numbers}\ \{R\}',
            font_size=60,
            color=BLUE
        ).shift(DOWN*2)

        self.play(
            AnimationGroup(
                FadeOut(integers, shift=DOWN),
                FadeIn(rational_numbers, shift=DOWN),
                FadeOut(zero_number, zero_neg_number)
            ),
            run_time=1.5
        )

        one_point = negative_number_line.n2p(1)
        pointer = Dot(point=one_point, color=YELLOW)

        number = MathTex(
            '1',
            color=YELLOW,
            font_size=90
        ).shift(UP*1.5)

        self.play(FadeIn(pointer))
        self.play(Write(number))

        half_point = negative_number_line.n2p(0.5)
        new_number = MathTex(
            r'\frac{1}{2}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2)

        self.play(
            pointer.animate.move_to(half_point),
            Transform(number, new_number),
            run_time=1.5
        )

        general_frac = MathTex(
            r'\frac{A}{B}',
            color=PURPLE,
            font_size=90
        ).shift(UP*2).shift(LEFT)
        equals = MathTex(
            r'=',
            color=PURPLE,
            font_size=90
        ).shift(UP*2)

        self.remove(new_number)
        self.play(number.animate.shift(RIGHT))
        self.play(Write(general_frac))
        self.play(Write(equals))

        self.play(
            number.animate.shift(LEFT*3),
            general_frac.animate.shift(LEFT*3),
            equals.animate.shift(LEFT*3)
        )

        part_of_intagers = MathTex(
            r'A,\ B\in \mathbb{Z}',
            color=PURPLE,
            font_size=90
        ).shift(UP*2).shift(RIGHT*3)

        self.play(Write(part_of_intagers))

        self.wait(1)

        self.play(
            AnimationGroup(
                FadeOut(part_of_intagers, shift=RIGHT),
                number.animate.shift(RIGHT*3),
                general_frac.animate.shift(RIGHT*3),
                equals.animate.shift(RIGHT*3)
            )
        )

        new_point = negative_number_line.n2p(0.25)
        new_number = MathTex(
            r'\frac{1}{4}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(11/4)
        new_number = MathTex(
            r'\frac{11}{4}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(-17/4)
        new_number = MathTex(
            r'-\frac{17}{4}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT*1.4)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(3)
        new_number = MathTex(
            r'\frac{9}{3}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)

        new_point = negative_number_line.n2p(-2/9)
        new_number = MathTex(
            r'-\frac{2}{9}',
            color=YELLOW,
            font_size=90
        ).shift(UP*2).shift(RIGHT*1.2)

        self.play(
            pointer.animate.move_to(new_point),
            Transform(number, new_number),
            run_time=0.5
        )

        self.wait(0.5)
