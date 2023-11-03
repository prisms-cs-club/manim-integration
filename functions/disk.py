from manim import *

class Disk(ThreeDScene):
    def construct(self):
        # 1) Show the creation of rieman rectangles
        # 2) Focus on one rectangle
        # 3) Show rotation
        # 4) Sum up the area
        pass

        # Show the creation of rieman rectangles using Manim's built in functions:
        axes = ThreeDAxes(
                    x_range=[-4, 4, 1],
                    y_range=[-3, 3, 1],
                    z_range=[-3, 3, 1],
                    x_length=8,
                    y_length=6,
                    z_length=6,
                )
        
        graph = axes.plot(lambda x: (x/2) ** 2, x_range=[-4, 4, 1], color=YELLOW)

        self.play(Create(axes), Create(graph))


        self.move_camera(phi = 75 * DEGREES, theta = -45 * DEGREES)
        # Create rieman rectangles
        rects = axes.get_riemann_rectangles(
            graph = graph, x_range=[-4, 4], dx=0.25, stroke_color=WHITE
            )
        self.play(Create(rects))
        # Set the opacity of all the rectangles other than the first one to 0.25, so that we can focus on the first rectangle
        animations = []
        for rect in rects[1:]:
            # Gradually set the opacity instead of setting it instantly
            animations.append(rect.animate.set_opacity(0.25))
        self.play(*animations)
        self.wait(1)
        # # look directly at the yz plane for debugging
        # self.move_camera(phi=0 * DEGREES, theta=0 * DEGREES)

        # first_rectangle = rects[0]
        # half_radius = first_rectangle.get_height() / 2



        # curved_arrow = CurvedArrow(
        #     #[0, half_radius * np.sin(PI/4), -half_radius * np.cos(PI/4)],
        #     #[0, half_radius * np.sin(PI/4), half_radius * np.cos(PI/4)]
        #     [-half_radius * np.cos(PI/4), half_radius * np.sin(PI/4), 0],
        #     [half_radius * np.cos(PI/4), half_radius * np.sin(PI/4), 0],
        #     )
        # curved_arrow.shift([first_rectangle.get_x(), 0, 0])
        # self.play(Create(curved_arrow))
        # curved_arrow = CurvedArrow(
        #     [first_rectangle.get_x(), 0, -half_radius],
        #     [first_rectangle.get_x(), 0, half_radius], 
        #     angle = PI
        # )       
        # self.wait(1)

        # rotate the first rectangle around the x axis to form a cylinder
        first_rectangle = rects[0]
        self.play(Rotate(first_rectangle, PI/2, X_AXIS))
        self.wait(1)

        cylinder = Cylinder(radius=rect.width / 2, height=rect.height)

        self.add(rect, cylinder)

        self.play(Rotate(rect, PI / 2, axis=X_AXIS))



#
if __name__ == '__main__':
    import subprocess
    subprocess.run(['manim', '-p', '-qh', __file__, 'Disk'])