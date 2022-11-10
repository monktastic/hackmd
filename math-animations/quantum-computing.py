from manim import *
from math import *
from operator import add


# If you've ever heard of quantum computing, you've probably been told that it somehow speeds things up by exponentially
# parallelizing computation. But this explanation is badly misleading. So, let's try to correct it.

class Quantum1(Scene):
    def construct(self):
        scratch = Text('')
        self.add(scratch)

        # We'll start with a normal, classical bit, which can be in one of two states: 0 or 1.
        bit = Text(r'1 bit: {0, 1}', font_size=24, t2c={'1 bit:': BLUE})
        self.play(Transform(scratch, bit))
        self.wait(5)

        # Three such bits can represent 2 x 2 x 2...
        three_bit_cross_product = Text(r'3 bits: {0, 1} x {0, 1} x {0, 1}', font_size=24, t2c={'3 bits:': BLUE})
        self.play(Transform(scratch, three_bit_cross_product))
        self.wait(3)

        # Or *eight* possible values. For shorthand, we will write those values in base 10.
        three_bits = Text(r'3 bits: {000, 001, 010, 011, 100, 101, 110, 111}', font_size=24, t2c={'3 bits:': BLUE})
        self.play(Transform(scratch, three_bits))
        self.wait(5)

        # A classical three-bit variable -- or register -- will contain only ONE of those values.
        three_bits_dec = Text(r'3 bits: {0, 1, 2, 3, 4, 5, 6, 7}', font_size=24, t2c={'3 bits:': BLUE})
        self.play(Transform(scratch, three_bits_dec))
        self.wait(6)

        # For example, it might contain 5. Three *quantum* bits -- or qubits --
        three_bit_var = Text(f'3-bit variable: 5', font_size=24, t2c={'3-bit variable:': BLUE})
        self.play(Transform(scratch, three_bit_var))
        self.wait(5)

        # will contain a superposition of all 8 possibilities at the same time. We represent this as a vector with 8
        # entries.
        three_qubit_tuple = MathTex(r"(a, b, c, d, e, f, g, h)", color=RED, font_size=40)
        self.play(Transform(scratch, three_qubit_tuple))
        self.wait(6)

        # which correspond to the 8 possible results.
        three_qubit_results = Text(r'0  1  2  3  4  5  6  7', font_size=30).shift(DOWN)
        self.play(FadeIn(three_qubit_results))
        self.wait(3)

        # In quantum mechanics, when you observe the value of a variable, it
        self.wait(3)
        self.play(FadeOut(three_qubit_results))

        # "collapses" into just one of the possible results. For example, we might get back value 3.
        three_qubit_one_result = Text(r'         3          ', font_size=30).shift(DOWN)
        self.play(FadeIn(three_qubit_one_result))
        self.wait(5)
        self.play(FadeOut(three_qubit_one_result))

        # Which value we get is random, and the probability of getting any one result is given by the square of the
        # corresponding entry. For example, the probability of getting result 3 is given by d^2.
        self.play(FadeIn(three_qubit_results))
        self.wait(8)
        d_squared = MathTex(r"d^2", font_size=40).shift(DOWN * 2)
        self.play(FadeIn(d_squared))
        self.wait(3)
        self.play(FadeOut(d_squared))

        # If we have this vector, then the probability of results 1, 3, 5, or 7 are each 25%.
        three_qubit_tuple = MathTex(
            r"(0, \frac{1}{2}, 0, \frac{1}{2}, 0, \frac{1}{2}, 0, \frac{1}{2})",
            color=RED, font_size=40)
        self.play(Transform(scratch, three_qubit_tuple))
        self.wait(3)

        half_squared = MathTex(r"{(\frac{1}{2})}^2 = 25\%", font_size=40).shift(DOWN * 2)
        self.play(FadeIn(half_squared))
        self.wait(3)
        self.play(FadeOut(half_squared))

        # In general, these entries can be complex numbers, but for simplicity, here we will stick to real numbers.
        self.wait(7)

        # Negative numbers are also allowed.
        three_qubit_tuple = MathTex(
            r"(0, \frac{1}{2}, 0, \frac{-1}{2}, 0, \frac{1}{2}, 0, \frac{-1}{2})",
            color=RED, font_size=40)
        self.play(Transform(scratch, three_qubit_tuple))
        self.wait(2)

        # Notice that squaring a negative number still gives a positive probability.
        half_squared = MathTex(r"{(\frac{-1}{2})}^2 = 25\%", font_size=40).shift(DOWN * 2)
        self.play(FadeIn(half_squared))
        self.wait(3)
        self.play(FadeOut(half_squared))

        # Because the squares give probabilities, they must sum to one.
        pythag1 = MathTex(r'a^2 + b^2 + c^2 + d^2 + e^2 + f^2 + g^2 + h^2 = 1').shift(DOWN * 2)
        self.add(pythag1)
        self.wait(3)

        # And recall from the Pythagorean theorem that the sum of the squares of the entries gives you the
        # length-squared of the whole vector.
        pythag2 = MathTex(r'a^2 + b^2 + c^2 + d^2 + e^2 + f^2 + g^2 + h^2 = {\lVert v \rVert}^2').shift(DOWN * 2)
        self.play(Transform(pythag1, pythag2))
        self.wait(7)

        # Together, this means that the vector must have length 1. We will see the importance of this later.
        length_one = MathTex(r"1 = {\lVert v \rVert}").shift(DOWN * 2)
        self.play(Transform(pythag1, length_one))
        self.wait(6)


