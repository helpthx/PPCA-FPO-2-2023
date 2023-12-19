def formating_objective_function(C, prob, cof='x', eq="Z"):
    if prob == "max":
        funcao_objetiva = f"Otimização de:  {prob} {eq} = "
    else:
        funcao_objetiva = f"Otimização de:  {prob} {eq} = "
    
    for i in range(len(C)):
        if i == 0:
            funcao_objetiva = funcao_objetiva + f"{C[i]}{cof}{i} "
        else:
            funcao_objetiva = funcao_objetiva + f"+ {C[i]}{cof}{i} "
    return funcao_objetiva

def formating_inequations(A, Aineq, B, cof='x'):
    inequacoes = 'Sujeito a: \n'
    for i in range(len(A)):
        inequacoes += '         '
        for j in range(len(A[i])):
            if j == 0:
                inequacoes += f"{A[i][j]}{cof}{j} "
            else:
                inequacoes += f"+ {A[i][j]}{cof}{j} "
        inequacoes += f"{Aineq[i]} {B[i]} \n"
                
            
    return inequacoes

def formating_input_coeficients(A, Aineq, B, C, prob, cof='x', eq="Z"):
    output = ''
    objective_function = formating_objective_function(C, prob, cof, eq)
    inequeations = formating_inequations(A, Aineq, B, cof)
    output = objective_function + '\n\n' + inequeations
    return output

def transforming_canonic_form(A, Aineq, B, C, prob):
    if prob == 'max':
        for i in range(len(Aineq)):
            if Aineq[i] != '<=':
                for j in range(len(A[i])):
                    A[i][j] = A[i][j]*-1
                Aineq[i] = '<='
                B[i] = B[i]*-1
    else:
        for i in range(len(C)):
            C[i] = C[i]
                       
        for i in range(len(Aineq)):
            if Aineq[i] != '>=':
                for j in range(len(A[i])):
                    A[i][j] = A[i][j]*-1
                Aineq[i] = '>='
                B[i] = B[i]*-1
    return A, Aineq, B, C, prob

def transforming_dual_form(A, Aineq, B, C, prob):
    At = list(map(list, zip(*A)))
    Bt = C.copy()
    Ct = B.copy()
    
    if prob == "max":
        prob = "min"
        Aineq = [">="]*len(Bt)
    else: 
        prob = "max"
        Aineq = ["<="]*len(Bt)

    return At, Aineq, Bt, Ct, prob

def solve_questao_3(A, Aineq, B, C, prob):
    print("a - Mostrando problema de entrada \n")
    print(formating_input_coeficients(A, Aineq, B, C, prob, "Z"))
    print("\n\n")
    A, Aineq, B, C, prob = transforming_canonic_form(A, Aineq, B, C, prob)
    print("b - Transformando em formato canonico \n")
    print(formating_input_coeficients(A, Aineq, B, C, prob, "Z"))
    print("\n\n")
    At, Aineq, Bt, Ct, prob = transforming_dual_form(A, Aineq, B, C, prob)
    print("c - Transformando em formato dual \n")
    print(formating_input_coeficients(At, Aineq, Bt, Ct, prob, "y", "D"))