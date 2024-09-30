import numpy as np
import matplotlib.pyplot as plt
import math
def lagrange(x, points):
    lagrange_results = [];
    for i in range(0, len(points)):
        numerator = 1;
        denominator = 1;
        for j in range(0, len(points)):
            if(i == j):
                continue;
            numerator *= (x - points[j][0]);
            denominator *= (points[i][0] - points[j][0]);
        lagrange_results.append(numerator / denominator);
    result = 0;
    for i in range(0, len(points)):
        result += points[i][1] * lagrange_results[i]
    return result;

def f(x):
    return 1 / (1 + 25 * x**2);
def g(x):
    return (abs(x)) ** (1/2);

def compute_cheby_points(n):
    x_coords = [];
    for i in range(0, n):
        x_coords.append(math.cos((2* i + 1) * math.pi / (2*(n - 1) + 2)))
    return x_coords;
def get_x_coords(interval, num_points):
    start = interval[0];
    orig_start = start
    end = interval[1];
    result = compute_cheby_points(num_points)
    
    return result;
def do_the_thing(my_function, n):
    x_coords = get_x_coords([-1, 1], n);
    actual_function_values = []
    for x in x_coords:
        actual_function_values.append([x, my_function(x)]);

    x_plot = np.linspace(-1, 1, 1000)
    y_actual = []
    y_interp = []
    for i in range(0, len(x_plot)):
        y_actual.append(my_function(x_plot[i]));
        y_interp.append(lagrange(x_plot[i], actual_function_values));
    
    plt.plot(x_plot, y_actual, label=f'Actual Function {my_function.__name__}(x)')
    plt.plot(x_plot, y_interp, '--', label='Lagrange Interpolation')
    plt.scatter(x_coords, [my_function(x) for x in x_coords], color='red', label='Interpolation Nodes')
    plt.title(f'Lagrange Interpolation vs Actual Function, n = {n}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
def main():
    functions = [f, g]
    nums = [5, 8, 20]
    for function in functions:
        for num in nums:
            do_the_thing(function, num)
if __name__ == "__main__":
    main();