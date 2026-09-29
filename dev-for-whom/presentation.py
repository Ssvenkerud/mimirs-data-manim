
from manim import *
from manim_slides import Slide




class Presentation(Slide):
    #def update_canvas(self):
    #    self.counter += 1
    #    old_slide_number = self.canvas["slide_number"]
    #    new_slide_number = Text(f"{self.counter}").move_to(old_slide_number)
    #    self.play(Transform(old_slide_number, new_slide_number))
    def construct(self):
# ---------------------------------------------------------
        # SLIDE 1: Completely Blank
        # ---------------------------------------------------------
        # Canvas starts blank. Pause immediately for slide 1.
        self.next_slide()

        # ---------------------------------------------------------
        # SLIDE 2: Title Page
        # ---------------------------------------------------------
        title = Text("Interactive Presentations with Manim", font_size=44, weight=BOLD)
        subtitle = Text("A Modern Approach to Animated Slides", font_size=28, color=BLUE)
        
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.5)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.next_slide()

        # Clear slide 2
        self.play(FadeOut(title_group))

        # ---------------------------------------------------------
        # SLIDE 3: Speaker Information & Picture
        # ---------------------------------------------------------
        # Speaker image (uses 'speaker.png' if available, falls back to a framed box)
        try:
            speaker_img = ImageMobject("speaker.png").scale_to_fit_height(3.5)
        except Exception:
            frame = Rectangle(height=3.8, width=3.0, color=BLUE, fill_opacity=0.1)
            label = Text("Speaker\nPhoto", font_size=20, color=GRAY)
            speaker_img = Group(frame, label)

        speaker_name = Text("Dr. Alex Morgan", font_size=32, weight=BOLD)
        speaker_role = Text("Lead Visualization Engineer", font_size=22, color=BLUE)
        speaker_bio = BulletedList(
            "PhD in Computer Science",
            "Specialist in Scientific Animation",
            "Core Contributor to Open Source Tools",
            font_size=20,
            buff=0.25
        )

        bio_group = VGroup(speaker_name, speaker_role, speaker_bio).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        speaker_slide = Group(speaker_img, bio_group).arrange(RIGHT, buff=0.8)

        self.play(FadeIn(speaker_img), Write(bio_group))
        self.next_slide()

        # Clear slide 3
        self.play(FadeOut(speaker_slide))

        # ---------------------------------------------------------
        # SLIDE 4: Content Slide 1 - Key Features
        # ---------------------------------------------------------
        slide4_title = Text("Key Features", font_size=36, weight=BOLD).to_corner(UL)
        
        bullets = BulletedList(
            "Step-by-step animation controls",
            "Seamless transition between static and dynamic elements",
            "High-resolution video rendering",
            "Cross-platform presentation viewing",
            font_size=24,
            buff=0.35
        ).next_to(slide4_title, DOWN, aligned_edge=LEFT, buff=0.6)

        self.play(Write(slide4_title))
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=RIGHT * 0.2), run_time=0.5)
        self.next_slide()

        # Clear slide 4
        self.play(FadeOut(slide4_title), FadeOut(bullets))

        # ---------------------------------------------------------
        # SLIDE 5: Content Slide 2 - Conclusion
        # ---------------------------------------------------------
        slide5_title = Text("Conclusion & Summary", font_size=36, weight=BOLD).to_corner(UL)
        
        box = RoundedRectangle(corner_radius=0.2, width=9, height=2.5, color=BLUE, fill_opacity=0.1)
        summary = Text(
            "Manim-slides combines programmatic precision\nwith real-time slide navigation.",
            font_size=24,
            alignment="center"
        ).move_to(box)

        content = VGroup(box, summary).next_to(slide5_title, DOWN, buff=0.8)

        self.play(Write(slide5_title))
        self.play(Create(box), Write(summary))
        self.next_slide()
