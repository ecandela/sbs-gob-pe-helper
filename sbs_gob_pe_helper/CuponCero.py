import requests 
from bs4 import BeautifulSoup 
import pandas as pd 
import numpy as np
import plotly.graph_objects as go
from io import BytesIO
from seleniumbase import SB
import common as cm

def get_curva_cupon_cero_historico(FechaInicio=None,FechaFin=None,TipoCurva=False):

    with SB(uc=True, test=True, locale_code="en", headless=False) as sb:
            # Obtener el directorio de descargas
            downloads_path = sb.get_downloads_folder()
        
            file_name ="curva_historica.xlsx"
            sb.delete_downloaded_file_if_present(file_name, browser=False)
            
            URL = "https://www.sbs.gob.pe/app/pp/n_CurvaSoberana/CurvaSoberana/ConsultaHistorica"
            
            # Abrir la URL con desconexión controlada
            sb.uc_open_with_disconnect(URL, 2.2)
            
            # Simular presionar la tecla Tab y luego Espacio
            sb.uc_gui_press_key("\t")
            sb.uc_gui_press_key(" ")
            
            # Reconectar después de una pausa
            sb.reconnect(2.2)
            
            # Seleccionar opciones y llenar fechas
            sb.select_option_by_value("#cboFiltroTipoCurva", TipoCurva)
            sb.type("#txtFiltroFechaInicio", FechaInicio)
            sb.type("#txtFiltroFechaFin", FechaFin)
            
            # Hacer clic para iniciar la descarga
            sb.click("#btnBuscarInformacionHistorica")
            
            # Esperar y buscar el nuevo archivo
            sb.assert_downloaded_file(file_name, timeout=None, browser=False)
            if sb.is_downloaded_file_present(file_name, browser=False):
            
                path_file = sb.get_path_of_downloaded_file(file_name,  browser=False) 

    df = pd.read_excel(path_file,engine='openpyxl')  
    df_nuevo = df.iloc[1:].reset_index(drop=True)
    df_nuevo.columns = df.iloc[0] 
    return df_nuevo

''' 
def get_curva_cupon_cero_historico(FechaInicio=None,FechaFin=None,TipoCurva=False):

    #URL = "https://www.sbs.gob.pe/app/pp/n_CurvaSoberana/ExportarListadoHistoricoCurvaSoberana" 
    URL = "https://www.sbs.gob.pe/app/pp/n_CurvaSoberana/CurvaSoberana/ConsultaHistorica" 



    data = {
                'FechaInicio': FechaInicio,
                'FechaFin': FechaFin,                    
                'TipoCurva': TipoCurva,                    
            }
    response = requests.post(URL, json=data)

    if response.status_code == 200:

         
        excel_data = BytesIO(response.content)
        
        # Utilizar pandas para leer los datos del archivo Excel en memoria y convertirlo en un DataFrame
        df = pd.read_excel(excel_data, engine='openpyxl')

        df_nuevo = df.iloc[1:].reset_index(drop=True)
        df_nuevo.columns = df.iloc[0]

        return df_nuevo
    
'''

def pivot_curva_cupon_cero_historico(df):

    # Pivotar el DataFrame
    pivot_df = df.pivot(index=["Fecha de Proceso", "Tipo de Curva"], columns="Plazo (DIAS)", values="Tasas (%)").reset_index()

    # Renombrar las columnas
    pivot_df.columns.name = None

    non_numeric_columns = ["Fecha de Proceso", "Tipo de Curva"]

    numeric_columns = [col for col in pivot_df.columns if col not in non_numeric_columns]
    numeric_columns.sort(key=lambda x: int(x.split(' ')[0]))

    new_columns_order = non_numeric_columns + numeric_columns
    pivot_df = pivot_df[new_columns_order]

    # Convertir las columnas a numéricas
    pivot_df[numeric_columns] = pivot_df[numeric_columns].apply(pd.to_numeric, errors='coerce')


    return pivot_df





