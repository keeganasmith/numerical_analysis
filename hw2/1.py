import math;
NUM_ITER = 16
EXPECTED = 21**(1/3)
def f(x):
    return math.e**x - x - 1;
def f_prime(x):
    return math.e**x - 1;
def f_double_prime(x):
    return math.e**x;
def g1(x):
    return x - f(x) / f_prime(x);
def g2(x):
    return x - (f(x)*f_prime(x)) / (f_prime(x)**2 - f(x) * f_double_prime(x))
def a(x):
    return (20 * x + 21 / (x**2)) / 21
def b(x):
    return x - (x**3 - 21)/(3 * x**2)
def c(x):
    return x - (x**4 - 21 * x) / (x**2 - 21)
def compute(initial_x, function, f_function = None):
    result = "\\begin{tabular}{|c|c|c|c|}\n"
    result += "\\hline\n"
    result += "Iteration & Approximation & Error\\\\\n"
    result += "\\hline\n"
    curr_approx = initial_x
    error = abs(curr_approx - EXPECTED)
    for i in range(0, NUM_ITER):
        result += f"{i} & {curr_approx:.6e} & {error:.6e}\\\\\n"
        result += "\\hline\n"
        curr_approx = function(curr_approx)
        error = abs(curr_approx - EXPECTED)
    result += "\\end{tabular}\n"

    return result
    #return approx;
function_mapping = {
    "f" : f,
    "g1": g1,
    "g2": g2,
    "a" : a,
    "b" : b,
    "c" : c,
}
if __name__ == "__main__":
    initial_num = float(input("enter initial num: "))
    my_func = input("enter the name of the function: ")
    #my_func_2 = input("enter the name of the function (f): ")
    result = compute(initial_num, function_mapping[my_func])
    print(result)