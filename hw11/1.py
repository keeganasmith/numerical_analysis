def back_sub(A, b):
    i = len(A) -1 
    coefficients = [0] * len(b)
    while(i >= 0):
        row_sum = 0
        j = len(A) - 1
        while(j > i):
            row_sum += A[i][j] * coefficients[j]
            j -= 1
        b[i][0] -= row_sum
        coefficients[i] = b[i][0] / A[i][i]
        i -= 1
    return coefficients
def forward_sub(A, b):
    coefficients = [0] * len(A)
    for i in range(0, len(A)):
        sum_row = 0
        for j in range(0, i ):
            sum_row += A[i][j] * coefficients[j]
        result = b[i] - sum_row
        coefficients[i] = result / A[i][i]
    return coefficients
def inner_product(a, b):
    result = 0
    for i in range(0, len(a)):
        result += a[i] * b[i]
    return result
def multiply_by_scalar(a, scalar):
    result = []
    for i in range(0, len(a)):
        result.append(a[i] * scalar)
    return result
def add_vectors(a, b):
    result = []
    for i in range(0, len(a)):
        result.append(a[i] + b[i])
    return result
def norm(a):
    result = 0
    for value in a:
        result += value**2
    return result ** .5
def subtract_vectors(a, b):
    return add_vectors(a, multiply_by_scalar(b, -1))
def gram_sum(i, v, theta, m):
    result = [0] * m
    for k in range(0, i):
        inner = inner_product(v[i], theta[k])
        intermed = multiply_by_scalar(theta[k], inner)
        result = add_vectors(intermed, result)
    return result
def transpose(A):
    result = []
    for i in range(0, len(A[0])):
        result.append([0] * len(A))
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            result[j][i] = A[i][j]
    return result
def gram_schmidt(A):
    w = []
    v = []
    theta = []
    v = transpose(A)    
    m = len(v[0])
    for i in range(0, len(v)):
        print(theta)
        summation = gram_sum(i, v, theta, m)
        w.append(subtract_vectors(v[i], summation))
        print(w)
        w_norm = norm(w[i])
        theta.append(multiply_by_scalar(w[i], 1/w_norm))
    Q = transpose(theta)
    R = []
    for i in range(0, len(v)):
        R.append([0] * len(v))
        R[i][i] = norm(w[i])
        for j in range(i+1, len(v)):
            R[i][j] = inner_product(v[j], theta[i])
    
    return Q, R
def to_string(A):
    result = ""
    for i in range(0, len(A)):
        for j in range(0, len(A[0])):
            result += str(A[i][j]) + " "
        result += "\n"
    return result
def row_col_product(A, B, i, j):
    result = 0
    for k in range(0, len(A[i])):
        
        result += A[i][k] * B[k][j]
    return result
def multiply(A, B):
    result = []
    for i in range(0, len(A)):
        result.append([0] * len(B[0]))
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            result[i][j] = row_col_product(A, B, i, j)
    return result
def convert_matrix_to_latex(A):
    result = "\\begin{bmatrix}\n"
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            result += str(A[i][j]) + " & "
        result += "\\\\\n"
    result += "\\end{bmatrix}\n"
    return result
def solve(Q, R, b):
    Q_transpose = transpose(Q)
    Q_transpose_b = multiply(Q_transpose, b)
    result = convert_matrix_to_latex(Q_transpose_b)
    print(result)
    result = back_sub(R, Q_transpose_b)
    return result
def main():
    A = [
        [1, 1, 2, 3],
        [2, 2, 2, 2], 
        [4, 3, 2, 2],
        [1, 1, 2, 3],
        [3, 1, 2, 3]
    ]
    
    Q, R = gram_schmidt(A)
    print("Q:")
    print(to_string(Q))
    print("R:")
    print(to_string(R))
    print("QR (should be equivalent to A):")
    mult_result = multiply(Q, R)
    print(to_string(mult_result))
    print("Q in latex:")
    print(convert_matrix_to_latex(Q))
    print("R in latex:")
    print(convert_matrix_to_latex(R))
    B = [[2], [5], [7], [2], [3]]
    result = solve(Q, R, B)
    print(result)
    A = [
        [1, 2],
        [1, 2],
        [2, 1]
    ]
    B = [[3], [4], [3]]
    Q, R = gram_schmidt(A)
    result = solve(Q, R, B)
    print(result)
if __name__ == "__main__":
    main()