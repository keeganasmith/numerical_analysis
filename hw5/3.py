from scipy.integrate import newton_cotes
import numpy as np
ACTUAL =  0.5493064 
def f(x):
    return 1/(1 + 2*x)
def n_point_rule(function, interval, n):
    a = interval[0]
    b = interval[1]
    x = np.linspace(a, b, n + 1)
    an, B = newton_cotes(n)
    h = (b - a) / n
    return h * np.sum(an * function(x))
def n3(function, interval): #newton cotes, n=3
    h = (interval[1] - interval[0]) / 3;
    return 3/8 * h * (function(interval[0]) + 3 *function(interval[0] + h) + 3* function(interval[0] + 2*h) + function(interval[1]))
def n4(function, interval):
    h = (interval[1] - interval[0]) / 4;
    a = interval[0]
    return 2/45 * h * (7 * function(a) + 32 * function(a + h) + 12 * function(a + 2 * h) + 32 * function(a + 3* h) + 7 * function(interval[1])) 
def n5(function, interval):
    h = (interval[1] - interval[0]) / 5;
    a = interval[0]
    x_val = a;
    index = 0
    vals =[]
    while(index < 6):
        vals.append(function(x_val))
        x_val += h
        index += 1
    return 5/288 * h * (19* vals[0] + 75 * vals[1] + 50 * vals[2] + 50 * vals[3] + 75 * vals[4] + 19 * vals[5])
def n6(function, interval):
    h = (interval[1] - interval[0]) / 6;
    a = interval[0]
    x_val = a;
    index = 0
    vals =[]
    while(index < 7):
        vals.append(function(x_val))
        x_val += h
        index += 1
    return 1/140 * h * (41* vals[0] + 216 * vals[1] + 27 * vals[2] + 272 * vals[3] + 27 * vals[4] + 216 * vals[5] + 41 * vals[6])
def n7(function, interval):
    h = (interval[1] - interval[0]) / 7;
    a = interval[0]
    x_val = a;
    index = 0
    vals =[]
    while(index < 8):
        vals.append(function(x_val))
        x_val += h
        index += 1
    return 7/17280 * h * (751* vals[0] + 3577 * vals[1] + 1323 * vals[2] + 2989 * vals[3] + 2989 * vals[4] + 1323 * vals[5] + 3577 * vals[6] + 751 * vals[7])
def n8(function, interval):
    h = (interval[1] - interval[0]) / 8;
    a = interval[0]
    x_val = a;
    index = 0
    vals =[]
    while(index < 9):
        vals.append(function(x_val))
        x_val += h
        index += 1
    return 4/14175 * h * (989* vals[0] + 5888 * vals[1] - 928 * vals[2] + 10496 * vals[3] - 4540 * vals[4] + 10496 * vals[5] - 928 * vals[6] + 5888 * vals[7] + 989 * vals[8])
def main():
    interval = [0, 1]
    print("n =3 error: ", abs(n3(f, interval) - ACTUAL))
    print("n=4 error:", abs(n4(f, interval) - ACTUAL))
    print("n=5 error:", abs(n5(f, interval) - ACTUAL))
    print("n=6 error:", abs(n6(f, interval) - ACTUAL))
    print("n=7 error:", abs(n7(f, interval) - ACTUAL))
    print("n=8 error:", abs(n8(f, interval) - ACTUAL))
    for i in range(9, 15):
        print(f"n={i} error:", abs(n_point_rule(f, interval, i)) - ACTUAL)
    
if __name__ == "__main__":
    main()
    
    
