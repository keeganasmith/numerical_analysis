import math;
NUM_ITER = 20
def f(x):
    return math.e**x - x - 1;
def f_prime(x):
    return math.e**x - 1;
def g1(x):
    return x - f(x) / f_prime(x);
def compute(initial_x, function):
    result = ""
    approx = initial_x
    for i in range(0, NUM_ITER):
        result += f"Iteration: {i}, approx: {approx}\n"

        approx = function(approx)
    return result
    #return approx;
function_mapping = {
    "f" : [f, f_prime]
}
if __name__ == "__main__":
    initial_num = float(input("enter initial num: "))
    my_func = input("enter the name of the function: ")
    result = compute(initial_num, function_mapping[my_func][0],function_mapping[my_func][1])
    print(result)