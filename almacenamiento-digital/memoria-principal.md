---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Memoria principal

Para el almacenamiento de datos, un computador contiene una gran colección de circuitos o _flip-flops_, cada uno de los cuales es capaz de almacenar un solo _bit_. Este depósito de _bits_ se conoce como la memoria principal de la máquina.

```{note}
Los _flip-flops_ se utilizan como elementos de almacenamiento de datos. Un _flip-flop_ es un dispositivo que almacena un solo _bit_ de datos. Es el elemento básico de almacenamiento en la lógica secuencial. Los _flip-flops_ son bloques de construcción fundamentales de los sistemas electrónicos digitales utilizados en los computadores, las comunicaciones y otros tipos de sistemas.
```

La capacidad de almacenamiento de una memoria se mide en _bits_. Usualmente, un registro digital u otras memorias digitales, tengan una capacidad de representación de informaciones expresada en múltiplos de 8 _bits_. Una cadena de 8 _bits_ se denomina _byte_.

## Organización de la memoria

La memoria principal está organizada en unidades denominadas celdas, con un tamaño típico de ocho bits. De este modo, pequeñas computadoras integradas en dispositivos domésticos (por ejemplo, hornos microondas, lavadoras) pueden tener memorias principales que consisten cientos de celdas, mientras computadores pueden tener millones de celdas en sus memorias principales.

```{figure} ../images/byte.png
:height: 100px
:name: fig-byte

Organización de un _byte_ en una celda
```

Normalmente, los _bits_ dentro de una celda de memoria están dispuestos en una fila ({numref}`fig-byte`). El _bit_ de la izquierda se llama _bit_ más significativo en referencia al hecho de que si el contenido de la celda se interpretara como la representación de un valor numérico, este _bit_ sería el dígito más significativo del número. Del mismo modo, el _bit_ de la derecha se denomina _bit_ menos significativo.

```{figure} ../images/memoria-celdas.png
:name: fig-memoria-celdas
:figclass: margin
     
Representación de celdas de una memoria.
```

Para identificar las celdas individuales de la memoria principal de una computadora, a cada celda se le asigna un identificador único o dirección. Tal sistema de direcciones no sólo permite una forma de identificar de forma única cada celda, sino que también asocia un orden a las celdas ({numref}`fig-memoria-celdas`).

La asignación de un orden tanto a las celdas de la memoria como a los bits dentro de cada celda, permite todo el conjunto de _bits_ dentro de la memoria principal está esencialmente ordenado en una larga fila. Los segmentos de esta fila pueden por lo tanto utilizarse para almacenar patrones de bits que pueden ser más largos que la longitud de una celda. Por ejemplo, es posible almacenar una cadena de 16 _bits_ simplemente usando dos celdas consecutivas de memoria.

Esta organización de memoria permite que otros circuitos pueden obtener datos de la memoria solicitando electrónicamente el contenido de una cierta dirección (operación de lectura), o pueden registrar información en la memoria solicitando que se registre un cierto patrón de _bits_ en la celda en una dirección particular (operación de escritura).

## Memoria RAM

Considerando que las celdas de la memoria son individuales y direccionables, se puede acceder a las células de forma independiente según se requiera. Para reflejar la capacidad de acceder a las celdas en cualquier orden, la memoria principal de una computadora suele denominarse {term}`RAM`.

La {term}`RAM` en la mayoría de los computadores modernos se construye utilizando tecnologías análogas, pero más complejas, que proporcionan una mayor miniaturización y un tiempo de respuesta más rápido. Muchas de estas tecnologías almacenan  _bits_  como pequeñas cargas eléctricas que se disipan rápidamente. Por lo tanto, estos dispositivos requieren de circuitos adicionales, conocidos como circuitos de actualización, que repiten las cargas muchas veces por segundo. Esta tecnología a menudo se denomina memoria dinámica ({term}`DRAM`). Otras veces se utilizan tecnología {term}`DRAM` sincrónico ({term}`SDRAM`), que en relación a la {term}`DRAM`, aplica técnicas adicionales para disminuir el tiempo para recuperar el contenido de sus celdas {cite}`noauthor_whats_2018`.

Es usual que los sistemas de memoria principal estén diseñados de tal forma que el número total de celdas sea expresador en potencia de dos. En este sentido, la comunidad adoptó el prefijo kilo en referencia a la unidad 1024, debido a su cercanía con mil. Es decir, el término kilobyte (KB) se usó para referirse a 1024 _bytes_. Por lo tanto, se decía que una máquina con 4096 celdas de memoria tenía una memoria de 4KB (4096 = 4 x 1024). Esta terminología también se extendió a otros múltiplos, como el megabyte, gigabyte, terabyte, entre otros. 

```{code-cell} ipython3
:tags: ["remove-input"]

import pandas as pd

table = pd.read_pickle('./data/multiplos_del_bit.pickle')
si = table['Prefijo del SI(SI)']
unidad = []
multiplo = []
for i in range(len(si)):
    unidad.append('{} ({})'.format(si.loc[i, 'Nombre'], si.loc[i, 'Símbolo']))
    multiplo.append('10<sup>{}</sup>'.format(3*(i+1)))

df = pd.DataFrame({'Sistema Internacional (SI)': unidad, 'Múltiplo': multiplo})

df.style.hide_index()
```

Desafortunadamente, esta aplicación de prefijos representa un mal uso de la terminología porque estos se usan en referencia a unidades que son potencias de mil. A fines de la década de 1990, las organizaciones de estándares internacionales desarrollaron terminología especializada {cite}`thor_prefixes_2000` para potencias de dos.

```{code-cell} ipython3
:tags: ["remove-input"]

si = table['Prefijo binario(IEC 60027-2)']
unidad = []
multiplo = []
for i in range(len(si)):
    unidad.append('{} ({})'.format(si.loc[i, 'Nombre'], si.loc[i, 'Símbolo']))
    multiplo.append('2<sup>{}</sup>'.format(10*(i+1)))

df = pd.DataFrame({'Binario (IEC 60027-2)': unidad, 'Múltiplo': multiplo})

df.style.hide_index()
```

## Bibliografia

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```