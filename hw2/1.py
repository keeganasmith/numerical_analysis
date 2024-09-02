import math;
NUM_ITER = 6
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
def compute(initial_x, function, f_function):
    result = "\\begin{tabular}{|c|c|c|c|}\n"
    result += "\\hline\n"
    result += "Iteration & Approximation & Residual\\\\\n"
    result += "\\hline\n"
    curr_approx = initial_x
    residual = f_function(curr_approx)
    
    for i in range(0, NUM_ITER):
        result += f"{i} & {curr_approx:.6e} & {residual:.6e}\\\\\n"
        result += "\\hline\n"
        curr_approx = function(curr_approx)

        residual = f_function(curr_approx)
    result += "\\end{tabular}\n"

    return result
    #return approx;
function_mapping = {
    "f" : f,
    "g1": g1,
    "g2": g2
}
if __name__ == "__main__":
    initial_num = float(input("enter initial num: "))
    my_func = input("enter the name of the function (g): ")
    my_func_2 = input("enter the name of the function (f): ")
    result = compute(initial_num, function_mapping[my_func], function_mapping[my_func_2])
    print(result)