class Quantum2(Scene):
    def construct(self):
        # There's another way we can visualize vectors which may seem a little strange at first.
        some_vec = MathTex(r"(0, \frac{1}{2}, 0, \frac{-1}{2}, 0, \frac{1}{2}, 0, \frac{-1}{2})", font_size=40) \
            .shift(DOWN * 3)
        self.add(some_vec)
        self.wait(4)

        # We can plot them on a line chart.
        x_range = [0, 8, 1]
        y_range = [-1, 1, 0.2]
        plane = NumberPlane(x_range=x_range, x_length=10, y_range=y_range, y_length=4)
        plane.add_coordinates(np.arange(*x_range), np.arange(*y_range))
        scratch_graph = plane.plot(lambda t: 0, color=WHITE)

        self.add(plane)
        self.add(scratch_graph)

        x = [0, 1, 2, 3, 4, 5, 6, 7]
        y = [0, 0.5, 0, -0.5, 0, 0.5, 0, -0.5]
        line_graph = plane.plot_line_graph(x, y)
        self.play(Transform(scratch_graph, line_graph))
        self.wait(2)

        # Notice how this looks like a pixellated sine wave.
        sin_func = plane.plot(lambda t: 0.5 * np.sin(PI / 2.0 * t))
        self.play(FadeIn(sin_func))
        self.wait(2)
        self.play(FadeOut(sin_func))

        # The more qubits we have, the closer our approximation can get.
        x2 = list(np.arange(0, 8, 0.5))
        y2 = list(map(lambda x: 0.5 * sin(pi / 2.0 * x), x2))
        line_graph2 = plane.plot_line_graph(x2, y2, line_color=PINK)
        self.play(Transform(scratch_graph, line_graph2))
        self.wait(6)

        # But let's stick to three for now.
        self.play(Transform(scratch_graph, line_graph))
        self.wait(1)

        # You've probably heard of the wave-particle duality in quantum physics. Well, this is such a wave.
        # When you observe its value ...
        self.wait(9)

        # it collapses to one result. This is analogous to finding a localized particle.
        delta_func = plane.plot(lambda t: 1 if (t == 3) else 0, color=RED)
        self.play(Transform(scratch_graph, delta_func))
        self.wait(5)

        # Waves can also interfere. To see how that happens, let's go back to our vector component representation.
        self.wait(8)


