from fastapi import FastAPI, Path
from fastapi.responses import FileResponse
import utils

from pydantic import BaseModel

import json, typing
from starlette.responses import Response

class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: typing.Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")

class IntList(BaseModel):
    funcao_objetiva: list[int] = []
    lista_equacoes: list[list[int]] = []
    lista_restricoes: list[int] = []

app = FastAPI()

@app.post("/2", response_class=PrettyJSONResponse)
async def b(data: IntList):
    """Url que recebe as equaçoes e inequações na forma canonica minizada em formato matricial. ie \n
        \n
        funcao_objetiva: Função objetiva do problema (i.e Z = 2x + 3y: [-2, -3]) \n
        lista_equacoes: Restrições em formato canonico (i.e x + y >= 0, 2x + 1y >= 5 e 7x + 3y =< 10: [[1, 1], [2, 1], [-7, -3]] ) \n
        lista_restricoes: Restrições em formato canonico (i.e x + y >= 0, 2x + 1y >= 5 e 7x + 3y =< 10: [0, 2, -10)""" 
    
    # Access the list of integers using `data.numbers`
    # Perform your logic with the list
    output = utils.formating_equation(data.lista_equacoes, data.lista_restricoes, data.funcao_objetiva, )
    return {"1": f"funcao_objetiva: {output}" }


from fastapi.responses import FileResponse

@app.get("/teste")
async def main():
    return [FileResponse("/home/jvrbaptista/Documents/mestrado/FPO/trabalho/2/images/teste.jpeg"),
            FileResponse("/home/jvrbaptista/Documents/mestrado/FPO/trabalho/2/images/car.jpeg")]


import os
import zipfile
import StringIO


def zipfiles(filenames):
    zip_subdir = "archive"
    zip_filename = "%s.zip" % zip_subdir

    # Open StringIO to grab in-memory ZIP contents
    s = StringIO.StringIO()
    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = Response(s.getvalue(), mimetype = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename

    return resp


@app.get("/image_from_id/")
async def image_from_id():

    # Get image from the database
    img = "/home/jvrbaptista/Documents/mestrado/FPO/trabalho/2/images/*"
    return zipfiles(img)
            