def get_curva_cupon_cero(tipoCurva=None,fechaProceso=None,tramoCorto=False):

    URL = "https://www.sbs.gob.pe/app/pu/CCID/Paginas/cc_unacurva.aspx" 
    '''   
    with requests.Session() as req:
        r = req.get(URL) 
        soup = BeautifulSoup(r.content, 'html.parser') 

        vs = soup.find("input", id="__VSTATE").get("value")
        ev_val = soup.find("input", id="__EVENTVALIDATION").get("value")

        data = {
                '__EVENTTARGET': 'cboTipoCurva',
                '__EVENTARGUMENT': '',
                '__LASTFOCUS': '',
                '__VSTATE': vs,
                '__VIEWSTATE': '',     

                '__SCROLLPOSITIONX':'0',
                '__SCROLLPOSITIONY':'100',

                '__EVENTVALIDATION':ev_val,
                'cboTipoCurva': tipoCurva
            }
        r = req.post(URL, data=data)
        soup_post_t_curv = BeautifulSoup(r.content, 'html.parser')

        vs = soup_post_t_curv.find("input", id="__VSTATE").get("value")
        ev_val = soup_post_t_curv.find("input", id="__EVENTVALIDATION").get("value")

        data = {
                '__EVENTTARGET': '',
                '__EVENTARGUMENT': '',
                '__LASTFOCUS': '',
                '__VSTATE': vs,
                '__VIEWSTATE': '',     

                '__SCROLLPOSITIONX':'0',
                '__SCROLLPOSITIONY':'64',

                '__EVENTVALIDATION':ev_val,
                'cboTipoCurva': tipoCurva,
                'cboFechas':fechaProceso,           
                'btnConsultar':"Consultar"
            }
        
        if tramoCorto:
            data["chkTramoCorto"] = "on"

        r = req.post(URL, data=data)
        '''  

    with SB(uc=True, test=True, locale_code="en", headless=False) as sb:
        URL = "https://www.sbs.gob.pe/app/pu/CCID/Paginas/cc_unacurva.aspx" 
        # Abrir la URL con desconexión controlada
        sb.uc_open_with_disconnect(URL, 2.2)
        
        # Simular presionar la tecla Tab y luego Espacio
        sb.uc_gui_press_key("\t")
        sb.uc_gui_press_key(" ")
        
        # Reconectar después de una pausa
        sb.reconnect(2.2)
        sb.select_option_by_value('select[name="cboTipoCurva"]', tipoCurva)
        sb.select_option_by_value('select[name="cboFechas"]', fechaProceso)

        # Interactuar con el checkbox según el parámetro
        checkbox_selector = '[name="chkTramoCorto"]'  # Cambia "checkboxName" al atributo `name` real del checkbox
        is_checked = sb.is_selected(checkbox_selector)
        
        if tramoCorto and not is_checked:
            sb.click(checkbox_selector)  # Marcar el checkbox si no está marcado
        elif not tramoCorto and is_checked:
            sb.click(checkbox_selector)  # Desmarcar el checkbox si está marcado
        
        sb.click('[name="btnConsultar"]') 
        # Obtener el código HTML de la página
        html_content = sb.get_page_source()

    soup_post_result = BeautifulSoup(html_content, 'html.parser')

    tablaCab = soup_post_result.find('table', {'id': 'tablaDetalle'})

    thead = tablaCab.find('thead')    
    lista_columnas = []

    for fila in thead.find_all('tr'):
        celdas = fila.find_all('th',{'class':'APLI_cabeceraTabla2'})
        datos_columna = [celda.text.strip() for celda in celdas]
        if len(datos_columna)>0:
            lista_columnas = datos_columna

    tablaCuerpo = soup_post_result.find('table', {'id': 'tablaCuerpo'})
    tbody = tablaCuerpo.find('tbody')
    datos_tabla = []
    # Iterar sobre las filas de la tabla
    for fila in tbody.find_all('tr'):
        # Obtener los datos de cada celda en la fila
        celdas = fila.find_all('td')
        datos_fila = [celda.text.strip() for celda in celdas]    
        datos_tabla.append(datos_fila)  


    df = pd.DataFrame(datos_tabla, columns=lista_columnas)

    df['Tasas (%)'] = pd.to_numeric(df['Tasas (%)'], errors='coerce')
    df['Periodo (días)'] = pd.to_numeric(df['Periodo (días)'], errors='coerce')

    return df    


def plot_curva(df):

    df_cup_por_anio = df[df['Periodo (días)'] % 360 == 0].copy()

    df_cup_por_anio["anio"] = df_cup_por_anio['Periodo (días)'] / 360 

    fig = go.Figure(data=go.Scatter(x=df_cup_por_anio.anio, y=df_cup_por_anio["Tasas (%)"], mode='lines+markers',    name='lines+markers'))

    # Obtener los límites mínimo y máximo de los datos en el eje Y
    y_min = df_cup_por_anio["Tasas (%)"].min()
    y_max = df_cup_por_anio["Tasas (%)"].max()

    # Calcular los 8 valores equidistantes entre el límite mínimo y máximo
    y_values = [y_min + (i * (y_max - y_min) / 7) for i in range(8)]

    fig.update_layout(
                    xaxis_title='Años',
                    yaxis_title='Tasas',       
                    yaxis=dict(tickmode='array',  tickvals=y_values, nticks=8, tickfont=dict(size=12), hoverformat='.2f'),         
                    xaxis=dict(type='category', tickfont=dict(size=12), tickangle=90),
                    margin=dict(l=20, r=10, t=20, b=10)
                    )

    fig.show()



def get_pronostico_lineal(conjunto_x,conjunto_y, var_indep ):
    x = var_indep
    f = np.polyfit(conjunto_x, conjunto_y, 1)
    a = f[0]
    b = f[1]
    pronostico = a * x + b

    return pronostico


def get_tasa_interes_por_dias(dias ,df_tasas):

    lb_dias = "Periodo (días)"
    ld_tasas = "Tasas (%)"

    # Valor "x" que deseas buscar
    x = dias
    y = None
    # Si "x" coincide con uno de los valores en la columna "días", entonces se muestra el registro correspondiente
    matching_record = df_tasas[df_tasas[lb_dias] == x]
    if len(matching_record)>0:

        #print(matching_record)
        y = matching_record.loc[: , ld_tasas].values[0]

    else:        
        # Encontrar el registro inferior y el registro superior más próximos a "x" en la columna "días"
        lower_record = df_tasas[df_tasas[lb_dias] <= x].tail(1)
        upper_record = df_tasas[df_tasas[lb_dias] >= x].head(1)

        result = pd.concat([lower_record, upper_record])

        conjunto_x = result[lb_dias]
        conjunto_y = result[ld_tasas]
        
        y = get_pronostico_lineal(conjunto_x,conjunto_y,x)

        #print(result)
    return y        