from manim import *


class Intagers(Scene):
    def construct(self):

        start_max = 1
        final_max = 10

        expantion_time = 0.5

        number_line = NumberLine(
            x_range=[0, start_max, 1],
            length=10,
            color=RED,
            include_numbers=True
        )

        self.play(Create(number_line))
        self.wait(0.5)

        current_num_marker = Dot(
            number_line.number_to_point(start_max),
            color=YELLOW
        )
        self.add(current_num_marker)
        self.wait(0.5)

        self.wait(2)
