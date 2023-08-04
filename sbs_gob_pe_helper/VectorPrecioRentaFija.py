import requests 
from bs4 import BeautifulSoup 
import pandas as pd 

def get_vector_precios(fechaProceso=None,cboMoneda="",cboEmisor="",cboRating=""):

    URL = "https://www.sbs.gob.pe/app/pu/ccid/paginas/vp_rentafija.aspx" 

    with requests.Session() as req:
        r = req.get(URL) 
        soup = BeautifulSoup(r.content, 'html.parser') 

        vs = soup.find("input", id="__VIEWSTATE").get("value")
        vsg = soup.find("input", id="__VIEWSTATEGENERATOR").get("value")
        ev_val = soup.find("input", id="__EVENTVALIDATION").get("value")

        data = {
                '__EVENTTARGET': '',
                '__EVENTARGUMENT': '',
                '__LASTFOCUS': '',
                '__VIEWSTATE': vs,
                '__VIEWSTATEGENERATOR': vsg,
                '__SCROLLPOSITIONX':'0',
                '__SCROLLPOSITIONY':'0',
                '__EVENTVALIDATION':ev_val,
                'cboFecProceso': fechaProceso,
                'cboMoneda':cboMoneda,
                'cboEmisor':cboEmisor,
                'cboRating':cboRating,
                'btnConsultar':"Consultar"
            }
        r = req.post(URL, data=data)
        soup_post = BeautifulSoup(r.content, 'html.parser')
        tabla = soup_post.find('table', {'id': 'tablaReporte'})

        thead = tabla.find('thead')
        lista_columnas = []
        for fila in thead.find_all('tr'):
            celdas = fila.find_all('th',{'class':'APLI_cabeceraTabla2'})
            datos_columna = [celda.text.strip() for celda in celdas]
            if len(datos_columna)>0:
                lista_columnas = datos_columna


        tbody = tabla.find('tbody')
        datos_tabla = []
        # Iterar sobre las filas de la tabla
        for fila in tbody.find_all('tr'):
            # Obtener los datos de cada celda en la fila
            celdas = fila.find_all('td')
            datos_fila = [celda.text.strip() for celda in celdas]    
            datos_tabla.append(datos_fila)  


        df = pd.DataFrame(datos_tabla, columns=lista_columnas)

        return df
    

def get_precios_by_isin():

    URL = "https://www.sbs.gob.pe/app/pu/CCID/Paginas/vp_detalle.aspx?cod=PEP21400M064" 

    with requests.Session() as req:
        r = req.get(URL) 
        soup = BeautifulSoup(r.content, 'html.parser') 

        tablaCab = soup.find('table', {'id': 'tablaDetalle'})

        thead = tablaCab.find('thead')
        lista_columnas = []
        for fila in thead.find_all('tr'):
            celdas = fila.find_all('td',{'class':'APLI_cabeceraTabla2'})
            datos_columna = [celda.text.strip() for celda in celdas]
            if len(datos_columna)>0:
                lista_columnas = datos_columna


        tablaCuerpo = soup.find('table', {'id': 'tablaCuerpo'})
        tbody = tablaCuerpo.find('tbody')
        datos_tabla = []
        # Iterar sobre las filas de la tabla
        for fila in tbody.find_all('tr'):
            # Obtener los datos de cada celda en la fila
            celdas = fila.find_all('td')
            datos_fila = [celda.text.strip() for celda in celdas]    
            datos_tabla.append(datos_fila)  


        df = pd.DataFrame(datos_tabla, columns=lista_columnas)

        return df