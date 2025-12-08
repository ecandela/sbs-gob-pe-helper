import pandas as pd 

def get_indice_spreads_corporativo(tipoCurva="",fechaInicio="", fechaFin=""):
    #https://www.sbs.gob.pe/app/pp/Spreads/Spreads_Consulta.asp

    # 1. LISTA BLANCA DE CÓDIGOS VÁLIDOS
    codigos_permitidos = [
        "CCCLD", "CSBCRD", "CCPVS", "CCPSS"
    ]
    
    # 2. VALIDACIÓN Y LIMPIEZA DE PARAMETRO
    if not isinstance(tipoCurva, str):
        # CAMBIO: Ahora lanza TypeError
        raise TypeError(f"❌ Error: El TipoCurva debe ser texto. Recibido: {tipoCurva}")
        
    codigo_clean = tipoCurva.upper().strip()
    
    if codigo_clean not in codigos_permitidos:
        # CAMBIO: Ahora lanza ValueError
        raise ValueError(f"❌ Error: El tipo '{tipoCurva}' no existe.\n   Opciones válidas: {codigos_permitidos}")

    fechaProceso = "05/12/2025"
    # Limpieza de la fecha reporte ISC_CCCLD
    fecha_clean = fechaProceso.strip()
    fecha_clean = fecha_clean.replace("/", ".") 

    # 2. CONSTRUCCIÓN DE LA URL
    base_url = "https://raw.githubusercontent.com/ecandela/sbs-gob-pe-helper-data/main/indice_spreads_corporativos"
    nombre_archivo = f"reporte_ISC_{tipoCurva}_{fecha_clean}.xls"
    url = f"{base_url}/{nombre_archivo}"

    try:   
        tablas = pd.read_html(url, flavor='bs4')
        df_raw = tablas[0]
        nuevos_encabezados = df_raw.iloc[1].values
        df_raw.columns = nuevos_encabezados
        df = df_raw.iloc[2:].copy()
        df.reset_index(drop=True, inplace=True)
        df.columns.name = None 
        
        print(f"2. Filas totales descargadas: {len(df)}")
        
        # --- REVISIÓN DE LA COLUMNA FECHA ---
        if 'Fecha de Proceso' not in df.columns:
             # CAMBIO: Ahora lanza KeyError
             raise KeyError(f"❌ Error: No existe la columna 'Fecha de Proceso'. Columnas: {df.columns.tolist()}")

        print(f"3. Muestra cruda de fecha (fila 0): '{df['Fecha de Proceso'].iloc[0]}'")

        # Conversión
        df['Fecha de Proceso'] = pd.to_datetime(df['Fecha de Proceso'], dayfirst=True, errors='coerce')
        
        nulos = df['Fecha de Proceso'].isna().sum()
        print(f"4. Fechas inválidas (NaT) detectadas: {nulos}")
        
        # Eliminamos nulos
        df = df.dropna(subset=['Fecha de Proceso'])
        
        if df.empty:
            # CAMBIO: Ahora lanza ValueError
            raise ValueError("⚠️ ALERTA: El DataFrame se quedó vacío después de limpiar fechas incorrectas.")

        # --- REVISIÓN DEL RANGO REAL ---
        min_fecha = df['Fecha de Proceso'].min()
        max_fecha = df['Fecha de Proceso'].max()
        print(f"5. Rango de fechas encontrado en el archivo: Del {min_fecha.date()} al {max_fecha.date()}")
        
        # --- FILTRADO ---
        if fechaInicio:
            fi = pd.to_datetime(fechaInicio, dayfirst=True)
            print(f"   -> Filtrando desde: {fi.date()}")
            df = df[df['Fecha de Proceso'] >= fi]

        if fechaFin:
            ff = pd.to_datetime(fechaFin, dayfirst=True)
            print(f"   -> Filtrando hasta: {ff.date()}")
            df = df[df['Fecha de Proceso'] <= ff]
            
        print(f"6. Filas finales después del filtro: {len(df)}")
        
        # --- FINALIZAR ---
        df = df.sort_values('Fecha de Proceso').reset_index(drop=True)
        df['Fecha Visual'] = df['Fecha de Proceso'].dt.strftime('%d/%m/%Y')
        
        df['Indice de Spread'] = pd.to_numeric(df['Indice de Spread'], errors='coerce')

        cols = ['Fecha Visual', 'Fecha de Proceso'] + [c for c in df.columns if c not in ['Fecha Visual', 'Fecha de Proceso']]
  
        df = df.sort_values(by=['Fecha de Proceso'], ascending=[True])
        return df[cols]

    except Exception as e:
        # CAMBIO: Lanza el error hacia arriba encapsulándolo, en lugar de devolver un string.
        # 'from e' mantiene el rastro original del error para que sepas qué pasó exactamente.
        raise RuntimeError(f"Error en el proceso: {str(e)}") from e

''' 
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