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
        rectangle_path_outline = Circle(color = WHITE, radius = first_rectangle.get_height())
        rectangle_path_outline.shift([first_rectangle.get_x(), 0, 0])
        rectangle_path_outline.rotate(PI / 2, axis = Y_AXIS, about_point=[first_rectangle.get_x(),0,0])
        rectangle_path_outline.rotate(-PI / 2, axis = X_AXIS, about_point=[first_rectangle.get_x(),0,0])
        rectangle_path_outline.rotate(PI, axis = Z_AXIS, about_point=[first_rectangle.get_x(),0,0])
        self.play(Rotate(first_rectangle,  -2 * PI, X_AXIS, about_point=[first_rectangle.get_x(),0,0]), DrawBorderThenFill(rectangle_path_outline))
        self.play(rectangle_path_outline.animate.set_fill(opacity=0.5))

        rotate_animations = []
        opacity_animations = []
        for rect in rects[1:]:
            rectangle_path_outline = Circle(color = WHITE, radius = rect.get_height())
            rectangle_path_outline.shift([rect.get_x(), 0, 0])
            rectangle_path_outline.rotate(PI / 2, axis = Y_AXIS, about_point=[rect.get_x(),0,0])
            rectangle_path_outline.rotate(-PI / 2, axis = X_AXIS, about_point=[rect.get_x(),0,0])
            rectangle_path_outline.rotate(PI, axis = Z_AXIS, about_point=[rect.get_x(),0,0])
            rotate_animations.append(Rotate(rect,  -2 * PI, X_AXIS, about_point=[rect.get_x(),0,0]))
            rotate_animations.append(DrawBorderThenFill(rectangle_path_outline))
            
            opacity_animations.append(rectangle_path_outline.animate.set_fill(opacity=0.1))

        self.play(*rotate_animations)
        self.wait(1)
        self.play(*opacity_animations)

        fade_out_animations = []
        for mobject in self.mobjects:
            fade_out_animations.append(FadeOut(mobject))
        self.play(*fade_out_animations)
        self.wait(1)

        # Calculate area of circles
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)
        first_circle = Circle(color = WHITE, radius = rect.get_height())
        new_first_rectangle = rects[0].copy()
        new_first_rectangle.move_to(ORIGIN).shift(RIGHT * 5)
        first_circle.next_to(new_first_rectangle, LEFT * 9)
        self.play(Create(first_circle), Create(new_first_rectangle))
        self.wait(1)
        radius = Line(first_circle.get_center(), [first_circle.get_x(), first_circle.get_height()/2, first_circle.get_z()])
        self.play(Create(radius))
        self.wait(1)
        rectangle_label = MathTex("r")
        rectangle_label.next_to(radius, LEFT)
        circle_label = MathTex("r")
        circle_label.next_to(new_first_rectangle, LEFT)
        self.play(Write(rectangle_label), Write(circle_label))



#
if __name__ == '__main__':
    import subprocess
    subprocess.run(['manim', '-p', '-qh', __file__, 'Disk'])