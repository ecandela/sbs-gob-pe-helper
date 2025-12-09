
# sbs-gob-pe-helper: Cliente de datos del Mercado de Valores y Seguros (SBS)
==============================

> ⚠️ **Aviso:** Esta es una librería de código abierto **NO OFICIAL**. Su desarrollo es independiente y no tiene vinculación con la Superintendencia de Banca, Seguros y AFP. Te recomendamos revisar la [Nota legal y Exención de Responsabilidad](docs/NotaLegal.md) antes de su uso.

<a target="new" href="https://pypi.org/project/sbs-gob-pe-helper/"><img border=0 src="https://img.shields.io/badge/python-%203.8.2+-blue.svg?style=flat" alt="Python version"></a>
<a target="new" href="https://pypi.org/project/sbs-gob-pe-helper/"><img border=0 src="https://img.shields.io/pypi/v/sbs-gob-pe-helper.svg?maxAge=60%" alt="PyPi version"></a>
<a target="new" href="https://pypi.org/project/sbs-gob-pe-helper/"><img border=0 src="https://img.shields.io/pypi/status/sbs-gob-pe-helper.svg?maxAge=60" alt="PyPi status"></a>

**sbs-gob-pe-helper** ofrece una interfaz *Pythonica* para acceder a datos históricos y vigentes (Curvas Cupón Cero, Vectores de Precios, Spreads) originados en la información pública de la [Superintendencia de Banca y Seguros del Perú](https://www.sbs.gob.pe/).

Esta librería facilita el acceso a la información mediante el consumo de datos estructurados, garantizando mayor estabilidad y rapidez al evitar la dependencia de *web scraping* en tiempo real sobre el portal gubernamental.

*El nombre del paquete es utilizado con fines descriptivos y de referencia a la fuente de datos (Uso Justo Nominativo).*

**Recursos Adicionales**:
Para una introducción detallada y casos de uso financiero, te recomendamos leer el artículo:
<a target="new" href="https://medium.com/@erik.candela.rojas/acceso-eficiente-a-datos-para-la-valorizaci%C3%B3n-de-instrumentos-de-deuda-en-el-per%C3%BA-con-python-45da0e5ac45e">Acceso Eficiente a Datos para la Valorización de Instrumentos de Deuda en el Perú con Python</a>.

-----------------
## Características 
A continuación se encuentran las características que aborda este paquete. 
- Curva cupón cero:
  - Extracción plazos y tasas de interés por tipo de curva de la SBS.
  - Gráfica de curva.
  - Interpolación lineal de la curva.
- Vector de precio de renta fija:
  - Extracción de datos de vector de precio por fecha de procesamiento desde la SBS.
  - Extracción de emisores disponibles del vector de precio.
  - Extracción de datos históricos de precios por ISIN.
- Índice spread corporativo.
  - Extracción de datos desde la SBS.

---  


## Instalación

Instala `sbs-gob-pe-helper` usando `pip`:

``` {.sourceCode .bash}
$ pip install sbs-gob-pe-helper
```

---


# Quick Start

## 📦 Módulo CuponCero

Puedes ver un ejemplo práctico en el siguiente notebook:
[📄 Ver Demo en GitHub](https://github.com/ecandela/sbs-gob-pe-helper/blob/main/test/Cupon_cero.ipynb)

### `get_curva_cupon_cero`

Esta función permite acceder a los datos de cupón cero de la SBS filtrando por tipo de curva y fecha de procesamiento.

**Parámetros**

| Parámetro | Tipo | Descripción | Formato / Ejemplo |
| :--- | :---: | :--- | :--- |
| `fechaProceso` | `str` | Fecha de procesamiento de los datos. | `"dd/mm/yyyy"` |
| `tipoCurva` | `str` | Código del tipo de curva deseada. | Ver tabla inferior |

**Tipos de Curva (`tipoCurva`)**

| Código | Descripción |
| :--- | :--- |
| **CBCRS** | Curva Cupón Cero CD BCRP |
| **CCSDF** | Curva Cupón Cero Dólares CP |
| **CSBCRD** | Curva Cupón Cero Dólares Sintética |
| **CCINFS** | Curva Cupón Cero Inflación Soles BCRP |
| **CCCLD** | Curva Cupón Cero Libor Dólares |
| **CCPEDS** | Curva Cupón Cero Perú Exterior Dólares - Soberana |
| **CCPSS** | Curva Cupón Cero Perú Soles Soberana |
| **CCPVS** | Curva Cupón Cero Perú Vac Soberana |

### 💻 Ejemplo de uso

```python
import sbs_gob_pe_helper.CuponCero as cc

# Configuración de la carpeta de caché (Usa raw strings 'r' para rutas en Windows)
cc.config.CACHE_DIR = r"E:\cache_temp" 

# Parámetros de consulta
tp_curva = 'CCPSS'
fec_proceso = '31/07/2023'

# Obtiene los datos de la curva de cupón cero para la fecha indicada
df_cup = cc.get_curva_cupon_cero(
    tipoCurva=tp_curva, 
    fechaProceso=fec_proceso
)

# Visualizar los primeros registros
df_cup.head()
```

![cupon primeros 5 registros](references/imagenes/cupon_head.png)

### plot_curva


Si deseas visualizar la gráfica de la curva de cupón cero, sigue estos pasos:

```python
cc.plot_curva(df_cup)
```

![Abrir Terminal](references/imagenes/curva_c0.png)

### `get_curva_cupon_cero_historico`

La función `get_curva_cupon_cero_historico` permite extraer los datos de cupón cero de la SBS para un rango de fechas específico y un tipo de curva determinado.

**Parámetros**

| Parámetro | Tipo | Descripción | Formato / Ejemplo |
| :--- | :---: | :--- | :--- |
| `fechaInicio` | `str` | Fecha de inicio del rango de consulta. | `"YYYY-MM-DD"` |
| `fechaFin` | `str` | Fecha de fin del rango de consulta. | `"YYYY-MM-DD"` |
| `tipoCurva` | `str` | Código del tipo de curva deseada. | Ver tabla inferior |

**Tipos de Curva (`tipoCurva`)**

| Código | Descripción |
| :--- | :--- |
| **CBCRS** | Curva Cupón Cero CD BCRP |
| **CCSDF** | Curva Cupón Cero Dólares CP |
| **CSBCRD** | Curva Cupón Cero Dólares Sintética |
| **CCINFS** | Curva Cupón Cero Inflación Soles BCRP |
| **CCCLD** | Curva Cupón Cero Libor Dólares |
| **CCPEDS** | Curva Cupón Cero Perú Exterior Dólares - Soberana |
| **CCPSS** | Curva Cupón Cero Perú Soles Soberana |
| **CCPVS** | Curva Cupón Cero Perú Vac Soberana |

### 💻 Ejemplo de uso

```python
import sbs_gob_pe_helper.CuponCero as cc

# Parámetros para la consulta histórica
fecha_inicio = "2023-08-01"
fecha_fin = "2023-08-26"
tp_curva = 'CCPSS'

# Obtiene los datos históricos de la curva de cupón cero
df_cup_hist = cc.get_curva_cupon_cero_historico(
    fechaInicio=fecha_inicio,
    fechaFin=fecha_fin,
    tipoCurva=tp_curva
)

# Visualizar los primeros registros
print(df_cup_hist.head())
```



![cupon primeros 5 registros](references/imagenes/curva_historico.png)



### pivot_curva_cupon_cero_historico
Adicionalmente, se puede emplear la funcion `pivot_curva_cupon_cero_historico` el cual recibe como parámetro el resultado de la función `get_curva_cupon_cero_historico` para generar un pivot:

```python
import sbs_gob_pe_helper.CuponCero as cc


df_cup_hist_pivot = cc.pivot_curva_cupon_cero_historico(df_cup_hist)
df_cup_hist_pivot.head()

```
![cupon primeros 5 registros](references/imagenes/curva_pivot.png)


### `get_tasa_interes_por_dias`

La función `get_tasa_interes_por_dias` permite calcular, mediante **interpolación lineal**, las tasas de interés para plazos (días) que no se encuentran disponibles explícitamente en la curva de cupón cero de la SBS.

Es ideal para obtener tasas ajustadas a plazos específicos (ej. 45 días) cuando la curva solo ofrece puntos estándar (ej. 30 y 60 días).

### 💻 Ejemplo de uso

```python
import pandas as pd
import sbs_gob_pe_helper.CuponCero as cc

# 1. Definimos los plazos (días) para los cuales queremos calcular la tasa.
# En este ejemplo, buscamos tasas para 0, 30, 60, 90 y 120 días.
data = {
    "dias": [0, 30, 60, 90, 120],    
}

df_test = pd.DataFrame(data)

# 2. Aplicamos la interpolación.
# Nota: 'df_cup' es el DataFrame obtenido previamente con get_curva_cupon_cero.
# Se pasa como argumento adicional para realizar el cálculo.
df_test['tasas'] = df_test['dias'].apply(
    cc.get_tasa_interes_por_dias, 
    args=(df_cup,)
)

# 3. Visualizar los resultados con las tasas interpoladas
print(df_test.head())
```


![Resultado de interpolación](references/imagenes/interpol.png)

## El modulo VectorPrecioRentaFija 
https://github.com/ecandela/sbs-gob-pe-helper/blob/main/test/Vector%20de%20Precios%20de%20Renta%20fija.ipynb

### get_vector_precios
La función  `get_vector_precios` permite acceder al vector de precios de la SBS para una determinada fecha de proceso.


| Parametro | Descripción |
| ------ | ------ |
|fechaProceso| Fecha de procesamiento|
|cboEmisor| Emisor|
|cboMoneda| Tipo de Moneda|
|cboRating| Rating Emisión|


| cboEmisor | Descripciòn |
| ------ | ------ |
|1000| GOB.CENTRAL|
|2011| ALICORP S.A.|
|0087| BANCO FALABELLA|
|0088| BCO RIPLEY|
|0001| BCRP|
|0011| CONTINENTAL|
|0042| CREDISCOTIA|
|0003| INTERBANK|

*Para conocer los emisores disponibles revisar la función `get_df_emisores`.



| cboMoneda | Descripciòn |
| ------ | ------ |
| 1 |   Soles|
| 2 | Soles VAC|
| 3 | Dolares|



| cboRating | 
| ------ | 
|A|
|A+|
|A-|
|AA|
|AA+|
|AA-|
|AAA|
|B-|
|BB|
|CP-1|
|CP-1+|
|CP-1-|
|CP-2|
|CP-2+|

### Ejemplo
```python

import sbs_gob_pe_helper.VectorPrecioRentaFija as vp 

fechaProceso = '05/12/2025'

#Obtiene el vector de precios de instrumentos de renta fija disponibles en la SBS para una fecha de proceso específica:
df_vector = vp.get_vector_precios(fechaProceso=fechaProceso)

df_vector.columns.tolist()
```

```json

['Nemónico',
 'ISIN/Identif.',
 'Emisor',
 'Moneda',
 'P. Limpio (%)',
 'TIR %',
 'Origen(*)',
 'Spreads',
 'P. Limpio (monto)',
 'P. Sucio (monto)',
 'I.C. (monto)',
 'F. Emisión',
 'F. Vencimiento',
 'Cupón (%)',
 'Margen Libor (%)',
 'TIR % S/Opc',
 'Rating Emisión',
 'Ult. Cupón',
 'Prox. Cupón',
 'Duración',
 'Var  PLimpio',
 'Var PSucio',
 'Var Tir']
```

```python

#Exhibiendo los primeros 5 registros del vector de precios:
df_vector.head()
```

![Vector de precio](references/imagenes/vector.PNG)



### get_df_emisores
La función  `get_df_emisores` permite obtener todos los emisores disponibles del vector de precios de la SBS.

### Ejemplo
```python

import sbs_gob_pe_helper.VectorPrecioRentaFija as vp 

#Obtiene el historico de precios del asset con isin PEP21400M064
df_emisores = vp.get_df_emisores()

df_emisores.head()
```

![df_emisores](references/imagenes/df_emisores.png)



### get_precios_by_isin
La función  `get_precios_by_isin` permite acceder a los datos históricos de precios para un determinado código ISIN.


| Parametro | Descripción |
| ------ | ------ |
|isin| código isin del asset|


### Ejemplo
```python

import sbs_gob_pe_helper.VectorPrecioRentaFija as vp 


#Obtiene el historico de precios del asset con isin PEP21400M064
df_precios = vp.get_precios_by_isin("PEP21400M064")

df_precios.head()
```

![precios_asset](references/imagenes/precios_asset.png)


---
## 📦 Módulo IndiceSpreadsCorporativo

Puedes ver un ejemplo práctico en el siguiente notebook:
[📄 Ver Demo en GitHub](https://github.com/ecandela/sbs-gob-pe-helper/blob/main/test/Indices%20de%20Spreads%20Corporativo.ipynb)

### `get_indice_spreads_corporativo`

La función `get_indice_spreads_corporativo` permite acceder a los índices de spread corporativo de la SBS.

**Parámetros**

| Parámetro | Tipo | Descripción | Formato / Ejemplo |
| :--- | :---: | :--- | :--- |
| `fechaInicio` | `str` | Fecha de inicio del rango de consulta. | `"dd/mm/yyyy"` |
| `fechaFin` | `str` | Fecha final del rango de consulta. | `"dd/mm/yyyy"` |
| `tipoCurva` | `str` | Código del tipo de curva deseada. | Ver tabla inferior |

**Tipos de Curva (`tipoCurva`)**

| Código | Descripción |
| :--- | :--- |
| **CBCRS** | Curva Cupón Cero CD BCRP |
| **CCSDF** | Curva Cupón Cero Dólares CP |
| **CSBCRD** | Curva Cupón Cero Dólares Sintética |
| **CCINFS** | Curva Cupón Cero Inflación Soles BCRP |
| **CCCLD** | Curva Cupón Cero Libor Dólares |
| **CCPEDS** | Curva Cupón Cero Perú Exterior Dólares - Soberana |
| **CCPSS** | Curva Cupón Cero Perú Soles Soberana |
| **CCPVS** | Curva Cupón Cero Perú Vac Soberana |

### 💻 Ejemplo de uso

```python
import sbs_gob_pe_helper.IndiceSpreadsCorporativo as isc 

# Parámetros de consulta
tp_curva = 'CCPSS'
fecha_inicio = '04/08/2023'
fecha_fin = '04/08/2023'

# Obtiene los índices de spread corporativo de la SBS para el rango específico
df_isc = isc.get_indice_spreads_corporativo(
    tipoCurva=tp_curva,
    fechaInicio=fecha_inicio, 
    fechaFin=fecha_fin
)

# Visualizar los primeros registros
df_isc.head()
```

![IndiceSpreadsCorporativo](references/imagenes/indicecorp.png)


---

## 💰 Valorización de Bonos

Puedes ver un ejemplo práctico en el siguiente notebook:
[📄 Ver Demo en GitHub](https://github.com/ecandela/sbs-gob-pe-helper/blob/main/test/Valorizacion%20de%20Bonos.ipynb)

## Feedback

La mejor manera de enviar comentarios es crear un problema en https://github.com/ecandela/sbs-gob-pe-helper/issues.
Si estás proponiendo una característica:

- Explica detalladamente cómo funcionaría.
- Mantén el alcance lo más limitado posible para facilitar la implementación.
- Recuerda que este es un proyecto impulsado por voluntarios y que las contribuciones son bienvenidas :)
