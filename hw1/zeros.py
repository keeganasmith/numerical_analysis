import math
NUM_ITERATIONS = 15
ACTUAL = 2**(1/3)

def f(x):
    return x**3 - 2;
def f_p(x):
    return 3 * (x **2); 
def g1(x):
    return x - f(x) / 3;
def g2(x):
    if(x**2 == 0):
        return math.inf
    return 2/ (x**2)
def g3(x):
    return x - f(x) / f_p(x)
function_mapping = {
    "g1": g1,
    "g2": g2,
    "g3": g3
}

def evaluate(function_name : str):
    result = "\\begin{tabular}{|c|c|c|c|}\n"
    result += "\\hline\n"
    result += "Iteration & Approximation & Residual & Error \\\\\n"
    result += "\\hline\n"
    my_function = function_mapping[function_name]
    curr_approx = 1.5
    residual = f(curr_approx)
    error = abs(curr_approx - ACTUAL)
    for i in range(0, NUM_ITERATIONS + 1):
        result += f"{i} & {curr_approx:.6e} & {residual:.6e} & {error:.6e} \\\\\n"
        result += "\\hline\n"
        curr_approx = my_function(curr_approx)
        residual = f(curr_approx)
        error = abs(curr_approx - ACTUAL)
    result += "\\end{tabular}\n"

    return result

if __name__ == "__main__":
    function_to_analyze = input()
    print(evaluate(function_to_analyze))