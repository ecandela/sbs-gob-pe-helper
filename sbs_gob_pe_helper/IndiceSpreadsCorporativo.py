

import requests
import json
import pandas as pd 
from bs4 import BeautifulSoup 
from seleniumbase import SB

from sbs_gob_pe_helper import common as cm

def get_indice_spreads_corporativo(tipoCurva="",fechaInicial="", fechaFinal=""):

    with SB(uc=True, test=True, locale_code="en", headless=False) as sb:
                          
            URL = "https://www.sbs.gob.pe/app/pp/Spreads/Spreads_Consulta.asp"
            
            # Abrir la URL con desconexión controlada
            sb.uc_open_with_disconnect(URL, 2.2)
            
            # Simular presionar la tecla Tab y luego Espacio
            sb.uc_gui_press_key("\t")
            sb.uc_gui_press_key(" ")
            
            # Reconectar después de una pausa
            sb.reconnect(2.2)
            
            # Seleccionar opciones y llenar fechas
            sb.select_option_by_value("#as_tip_curva", tipoCurva)
            sb.select_option_by_value("#as_fec_cons", fechaInicial)
            sb.select_option_by_value("#as_fec_cons2", fechaFinal)
                                 

            # Hacer clic para iniciar la descarga
            sb.click("#Consultar")
            
            html_content = sb.get_page_source()

    soup_post_result = BeautifulSoup(html_content, 'html.parser')
    tabla = soup_post_result.find("table", class_="APLI_conteTabla2")
      
    data = []

    # Obtener los nombres de las columnas desde el primer tr
    header_cells = tabla.find_all("tr")[0].find_all("td")
    column_names = [celda.get_text(strip=True) for celda in header_cells]

    # Iterar sobre las filas de la tabla a partir de la segunda fila
    for fila in tabla.find_all("tr")[1:]:
        celdas = fila.find_all("td")
        if celdas:  # Solo procesar filas con datos
            data.append([celda.get_text(strip=True) for celda in celdas])

    
    # Crear un DataFrame con los datos, usando los nombres de las columnas obtenidos
    df = pd.DataFrame(data, columns=column_names)
    df['Indice de Spread'] = pd.to_numeric(df['Indice de Spread']) 
    df['Sec.'] = pd.to_numeric(df['Sec.']) 
    
    return df

''' 
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
'''