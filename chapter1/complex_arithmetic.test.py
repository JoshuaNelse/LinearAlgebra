import unittest
from chapter1.complex_arithmetic import complex_add, complex_multiply

class ComplexArithmetic(unittest.TestCase):

    def test_complex_addition(self):
        # (a+bi)+(c+di) = (a+c)+(b+d)i
        tests = [
            ("(3+4i)+(1+2i)", "4+6i"),
            # Negative numbers
            ("(3+4i)+(-1-2i)", "2+2i"),
            ("(-3-4i)+(1+2i)", "-2-2i"),
            ("(-3-4i)+(-1-2i)", "-4-6i"),
            # Zero cases
            ("(0+0i)+(5+3i)", "5+3i"),
            ("(5+3i)+(0+0i)", "5+3i"),
            ("(0+0i)+(0+0i)", "0+0i"),
            # Real-only numbers (imaginary part is 0)
            ("(5+0i)+(3+0i)", "8+0i"),
            ("(5+0i)+(-3+0i)", "2+0i"),
            # Imaginary-only numbers (real part is 0)
            ("(0+2i)+(0+3i)", "0+5i"),
            ("(0+5i)+(0-3i)", "0+2i"),
            # Mixed positive and negative
            ("(5-3i)+(2+7i)", "7+4i"),
            ("(-5+3i)+(2-7i)", "-3-4i"),
            # Result with zero real or imaginary part
            ("(3+4i)+(-3+2i)", "0+6i"),
            ("(3+4i)+(2-4i)", "5+0i"),
        ]
        for test in tests:
            self.assertEqual(test[1], complex_add(test[0]))

    def test_complex_multiplication(self):
        # (a+bi)*(c+di) = (ac-bd)+(ad+bc)i
        tests = [
            # Basic multiplication
            ("(3+4i)*(1+2i)", "-5+10i"),
            ("(2+3i)*(4+5i)", "-7+22i"),
            # Negative numbers
            ("(3+4i)*(-1-2i)", "5-10i"),
            ("(-3-4i)*(1+2i)", "5-10i"),
            ("(-3-4i)*(-1-2i)", "-5+10i"),
            # Zero cases
            ("(0+0i)*(5+3i)", "0+0i"),
            ("(5+3i)*(0+0i)", "0+0i"),
            ("(0+0i)*(0+0i)", "0+0i"),
            # Multiplication by 1
            ("(1+0i)*(5+3i)", "5+3i"),
            ("(5+3i)*(1+0i)", "5+3i"),
            # Real-only numbers
            ("(5+0i)*(3+0i)", "15+0i"),
            ("(5+0i)*(-3+0i)", "-15+0i"),
            # Imaginary-only numbers
            ("(0+2i)*(0+3i)", "-6+0i"),  # i*i = -1, so 2i*3i = 6i² = -6
            ("(0+5i)*(0-3i)", "15+0i"),  # 5i*(-3i) = -15i² = 15
            # Mixed positive and negative
            ("(5-3i)*(2+7i)", "31+29i"),
            ("(-5+3i)*(2-7i)", "11+41i"),
            # Multiplication by i (rotating by 90 degrees)
            ("(3+4i)*(0+1i)", "-4+3i"),
            ("(5-2i)*(0+1i)", "2+5i"),
            # Results with zero real or imaginary part
            ("(2+3i)*(3-2i)", "12+5i"),
            ("(1+1i)*(1-1i)", "2+0i"),  # Conjugate multiplication
        ]
        for test in tests:
            self.assertEqual(test[1], complex_multiply(test[0]))


if __name__ == '__main__':
    unittest.main()
