import sys as so
import numpy as np

WELCOME_MSG = "\n---- Programa que resuelve un sistema de ecuaciones lineales mediante el metodo de Eliminacion Gaussiana ----\n"
REINPUT     = "Ingresa de nuevo la dimension de la matriz"
DIMEN_ERROR = "El tamanio de la matriz es erroneo"

# Matrices de los problemas
m_a_15 = np.array([
    [2, 1, 3], 
    [1, 2, 0],
    [0, 1, 1]
    ], float)


m_b_15 = np.array([
    [0], 
    [0],
    [0]
    ], float)


m_a_16 = np.array([
    [2, -1, -3], 
    [-1, 2, -3],
    [1, 1, 4]
    ], float)


m_b_16 = np.array([
    [0], 
    [0],
    [0]
    ], float)


m_a_17 = np.array([
    [3, 1, 1, 1], 
    [5, -1, 1, -1]
    ], float)


m_b_17 = np.array([
    [0], 
    [0]
    ], float)


m_a_18 = np.array([
    [0, 1, 3, -2], 
    [2, 1, -4, 3],
    [2, 3, 2, -1],
    [-4, -3, 5, -4]
    ], float)


m_b_18 = np.array([
    [0], 
    [0],
    [0],
    [0]
    ], float)


m_a_19 = np.array([
    [0, 2, 2, 4], 
    [1, 0, -1, -3],
    [2, 3, 1, 1],
    [-2, 1, 3, -2]
    ], float)


m_b_19 = np.array([
    [0], 
    [0],
    [0],
    [0]
    ], float)


m_a_20 = np.array([
    [1, 3, 0, 1], 
    [1, 4, 2, 0],
    [0, -2, -2, -1],
    [2, -4, 1, 1], 
    [1, -2, -1, 1]
    ], float)


m_b_20 = np.array([
    [0], 
    [0],
    [0],
    [0],
    [0]
    ], float)


m_a_21 = np.array([
    [2, -1, 3, 4], 
    [1, 0, -2, 7],
    [3, -3, 1, 5],
    [2, 1, 4, 4]
    ], float)


m_b_21 = np.array([
    [9], 
    [11],
    [8],
    [10]
    ], float)


m_a_22 = np.array([
    [0, 0, 1, 1, 1], 
    [-1, -1, 2, -3, 1],
    [1, 1, -2, 0, -1],
    [2, 2, -1, 0, 1]
    ], float)


m_b_22 = np.array([
    [0], 
    [0],
    [0],
    [0]
    ], float)