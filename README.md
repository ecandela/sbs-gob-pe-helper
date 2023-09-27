sbs-gob-pe-helper : Web Scraping de datos de la Superintendencia de Banca y Seguros (SBS) del Perú .
==============================

Nota : Te recomendamos revisar la [Nota legal](docs/NotaLegal.md) antes de emplear la libreria.

<a target="new" href="https://pypi.org/project/sbs-gob-pe-helper/"><img border=0 src="https://img.shields.io/badge/python-%203.8.2+-blue.svg?style=flat" alt="Python version"></a>
<a target="new" href="https://pypi.org/project/sbs-gob-pe-helper/"><img border=0 src="https://img.shields.io/pypi/v/yfinance.svg?maxAge=60%" alt="PyPi version"></a>
<a target="new" href="https://pypi.org/project/sbs-gob-pe-helper/"><img border=0 src="https://img.shields.io/pypi/status/yfinance.svg?maxAge=60" alt="PyPi status"></a>




**sbs-gob-pe-helper** ofrece una forma Pythonica de descargar datos de mercado de la [Superintendencia de Banca y Seguros del Perú](https://www.sbs.gob.pe/), mediante web scraping (sbs web scraping).


**Nota**: Es recomendable ejecutar esta librería en un entorno local. Se ha observado que en plataformas como Google Colab puede generar conflictos.

**Informativo**: Te invito a visitar la publicación en el portal Medium titulada:
<a target="new" href="https://medium.com/@erik.candela.rojas/acceso-eficiente-a-datos-para-la-valorizaci%C3%B3n-de-instrumentos-de-deuda-en-el-per%C3%BA-con-python-45da0e5ac45e">Acceso Eficiente a Datos para la Valorización de Instrumentos de Deuda en el Perú con Python</a>, donde se realiza una introducción detallada de la librería.


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

## El modulo CuponCero 


### get_curva_cupon_cero
La función `get_curva_cupon_cero` permite acceder a los datos de cupón cero de la SBS por tipo de curva y fecha de procesamiento:


| Parametro | Descripción |
| ------ | ------ |
|fechaProceso| Fecha de procesamiento|
|tipoCurva| Tipo de curva|

| tipoCurva | Descripciòn |
| ------ | ------ |
| CBCRS |    Curva Cupon Cero CD BCRP|
| CCSDF |   Curva Cupon Cero Dólares CP|
| CSBCRD | Curva Cupon Cero Dólares Sintetica|
| CCINFS | Curva Cupon Cero Inflacion Soles BCRP|
| CCCLD | Curva Cupon Cero Libor Dolares|
| CCPEDS | Curva Cupon Cero Peru Exterior Dolares - Soberana|
| CCPSS | Curva Cupon Cero Peru Soles Soberana|
| CCPVS | Curva Cupon Cero Peru Vac Soberana|


### Ejemplo

```python
import sbs_gob_pe_helper.CuponCero as cc

tp_curva = 'CCPSS'
fec_proceso = '31/07/2023'

#obtiene todos los datos de la curva de cupon cero de un determinado fecha de proceso
df_cup= cc.get_curva_cupon_cero(tipoCurva=tp_curva, fechaProceso=fec_proceso)
df_cup.head()
```

![cupon primeros 5 registros](references/imagenes/cupon_head.png)

### plot_curva


Si deseas visualizar la gráfica de la curva de cupón cero, sigue estos pasos:

```python
cc.plot_curva(df_cup)
```

![Abrir Terminal](references/imagenes/curva_c0.png)




### get_curva_cupon_cero_historico
La función `get_curva_cupon_cero_historico` permite acceder a los datos de cupón cero de la SBS a partir de un rango de fechas de procesamiento y tipo de curva:


| Parametro | Descripción |
| ------ | ------ |
|FechaInicio| Fecha de procesamiento|
|FechaFin| Tipo de curva|
|TipoCurva| Tipo de curva|

| tipoCurva | Descripciòn |
| ------ | ------ |
| CBCRS |    Curva Cupon Cero CD BCRP|
| CCSDF |   Curva Cupon Cero Dólares CP|
| CSBCRD | Curva Cupon Cero Dólares Sintetica|
| CCINFS | Curva Cupon Cero Inflacion Soles BCRP|
| CCCLD | Curva Cupon Cero Libor Dolares|
| CCPEDS | Curva Cupon Cero Peru Exterior Dolares - Soberana|
| CCPSS | Curva Cupon Cero Peru Soles Soberana|
| CCPVS | Curva Cupon Cero Peru Vac Soberana|


### Ejemplo

```python
import sbs_gob_pe_helper.CuponCero as cc


inicio="2023-08-01"
fin="2023-08-26"
tipoCurva='CCPSS'

#obtiene todos los datos de la curva de cupon cero de un determinado fecha de proceso
df_cup_hist = cc.get_curva_cupon_cero_historico(FechaInicio=inicio,FechaFin=fin,TipoCurva=tipoCurva)
df_cup_hist.head()
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


### get_tasa_interes_por_dias
La función `get_tasa_interes_por_dias` permite acceder interpolación lineal de las tasas de interés de plazos no disponible en las curvas de cupón cero de la SBS :


```python

#Si buscas obtener tasas para plazos no presentes en los datos de cupón cero, se llevará a cabo una interpolación utilizando los valores de plazos ya existentes.

# En el siguiente ejemplo, se calcularán las tasas correspondientes para los períodos de 30, 60 y 120.
data = {
    "dias": [0, 30, 60 , 90 , 120],    
}

df_test = pd.DataFrame(data)


df_test['tasas'] = df_test['dias'].apply(cc.get_tasa_interes_por_dias, args=(df_cup,))

df_test.head()

```

![Resultado de interpolación](references/imagenes/interpol.png)

## El modulo VectorPrecioRentaFija 


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

fechaProceso = '21/07/2023'

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

fechaProceso = '21/07/2023'

#Obtiene el historico de precios del asset con isin PEP21400M064
df_precios = vp.get_precios_by_isin("PEP21400M064")

df_precios.head()
```

![precios_asset](references/imagenes/precios_asset.png)


---


## El modulo IndiceSpreadsCorporativo 



### get_indice_spreads_corporativo
La función `get_indice_spreads_corporativo` permite acceder a los índices de spread  Índice spread corporativo de la SBS:

| Parametro | Descripción |
| ------ | ------ |
|fechaInicial| Fecha inicial|
|fechaFinal| Fecha final|
|tipoCurva| Tipo de curva|

| tipoCurva | Descripciòn |
| ------ | ------ |
| CBCRS |    Curva Cupon Cero CD BCRP|
| CCSDF |   Curva Cupon Cero Dólares CP|
| CSBCRD | Curva Cupon Cero Dólares Sintetica|
| CCINFS | Curva Cupon Cero Inflacion Soles BCRP|
| CCCLD | Curva Cupon Cero Libor Dolares|
| CCPEDS | Curva Cupon Cero Peru Exterior Dolares - Soberana|
| CCPSS | Curva Cupon Cero Peru Soles Soberana|
| CCPVS | Curva Cupon Cero Peru Vac Soberana|

### Ejemplo
```python


import sbs_gob_pe_helper.IndiceSpreadsCorporativo as isc 
tpCurva = 'CCPSS'
fInicial = '04/08/2023'
fFinal = '04/08/2023'

#Obtiene el vector de precios de instrumentos de renta fija disponibles en la SBS para una fecha de proceso específica:
df_isc = isc.get_indice_spreads_corporativo(tipoCurva=tpCurva,fechaInicial=fInicial, fechaFinal=fFinal)

df_isc.head()
```
![IndiceSpreadsCorporativo](references/imagenes/indicecorp.png)


---

## Feedback

La mejor manera de enviar comentarios es crear un problema en https://github.com/ecandela/sbs-gob-pe-helper/issues.
Si estás proponiendo una característica:

- Explica detalladamente cómo funcionaría.
- Mantén el alcance lo más limitado posible para facilitar la implementación.
- Recuerda que este es un proyecto impulsado por voluntarios y que las contribuciones son bienvenidas :)
