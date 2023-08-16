sbs-gob-pe-helper
==============================

Nota : Te recomendamos revisar la [Nota legal](docs/NotaLegal.md) antes de emplear la libreria.


**sbs-gob-pe-helper** ofrece una forma Pythonica de descargar datos de mercado de la [Superintendencia de Banca y Seguros del Perú](https://www.sbs.gob.pe/), mediante web scraping (sbs web scraping).


-----------------
## Características 
A continuación se encuentran las características que aborda este paquete. :
- Curva cupón cero:
  - Extracción de datos desde la SBS.
  - Gráfica de curva.
  - Interpolación lineal de la curva.
- Vector de precio de renta fija:
  - Extracción de datos desde la SBS.
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


El módulo `CuponCero` permite acceder a los datos de bonos cupón cero de la SBS de una manera más alineada a Python:

## sbs_gob_pe_helper.CuponCero


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
```

![cupon primeros 5 registros](references/imagenes/cupon_head.png)


Si deseas visualizar la gráfica de la curva de cupón cero, sigue estos pasos:

```python
cc.plot_curva(df_cup)
```

![Abrir Terminal](references/imagenes/curva_c0.png)


Para extrapolar tasas de interes de forma lineal entonces realizar esto:


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

El módulo `VectorPrecioRentaFija` permite acceder a los datos de bonos cupón cero de la SBS de una manera más alineada a Python:

## sbs_gob_pe_helper.VectorPrecioRentaFija


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

*Los emisores disponibles se encuentran en la siguiente página: https://www.sbs.gob.pe/app/pu/CCID/Paginas/vp_rentafija.aspx



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

---



---

## Feedback

La mejor manera de enviar comentarios es crear un problema en https://github.com/ecandela/sbs-gob-pe-helper/issues.
Si estás proponiendo una característica:

- Explica detalladamente cómo funcionaría.
- Mantén el alcance lo más limitado posible para facilitar la implementación.
- Recuerda que este es un proyecto impulsado por voluntarios y que las contribuciones son bienvenidas :)