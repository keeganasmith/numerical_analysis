import numpy as np
import matplotlib.pyplot as plt
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

def get_x_coords(interval, num_points):
    start = interval[0];
    orig_start = start
    end = interval[1];
    result = [];
    result.append(start);
    while(start < end):
        start += (end - orig_start) / (num_points - 1)
        result.append(start)
    return result;

def main():
    x_coords = get_x_coords([-1, 1], 5);
    actual_function_values = []
    for x in x_coords:
        actual_function_values.append([x, f(x)]);

    x_plot = np.linspace(-1, 1, 1000)
    y_actual = []
    y_interp = []
    for i in range(0, len(x_plot)):
        y_actual.append(f(x_plot[i]));
        y_interp.append(lagrange(x_plot[i], actual_function_values));
    
    plt.plot(x_plot, y_actual, label='Actual Function f(x)')
    plt.plot(x_plot, y_interp, '--', label='Lagrange Interpolation')
    plt.scatter(x_coords, [f(x) for x in x_coords], color='red', label='Interpolation Nodes')
    plt.title('Lagrange Interpolation vs Actual Function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()
if __name__ == "__main__":
    main();