from manim import *


class Intagers(MovingCameraScene):
    def construct(self):
        start_min = -1
        final_min = -5

        start_max = 1
        final_max = 5

        expantion_time = 0.5

        number_line = NumberLine(
            x_range=[start_min, start_max, 1],
            length=10,
            color=RED,
            include_numbers=True,
            font_size=24
        )

        self.play(Create(number_line))
        self.wait(0.5)

        for i in range(start_max+1, final_max+1):
            new_number_line = NumberLine(
                x_range=[-i, i],
                length=10 * i / start_max,
                color=RED,
                include_numbers=True,
                font_size=24*((2*i)/(start_max))
            )

            self.play(
                Transform(number_line, new_number_line),
                self.camera.frame.animate.scale(
                    (i)/(start_max-start_min)
                ),
                run_time=expantion_time,
                rate_func=linear
            )
        self.wait(1)
