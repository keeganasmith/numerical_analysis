import numpy as np
import random
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import copy
NUM_ITER = 500
global_solutions = []
lock = threading.Lock()
def compute_jacobian_matrix(x_vector):
    my_jacobian = np.array([[0, 2, 3, 0], [4, 0, 6, 0], [7, 8, 0, 0], [0, 0 , 0, 0]])

    my_jacobian[0][0] = 1 - x_vector[3][0]
    my_jacobian[0][3] = -x_vector[0][0]
    my_jacobian[1][1] = 5 - x_vector[3][0]
    my_jacobian[1][3] = -x_vector[1][0]
    my_jacobian[2][2] = 10 - x_vector[3][0]
    my_jacobian[2][3] = -x_vector[2][0]
    my_jacobian[3][0] = 2 * x_vector[0][0]
    my_jacobian[3][1] = 2 * x_vector[1][0]
    my_jacobian[3][2] = 2 * x_vector[2][0]
    return my_jacobian
def compute_f(x_vector):
    my_f = np.array([[0], [0], [0], [0]])

    my_f[0][0] = x_vector[0][0] + 2 * x_vector[1][0] + 3 * x_vector[2][0] - x_vector[3][0] * x_vector[0][0]
    my_f[1][0] = 4 * x_vector[0][0] + 5 * x_vector[1][0] + 6 * x_vector[2][0] - x_vector[3][0] * x_vector[1][0]
    my_f[2][0] = 7 * x_vector[0][0] + 8 * x_vector[1][0] + 10 * x_vector[2][0] - x_vector[3][0] * x_vector[2][0]
    my_f[3][0] = x_vector[0][0]**2 + x_vector[1][0]**2 + x_vector[2][0]**2 - 1
    return my_f
def iterate(initial_x):
    for i in range(0, NUM_ITER):
        jacobian = compute_jacobian_matrix(initial_x)
        my_f = compute_f(initial_x)
        initial_x = initial_x + np.linalg.solve(jacobian, -my_f)
    return initial_x
def perform_iteration(i, start, end):
    #print("got here")
    j = random.uniform(start, end)
    k = random.uniform(start, end)
    l = random.uniform(start, end)
    m = random.uniform(start, end)
    try:
        result = tuple(iterate(np.array([[j], [k], [l], [m]])).flatten())
        
        return result
    except Exception as e:
        return None
if __name__ == "__main__":
    start = -10
    end = 10
    num_attempts = 10000
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(perform_iteration, i, start, end) for i in range(num_attempts)]
        for future in as_completed(futures):
            result = future.result()
            if(result):
                with lock:
                    global_solutions.append(result)
    while(True):
        result = []
        for i in range(0, 3):
            result.append(np.array(global_solutions[random.randint(0, len(global_solutions))]))
        result = np.array(result)
        eigenvectors = []
        for i in range(0, len(result)):
            eigenvectors.append(result[i][:3])
        determinant = np.linalg.det(eigenvectors)
        if(not (determinant <= 10**(-2) and determinant >= -10**(-2))):
            for i in range(0, len(result)):
                print(f"Solution {i}: ", result[i]) 
            print("determinant was: ", determinant)
            break;
        print("determinant was approx. 0, trying again")