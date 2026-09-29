from manim import *
from manim_slides import Slide


class BasicExample(Slide):
    def construct(self):
        circle = Circle(radius=3, color=RED)
        dot = Dot()

        self.play(GrowFromCenter(circle))
        self.next_slide()  # Waits for user input to continue

        self.next_slide(loop=True)  # Start loop
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.next_slide()  # New non-looping slide

        self.play(dot.animate.move_to(ORIGIN))
