import numpy as np
import random
from multiprocessing import Process, Manager
NUM_ITER = 500
def compute_jacobian_matrix(x_vector):
    my_jacobian = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    x_1 = x_vector[0][0]
    x_2 = x_vector[1][0]
    x_3 = x_vector[2][0]
    my_jacobian[0][0] = 2 - 6 * x_1 * x_3
    my_jacobian[0][2] = -3 * x_2**2 + 1
    my_jacobian[1][1] = 2 + 2 * x_3
    my_jacobian[1][2] = 2 * x_2
    my_jacobian[2][0] = 3 * x_1**2 - 1
    my_jacobian[2][1] = -2 * x_2
    return my_jacobian
def compute_f(x_vector):
    my_f = np.array([[0], [0], [0]])
    x_1 = x_vector[0][0]
    x_2 = x_vector[1][0]
    x_3 = x_vector[2][0]
    my_f[0][0] = x_1**3 + x_2 * x_3 - 2 * x_1 * x_2
    my_f[1][0] = x_2 + x_1 * x_3 - x_1**2
    my_f[2][0] = x_3 + x_1 * x_2
    return my_f
def iterate(initial_x):
    for i in range(0, NUM_ITER):
        jacobian = compute_jacobian_matrix(initial_x)
        my_f = compute_f(initial_x)
        initial_x = initial_x + np.linalg.solve(jacobian, -my_f)
    return initial_x
def perform_iteration(i, start, end, batch_size, lock, global_solutions):
    results = []
    for i in range(0, batch_size):
        j = random.uniform(start, end)
        k = random.uniform(start, end)
        l = random.uniform(start, end)
        try:
            result = tuple(iterate(np.array([[j], [k], [l]])).flatten())
            
            results.append(result)
        except Exception as e:
            continue
    with lock:
        global_solutions.extend(results)
def f(x_tuple):
    x_1 = x_tuple[0]
    x_2 = x_tuple[1]
    return (x_1**2 + (x_2 - 1/2)**2)**(1/2)
if __name__ == "__main__":
    start = -100
    end = 100
    num_cores = 192
    batch_size = 10000
    num_attempts = num_cores
    processes = []
    manager = Manager()
    global_solutions = manager.list()
    lock = manager.Lock()
    for i in range(0, num_cores):
        p = Process(target = perform_iteration, args=(i, start, end, batch_size, lock, global_solutions))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    smallest = 999999999
    smallest_sol = None
    for solution in global_solutions:
        result = f(solution)
        if(result < smallest):
            smallest_sol = solution
            smallest = result
    
    print(f"smallest value obtained was {smallest} at {smallest_sol}")