class Quantum3(Scene):
    def construct(self):
        scratch = Text('')
        self.add(scratch)

        # This time, we will write our vector in column form.
        v_col = MathTex(r'\begin{bmatrix} v_0 \\ v_1 \\ v_2 \\ v_3 \\ v_4 \\ v_5 \\ v_6 \\ v_7 \end{bmatrix}')
        self.play(Transform(scratch, v_col))
        self.wait(3)

        # We can multiply this on the left by an 8x8 matrix M.
        m = MathTex(r'M_{8x8}', font_size=50, color=RED)
        group = VGroup(m, MathTex(r'\times'), v_col).arrange(RIGHT)
        self.play(Transform(scratch, group))
        self.wait(4)

        # The result will be a new 8-component vector w.
        w_col = MathTex(r'\begin{bmatrix} w_0 \\ w_1 \\ w_2 \\ w_3 \\ w_4 \\ w_5 \\ w_6 \\ w_7 \end{bmatrix} = \vec{w}',
                        color=PINK)
        group = VGroup(m, MathTex(r'\times'), v_col, MathTex('='), w_col).arrange(RIGHT)
        self.play(Transform(scratch, group))
        self.wait(4)

        # A remarkable fact about our universe is that ALL physical laws are ultimately expressed at the quantum level
        # as rotation matrices (or really, their complex equivalents, called unitary matrices). That deserves its own
        # video. For now, just notice that rotating a vector doesn't change its length.
        self.wait(12)
        self.remove(scratch)

        # That's important, because the length must remain one so that the probabilities still add to one.
        plane = NumberPlane()
        vector_1 = Vector([3, 0], color=RED)
        vector_2 = Vector([3 * sqrt(2)/2, -3 * sqrt(2)/2], color=GREEN)
        vec_group = VGroup(vector_1, vector_2)
        self.add(plane, vec_group)
        self.wait(3)
        self.play(Rotate(vec_group, angle=2*PI, about_point=ORIGIN, run_time=4))
        self.wait(2)
        self.remove(plane, vec_group)

        # Now, linear algebra tells us that we can break this product down into the sum of 8 products.
        m = MathTex(r'M', font_size=50, color=RED)
        v0_prod = MathTex(r'M \times \begin{bmatrix} v_0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}', color=BLUE)
        v1_prod = MathTex(r'M \times \begin{bmatrix} 0 \\ v_1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}', color=PINK)
        v7_prod = MathTex(r'M \times \begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ v_7 \end{bmatrix}', color=YELLOW)
        group = VGroup(m, MathTex(r'\times'), v_col, MathTex('='), v0_prod, MathTex('+'), v1_prod, MathTex('+'),
                       MathTex(r'...'), MathTex('+'), v7_prod).arrange(RIGHT)
        self.play(FadeIn( group))
        self.wait(7)

        # And this operation is implemented efficiently by quantum mechanics. So it's *kind* of like we're doing 8
        # computations at the same time.
        self.wait(9)

class Quantum3b(Scene):
    def construct(self):
        # If we had four qubits, that would be like parallelizing 2^4 or 16 computations.
        pow = MathTex(r'2^4 = 16', font_size=50)
        self.add(pow)
        self.wait(7)
        self.remove(pow)

        # With 5, that's 32, and so on.
        pow = MathTex(r'2^5 = 32', font_size=50)
        self.add(pow)
        self.wait(1)
        self.remove(pow)

        pow = MathTex(r'2^6 = 64', font_size=50)
        self.add(pow)
        self.wait(1)
        self.remove(pow)

        pow = MathTex(r'2^7 = 128', font_size=50)
        self.add(pow)
        self.wait(1)
        self.remove(pow)

        pow = MathTex(r'2^{100} = 1,267,650,600,228,229,401,496,703,205,376', font_size=40)
        self.add(pow)
        self.wait(1)

        # This is why people say that quantum computers work through exponential parallelism. With just 100 qubits,
        # that value is around 10^30. But this is badly misleading. First, we can only parallelize a very specific
        # kind of multiplication. More importantly, when you try to read the result, you only get
        self.wait(17)
        self.remove(pow)

        # ONE of the values! What good is parallelism if you have to throw away almost all of the results?
        self.add(MathTex(r'1', font_size=100))
        self.wait(7)

        # So "exponential parallelism" is a terrible explanation. There's something much more interesting going on.
        self.wait(7)


