import  sys         as so
import  numpy       as np
from    numpy       import *

# Revisa si el valor es cero
def is_a_zero (number) :
    return fabs(number) < 1.0e-12


# Cambia las filas de la matriz
def change_row (current_row, new_row, matrix) :
    aux_row = np.matrix(matrix[current_row, :])
    matrix[current_row, :] = matrix[new_row, :]
    matrix[new_row] = aux_row
    return matrix


# Revisa si hay filas en ceros
def get_rows_zeros_and_non_zero_indices (matrix) :
    (n, m)              = matrix.shape
    zero_indices        = []
    non_zero_indices    = []
    
    for k in range (n - 1) :
        (index, _) = get_non_zero_element(matrix[k, :])
        if (index == -1) :
            zero_indices.append(k)
        else :
            non_zero_indices.append(k)
    return (zero_indices, non_zero_indices)


def move_rows_zeros (zero_indices, non_zero_indices, matrix_a, matrix_b) :
    aux_i = len(non_zero_indices) - 1

    for index in zero_indices : 
        print("index: ", index)
        print("matrix_a[", index, ":]: ", matrix_a[index, :])
        print("aux_i: matrix_a[", non_zero_indices[aux_i], ":]: ", matrix_a[non_zero_indices[aux_i], :])
        
        aux_row_a = matrix_a[index, :]
        matrix_a[index, :] = matrix_a[non_zero_indices[aux_i], :]
        matrix_a[non_zero_indices[aux_i], :] = aux_row_a

        aux_row_b = matrix_b[index, :]
        matrix_b[index, :] = matrix_b[non_zero_indices[aux_i], :]
        matrix_b[non_zero_indices[aux_i], :] = aux_row_b
        aux_i -= 1

    return matrix_a, matrix_b


# Normaliza la fila de la matriz
def normalize_row (factor, row) :
    for i in range(len(row)) :
        row[i] = float(row[i] / factor)
    return row


# Obtiene el elemento no zero de la fila
# return (index, element)
def get_non_zero_element (row) : 
    for index in range(len(row)) : 
        element = row[index]
        if (not is_a_zero(element)) : 
            return (index, element)

    return (-1, 0)


# Obtiene el rango de la matriz
def get_matrix_range (matrix) :
    range_matrix    = 0
    (n, m)          = matrix.shape
    for i in range(n) :
        for j in range(m) :
            if (fabs(matrix[i, j]) != 0) :
                range_matrix += 1
                break
                
    return range_matrix


def get_complete_solution (index, a_row, b_matrix_element) :
    aux_sum = 0
    # print("LEN_A_ROW: ", len(a_row))
    for i in range(index + 1, len(a_row)) :
        # print("a_row: ", a_row[i])
        aux_sum += a_row[i]
    return (b_matrix_element - aux_sum) / a_row[index]


def print_solutions (solutions, numb_excercise) : 
    print("Las soluciones del ejercicio", numb_excercise, "son: \n", solutions)
    
