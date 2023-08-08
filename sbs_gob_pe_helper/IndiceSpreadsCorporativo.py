

import requests
import json
import pandas as pd 


def get_indice_spreads_corporativo(tipoCurva="",fechaInicial="", fechaFinal=""):
    # URL de la API a la que haremos la llamada POST
    url = 'https://www.sbs.gob.pe/app/pp/Spreads/n_spreads_coorporativos/ObtenerIndiceSpreadsCorporativo'

    # Datos que se enviarán en el cuerpo de la solicitud POST
    data_param = {
        'fechaFinal': fechaInicial, #"04/08/2023",
        'fechaInicial':fechaFinal, #"01/08/2023",
        'tipoCurva': tipoCurva #"CCPSS"
    }

    # Realizar la llamada POST
    response = requests.post(url, json=data_param)

    # Parsear el JSON en un diccionario
    data_dict = json.loads(response.text)

    # Extraer la parte del diccionario que contiene los datos que queremos
    data_response = data_dict['data']['consulta1']

    # Crear un DataFrame a partir de los datos
    df = pd.DataFrame(data_response)

    return df