class Quantum4(Scene):
    def construct(self):
        scratch = Text('')
        self.add(scratch)

        # Suppose that M times this input vector gives us some result, which we can view as a wave.
        m = MathTex(r'M', font_size=50, color=RED)
        v0_str = r'\begin{bmatrix} v_0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}'
        v0 = MathTex(v0_str, color=BLUE)

        x_range = [0, 8, 1]
        y_range = [-1, 1, 0.2]
        plane = NumberPlane(x_range=x_range, x_length=10, y_range=y_range, y_length=4)
        plane.add_coordinates(np.arange(*x_range), np.arange(*y_range))

        x = [0, 1, 2, 3, 4, 5, 6, 7]
        y0 = [0, 0.5, 0, -0.5, 0, 0.5, 0, -0.5]
        line_graph0 = plane.plot_line_graph(x, y0, line_color=RED)
        graph_group = VGroup(plane, line_graph0)

        group = VGroup(m, MathTex(r'\times'), v0, MathTex('='), graph_group).arrange(RIGHT)
        self.play(Transform(scratch, group))
        self.wait(6)

        # Similarly, multiplying by this vector gives us a different wave.
        v1_str = r'\begin{bmatrix} 0 \\ v_1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}'
        v1 = MathTex(v1_str, color=BLUE)

        y1 = [0.5, -0.5, .5, -0.5, 0.5, -0.5, 0.5, -0.5]
        line_graph1 = plane.plot_line_graph(x, y1, line_color=GREEN)
        graph_group = VGroup(plane, line_graph1)

        group = VGroup(m, MathTex(r'\times'), v1, MathTex('='), graph_group).arrange(RIGHT)
        self.play(Transform(scratch, group))
        self.wait(5)

        # If we multiply by the sum of those two vectors, the result will be the sum of the two waves.
        v01_str = r'\begin{bmatrix} v_0 \\ v_1 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \\ 0 \end{bmatrix}'
        v01 = MathTex(v01_str, color=BLUE)
        graph_ind_group = VGroup(plane, line_graph0, line_graph1)

        ind_group = VGroup(m, MathTex(r'\times'), v01, MathTex('='), graph_ind_group).arrange(RIGHT)
        self.play(Transform(scratch, ind_group))
        self.wait(5)

        # The waves will add like so.
        y_sum = list(map(add, y0, y1))
        line_graph01 = plane.plot_line_graph(x, y_sum, line_color=YELLOW)
        graph_sum_group = VGroup(plane, line_graph01)
        sum_group = VGroup(m, MathTex(r'\times'), v01, MathTex('='), graph_sum_group).arrange(RIGHT)
        self.play(Transform(scratch, sum_group))
        self.wait(3)

        # Let's rewind and look at the two waves individually.
        self.play(Transform(scratch, ind_group))
        self.wait(3)

        # Notice how in some places, the red and green waves will cancel each other out --- like at positions 1 and 5.
        # In other places, they will amplify each other like at positions 3 and 7.
        self.wait(15)
        self.play(Transform(scratch, sum_group))

        # This is constructive and destructive wave interference, like in the famous two-slit experiment.
        self.wait(6)

        # It only works because values are allowed to be negative. And *that* is only possible because of the
        # nature of QM.
        v = MathTex(r'\begin{bmatrix} v_0 \\ v_1 \\ v_2 \\ v_3 \\ v_4 \\ v_5 \\ v_6 \\ v_7 \end{bmatrix}')
        y_v = [0.1, -0.1, -0.1, 0.9, 0.1, -0.1, -0.1, 0]
        line_graph_v = plane.plot_line_graph(x, y_v, line_color=ORANGE)
        graph_group = VGroup(plane, line_graph_v)
        sum_group = VGroup(m, MathTex(r'\times'), v, MathTex('='), graph_group).arrange(RIGHT)
        self.play(Transform(scratch, sum_group))
        self.wait(5)


