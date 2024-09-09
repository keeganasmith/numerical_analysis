import numpy as np
NUM_ITER = 20
my_jacobian = np.array([[0, 2, 3, 0], [4, 0, 6, 0], [7, 8, 0, 0], [0, 0 , 0, 0]])
my_f = np.array([[0], [0], [0], [0]])
def compute_jacobian_matrix(x_vector):
    my_jacobian[0][0] = 1 - x_vector[3][0]
    my_jacobian[0][3] = -x_vector[0][0]
    my_jacobian[1][1] = 5 - x_vector[3][0]
    my_jacobian[1][3] = -x_vector[1][0]
    my_jacobian[2][2] = 10 - x_vector[3][0]
    my_jacobian[2][3] = -x_vector[2][0]
    my_jacobian[3][0] = 2 * x_vector[0][0]
    my_jacobian[3][1] = 2 * x_vector[1][0]
    my_jacobian[3][2] = 2 * x_vector[2][0]
def compute_f(x_vector):
    my_f[0][0] = x_vector[0][0] + 2 * x_vector[1][0] + 3 * x_vector[2][0] - x_vector[3][0] * x_vector[0][0]
    my_f[1][0] = 4 * x_vector[0][0] + 5 * x_vector[1][0] + 6 * x_vector[2][0] - x_vector[3][0] * x_vector[1][0]
    my_f[2][0] = 7 * x_vector[0][0] + 8 * x_vector[1][0] + 10 * x_vector[2][0] - x_vector[3][0] * x_vector[2][0]
    my_f[3][0] = x_vector[0][0]**2 + x_vector[1][0]**2 + x_vector[2][0]**2 - 1

def iterate(initial_x):
    for i in range(0, NUM_ITER):
        compute_jacobian_matrix(initial_x)
        compute_f(initial_x)
        initial_x = initial_x + np.linalg.solve(my_jacobian, -my_f)
        
    return initial_x
    
if __name__ == "__main__":
    result = iterate(np.array([[0], [0.5], [1], [10]]))
    print("eigen vector 1: ", result)