import random
import matplotlib.pyplot as plt
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def magnitude(self):
        return (self.real**2 + self.imaginary**2) ** .5
    def add(a, b):
        return Complex(a.real + b.real, a.imaginary + b.imaginary)
    def square(a):
        return Complex(a.real**2 - a.imaginary**2, 2 * a.real * a.imaginary)
def w(z):
    one = Complex(1, 0)
    z_square = Complex.square(z)
    z_square_term = Complex(1/2 * z_square.real, 1/2 * z_square.imaginary)
    result = Complex.add(one, Complex.add(z_square, z_square_term))
    return result
def magnitude(z):
    return w(z).magnitude()

def plot(bad_points, good_points):
    plt.scatter(*zip(*good_points), color='blue', label='Good Points', alpha=0.6)
    plt.scatter(*zip(*bad_points), color='red', label='Bad Points', alpha=0.6)
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.legend()
    plt.title("Scatter Plot of Good and Bad Points")
    plt.show()
    return

def generate_points(real_interval, imag_interval, num_points):
    result = []
    for i in range(0, num_points):
        real = random.uniform(real_interval[0], real_interval[1])
        imag = random.uniform(imag_interval[0], imag_interval[1])
        result.append([real, imag])
    return result

def main():
    real_interval = [-1, 1]
    imag_interval = [-2, 2]
    num_points = 100000
    points = generate_points(real_interval,imag_interval,  num_points)
    good_points = []
    bad_points = []
    for i in range(0, len(points)):
        my_complex = Complex(points[i][0], points[i][1])
        my_magnitude = magnitude(my_complex)
        if(my_magnitude < 1):
            good_points.append(points[i])
        else:
            bad_points.append(points[i])
    plot(bad_points, good_points)

if __name__ == "__main__":
    main()
    