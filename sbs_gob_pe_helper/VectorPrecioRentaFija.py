import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumbase import SB
from seleniumbase import Driver
import os

from sbs_gob_pe_helper import common as cm

def get_vector_precios(fechaProceso=None,cboMoneda="",cboEmisor="",cboRating=""):

    # Validación de que fechaProceso no sea None ni un string vacío
    if not fechaProceso:
        raise ValueError("El parámetro 'fechaProceso' no puede ser None ni un string vacío.")
    
   
    with SB(uc=True, test=True, locale_code="en", headless=False) as sb:
        URL = "https://www.sbs.gob.pe/app/pu/ccid/paginas/vp_rentafija.aspx" 
        # Abrir la URL con desconexión controlada
        sb.uc_open_with_disconnect(URL, 2.2)
        
        # Simular presionar la tecla Tab y luego Espacio
        sb.uc_gui_press_key("\t")
        sb.uc_gui_press_key(" ")
        
        # Reconectar después de una pausa
        sb.reconnect(2.2)
        sb.select_option_by_value('select[name="cboFecProceso"]', fechaProceso)
        sb.select_option_by_value('select[name="cboMoneda"]', cboMoneda)
        sb.select_option_by_value('select[name="cboEmisor"]', cboEmisor)
        sb.select_option_by_value('select[name="cboRating"]', cboRating)

        sb.click('[name="btnConsultar"]') 
        # Obtener el código HTML de la página
        html_content = sb.get_page_source()

    soup_post = BeautifulSoup(html_content, 'html.parser')
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

''' 
def get_vector_precios(fechaProceso=None,cboMoneda="",cboEmisor="",cboRating=""):

    URL = "https://www.sbs.gob.pe/app/pu/ccid/paginas/vp_rentafija.aspx" 


    #r = req.get(URL) 
    #soup = BeautifulSoup(r.content, 'html.parser') 

    html = get_html(url=URL)
    soup = BeautifulSoup(html, 'html.parser')
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
    
    print(data)
    
    with requests.Session() as req:
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
'''


def get_html_webdriver(url):
    # Configurar un perfil persistente de Chrome
    chrome_options = Options()
    # Iniciar el navegador con el perfil persistente
    driver = webdriver.Chrome(options=chrome_options)

    # Navegar a las páginas
    try:
        driver.get(url)    
        html_content = driver.page_source  # Obtener el contenido HTML de la página     
    finally:
        driver.quit()

        return html_content
    
def get_html_seleniumbase(url):

    with SB(uc=True, test=True, locale_code="en", headless=False) as sb:

        # Abrir la URL con desconexión controlada
        sb.uc_open_with_disconnect(url, 2.2)
        
        # Simular presionar la tecla Tab y luego Espacio
        sb.uc_gui_press_key("\t")
        sb.uc_gui_press_key(" ")
        
        # Reconectar después de una pausa
        sb.reconnect(2.2)
        
        # Obtener el código HTML de la página
        html_content = sb.get_page_source()
        
        return html_content



def get_html(url="",tipo="wd"):

    #return get_html_webdriver(url)
    return get_html_seleniumbase(url)

    
def get_df_emisores():

    URL = "https://www.sbs.gob.pe/app/pu/ccid/paginas/vp_rentafija.aspx" 
    html = get_html(url=URL)
    #with requests.Session() as req:
    #    r = req.get(URL) 
    #    soup = BeautifulSoup(r.content, 'html.parser') 
    soup = BeautifulSoup(html, 'html.parser')
    # Encuentra el elemento <select> por su etiqueta y atributos
    select_element = soup.find('select', {'name': 'cboEmisor'})

    # Inicializamos listas para almacenar los valores
    values = []
    text_values = []

    # Recorremos las opciones dentro del elemento <select>
    for option in select_element.find_all('option'):
        value = option.get('value')
        text = option.get_text()
        if value is not None and value!="" and text.strip() != "":
            values.append(value)
            text_values.append(text)

    # Creamos un diccionario con los datos
    data = {'cboEmisor': values, 'Emisor': text_values}

    # Creamos un DataFrame a partir del diccionario
    df = pd.DataFrame(data)


    return df


def get_precios_by_isin(isin):

    #PEP21400M064
    URL = f"https://www.sbs.gob.pe/app/pu/CCID/Paginas/vp_detalle.aspx?cod={isin}" 

    #with requests.Session() as req:
    #r = req.get(URL) 
    #soup = BeautifulSoup(r.content, 'html.parser') 

    html = get_html(url=URL)
    soup = BeautifulSoup(html, 'html.parser') 
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