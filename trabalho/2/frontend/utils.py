
import numpy as np
from intvalpy import lineqs

def formating_equation(A, B, C, prob='min', non_negative=True) -> str:
    ineq = []

    if not ineq:
        if prob == 'max':
            ineq = ['<='] * len(B)
        elif prob == 'min':
            ineq = ['>='] * len(B)

    output = f"Otimizacao de:  {prob} Z = {C[0]}x + {C[1]}y"

    output = output + ",  Sujeito a:"
    for i in range(len(A)):
        output = output + f" {A[i][0]}x + {A[i][1]}y {ineq[i]} {B[i]}, "
    
    if non_negative:
        output = output + " Tal que: x, y >= 0"

    return output


def generating_grafh_and_vertices(A, B):
    A = np.array(A)
    b = np.array(B)

    dots = lineqs(A, b, title='Solução', s=1.0, bounds=[[0, 0], [100, 100]], color='Green', alpha=1.0, size=(8,8), save=True)
    return dots

def calculating_objective_function(C, dots):
    output = (f"Z = {C[0]}x + {C[1]}y temos")

    z_solutions = {}
    for dot in dots:
        solution = round(C[0]*dot[0] + C[1]*dot[1], 4)
        ponto = f"{dot[0]},{dot[1]}"
        z_solutions.update({solution: ponto})
        
        output = output + (f",  Z({ponto}) = {solution}")
    
    return output, z_solutions

def returning_lowest_highest_value(z_solutions, prob='min'):
    output = ''

    if prob == 'max':
        output = output + (f"O valor maximo da zona factivel é {max(z_solutions)} encontrado no ponto Z({z_solutions[max(z_solutions)]})")
    elif prob == 'min':
        if min(z_solutions) < 0:
            result = min(z_solutions) * -1
        else:
            result = min(z_solutions)

        output = output + (f"O valor minimo da zona factivel é {result} encontrado no ponto Z({z_solutions[min(z_solutions)]})")
    
    return output