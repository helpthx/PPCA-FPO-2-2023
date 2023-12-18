from fastapi import FastAPI
from fastapi.responses import FileResponse
import utils

from pydantic import BaseModel

class IntList(BaseModel):
    funcao_objetiva: list[int] = []
    lista_equacoes: list[list[int]] = []
    lista_restricoes: list[int] = []

app = FastAPI()

@app.post("/2")
async def b(data: IntList):
    """Url que recebe as equaçoes e inequações na forma canonica minizada em formato matricial. ie \n
        \n
        funcao_objetiva: Função objetiva do problema (i.e Z = 2x + 3y: [-2, -3]) \n
        lista_equacoes: Restrições em formato canonico (i.e x + y >= 0, 2x + 1y >= 5 e 7x + 3y =< 10: [[1, 1], [2, 1], [-7, -3]] ) \n
        lista_restricoes: Restrições em formato canonico (i.e x + y >= 0, 2x + 1y >= 5 e 7x + 3y =< 10: [0, 2, -10)""" 
    
    # Access the list of integers using `data.numbers`
    # Perform your logic with the list
    output_1 = utils.formating_equation(data.lista_equacoes, data.lista_restricoes, data.funcao_objetiva)
    dots = utils.generating_grafh_and_vertices(data.lista_equacoes, data.lista_restricoes)
    output_5, all_solutions = utils.calculating_objective_function(data.funcao_objetiva, dots)
    output_6 = utils.returning_lowest_highest_value(all_solutions)
    
    results = {"1": f"Funcao Objetiva: {str(output_1)}",
               "2": f"Pontos factiveis: {str(dots.tolist())}",
               "5": f"Possiveis valores para funcao objetiva: {str(output_5)}",
               "6": f"Valor otimo para funcao objetiva: {str(output_6)}"}
    
    return  FileResponse('/home/jvrbaptista/Documents/mestrado/FPO/PPCA-FPO-2-2023/trabalho/2/frontend/Solução.png', headers=results)


# from fastapi.responses import FileResponse

# @app.get("/teste")
# async def main():
#     return [FileResponse("/home/jvrbaptista/Documents/mestrado/FPO/trabalho/2/images/teste.jpeg"),
#             FileResponse("/home/jvrbaptista/Documents/mestrado/FPO/trabalho/2/images/car.jpeg")]

@app.post("/ImgAndJSON")
# Postmsg is a Pydantic model having 1 str field
def ImgAndJSON():

    results={"message":"This is just test message"}

    return FileResponse('/home/jvrbaptista/Documents/mestrado/FPO/PPCA-FPO-2-2023/trabalho/2/perfil.jpeg', headers=results)
