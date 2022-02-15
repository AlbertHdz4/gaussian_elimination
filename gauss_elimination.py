""" Author: Alberto Hernández López """
''' Eliminación Gaussiana con pivoteo parcial '''
from    numpy           import * # Para manejar matrices 
from    utils           import *
from    constants       import *
from    model.colors    import *

import  model.solution


# Metodo de eliminacion gaussiana
def gauss_elimination (A, B, exercise_number = "NA") :
    print("EJERCICIO:", exercise_number)

    # Obtenemos las dimensiones de A
    (n_A, m_A)          = A.shape
    most_left_column    = A[:, 0]

    print("Dimensiones de A: n = ", n_A, " m = ", m_A, "\n")
    print("La matriz A es:\n", A, "\n")

    # Acomodamos la matriz
    for l in range(m_A - 1) :
        if (not is_a_zero(most_left_column[l])) : 
            if (l != 0) : 
                A = change_row(0, l, A)
                B = change_row(0, l, B)
            break

    print("La matriz A acomodada es:\n", A, "\n")
    print("La matriz B acomodada es:\n", B, "\n")

    # Realizamos eliminación hacia adelante
    for row_index in range(n_A - 1) :
        (norm_factor_index, norm_factor) = get_non_zero_element(A[row_index, :])
        
        if (norm_factor_index == -1) : continue

        # Normalizamos la fila - pivote
        A[row_index, :] = normalize_row(norm_factor, A[row_index, :])
        B[row_index, :] = normalize_row(norm_factor, B[row_index, :])

        for nxt_row_index in range(row_index + 1, n_A) :
            factor  = A[nxt_row_index, row_index]
            index   = row_index

            if (factor == 0) : continue

            # Realizamos la eliminación de la fila
            for column_index in range(index, m_A) :
                A[nxt_row_index, column_index] = A[nxt_row_index, column_index] - (A[row_index, column_index] * factor)

            # Realizamos las operaciones en B
            B[nxt_row_index] = B[nxt_row_index] - B[row_index] * factor

        # Realizamos intercambios de filas, en caso de ser una fila de zeros
        (norm_factor_index, _) = get_non_zero_element(A[nxt_row_index, :])

        if (nxt_row_index + 1 > n_A) :
            (norm_factor_index, _)      = get_non_zero_element(A[nxt_row_index, :])
            (nxt_norm_factor_index, _)  = get_non_zero_element(A[nxt_row_index + 1, :])

            if (norm_factor_index > nxt_norm_factor_index) : 
                A = change_row(nxt_row_index, nxt_row_index + 1, A)
                B = change_row(nxt_row_index, nxt_row_index + 1, B)

    
    # Realizamos la normalización de la última fila de la matriz
    (_, norm_factor ) = get_non_zero_element(A[n_A - 1, :])
    if (norm_factor != 0) :
        A[n_A - 1, :] = normalize_row(norm_factor, A[n_A - 1, :])
        B[n_A - 1]    = normalize_row(norm_factor, B[n_A - 1])

    (A, B) = check_final_rows(A, B)

    # Obtenemos el rango de la matriz
    range_A                     = get_matrix_range(A)
    are_there_many_solutions    = (range_A < m_A)

    print("La matriz diagonalizada es:\n", A, "\n")
    print("La matriz B es:\n", B, "\n")

    # Soluciones de la ecuacion, imprimimos las soluciones
    x = zeros(m_A, float)
    if (range_A == m_A) :
        x[m_A - 1] = B[m_A-1] / A[m_A - 1, m_A - 1]
        for i in range(m_A - 2, -1, -1):
            sum_ax = 0
  
            for j in range(i + 1, m_A):
                sum_ax += A[i, j] * x[j]
        
            x[i] = (B[i] - sum_ax) / A[i,i]
        
        print_solutions(x, exercise_number)


    elif (are_there_many_solutions) : # Imprimimos las soluciones infinitas
        print(f"{bcolors.HEADER}Atencion: El sistema de ecuaciones tiene infinitas soluciones.{bcolors.ENDC}")
        print_infinite_solutions(A, B)
        

# Contiene las matrices a resolver de la parte 1 de la tarea
if __name__ == '__main__':
    print(f"{bcolors.OKGREEN}******************** START ********************{bcolors.ENDC}")
    print("\n")
    
    print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    gauss_elimination(m_a_15, m_b_15, 15)
    print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")

    print("\n\n")

    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    # gauss_elimination(m_a_16, m_b_16, 16)
    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")

    # print("\n\n")

    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    # gauss_elimination(m_a_17, m_b_17, 17)
    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")

    # print("\n\n")

    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    # gauss_elimination(m_a_18, m_b_18, 18)
    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")

    # print("\n\n")

    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    # gauss_elimination(m_a_19, m_b_19, 19)
    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")

    # print("\n\n")

    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    # gauss_elimination(m_a_20, m_b_20, 20)
    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")

    # print("\n\n")

    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    # gauss_elimination(m_a_21, m_b_21, 21)
    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")

    # print("\n\n")

    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    # gauss_elimination(m_a_22, m_b_22, 22)
    # print(f"{bcolors.FAIL}----------------------------------------{bcolors.ENDC}")
    
    print(f"{bcolors.OKGREEN}******************** END ********************{bcolors.ENDC}")