class Quantum5(Scene):
    def construct(self):
        scratch = Text(' ')

        self.add(scratch)

        # So how can we use these facts to design a quantum algorithm? First, what *is* a quantum algorithm?
        self.wait(7)

        # It's actually just a sequence of such matrices.
        m1 = MathTex(r'M_1', font_size=50, color=RED)
        m2 = MathTex(r'M_2', font_size=50, color=GREEN)
        m3 = MathTex(r'M_3', font_size=50, color=BLUE)
        mult_group = VGroup(m1, MathTex(r'\times'), m2, MathTex(r'\times'), m3).arrange(RIGHT)
        self.play(FadeIn(mult_group))
        self.wait(3)
        self.play(FadeOut(mult_group))

        # What should this sequence do? Let's say your algorithm gets some input which we encode as vector v.
        v = MathTex(r'\begin{bmatrix} v_0 \\ v_1 \\ v_2 \\ v_3 \\ v_4 \\ v_5 \\ v_6 \\ v_7 \end{bmatrix}')
        self.play(FadeIn(v))
        self.wait(6)
        self.play(FadeOut(v))

        # And let's say that the correct answer for this particular input is the number 4. This means that your quantum
        # algorithm should produce something close to this output.
        res = MathTex(r'\begin{bmatrix} 0 \\ 0 \\ 0 \\ 0 \\ 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}', color=BLUE)
        self.play(FadeIn(res))
        self.wait(8)

        # Such a vector would collapse to position 4 with near 100% probability when measured.
        self.wait(5)
        self.play(FadeOut(res))

        # In other words, when we multiply our sequence of matrices by this input, we should get something close to this output.
        mult_group = VGroup(m1, MathTex(r'\times'), m2, MathTex(r'\times'), m3, MathTex(r'\times'), v, MathTex(r'\approx'),
                            res).arrange(RIGHT)
        self.play(Transform(scratch, mult_group))
        self.wait(7)

        # Each multiplication can be thought of as creating an interference pattern.
        self.wait(5)

        # At the end, we want the resulting wave to be really sharp, with a peak where the true result should be.
        # Of course, this should work not just for one particular input, but for all of them.
        x_range = [0, 8, 1]
        y_range = [-1, 1, 0.2]
        plane = NumberPlane(x_range=x_range, x_length=5, y_range=y_range, y_length=3)
        plane.add_coordinates(np.arange(*x_range), np.arange(*y_range))
        delta_func = plane.plot(lambda t: 1 if (t == 4) else 0, color=RED)
        graph_group = VGroup(plane, delta_func)

        mult_group = VGroup(m1, MathTex(r'\times'), m2, MathTex(r'\times'), m3, MathTex(r'\times'), v, MathTex(r'\approx'),
                            res, MathTex(r'=')).arrange(RIGHT)
        group = VGroup(mult_group, graph_group).arrange(RIGHT)
        self.play(Transform(scratch, group))
        self.wait(13)

        # Okay, but how do we figure out the right sequence of matrices to make this happen?
        qmark = Text(r'?', font_size=100)
        self.play(Transform(scratch, qmark))
        self.wait(6)

        # The answer is that in general, we don't know! There are only a small handful of specific problems for which
        # anyone has discovered quantum algorithms that require fewer steps than their classical counterparts. Nobody
        # knows of a way to speed up problems *in general*, nor is it believed that we will find a general way to do
        # such a thing.
        qmark = Text(r'!', font_size=100)
        self.play(Transform(scratch, qmark))
        self.wait(26)

# I'll put some links in the description if you want to deep dive into some particular algorithms
# that have been found. I hope this video clears up some of the misconceptions out there.

class Test(Scene):
    def construct(self):
        plane = NumberPlane()
        vector_1 = Vector([3, 0], color=RED)
        vector_2 = Vector([3 * sqrt(2)/2, -3 * sqrt(2)/2], color=GREEN)
        vec_group = VGroup(vector_1, vector_2)
        self.add(plane, vec_group)
        self.wait(2)
        self.play(Rotate(vec_group, angle=2*PI, about_point=ORIGIN))
        self.wait(3)