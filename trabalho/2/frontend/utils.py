
def formating_equation(A, B, C, prob='min', non_negative=True) -> str:
    ineq = []

    if not ineq:
        if prob == 'max':
            ineq = ['<='] * len(B)
        elif prob == 'min':
            ineq = ['>='] * len(B)

    output = f"Otimização de:  {prob} Z = {C[0]}x + {C[1]}y"

    output = output + "\nSujeito a:"
    for i in range(len(A)):
        output = output + f"        {A[i][0]}x + {A[i][1]}y {ineq[i]} {B[i]}"
    
    if non_negative:
        output = output + "\n Tal que: x, y >= 0"

    return output