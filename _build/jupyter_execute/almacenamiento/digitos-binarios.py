# Dígitos binarios

Los computadores son capaces de representar cualquier información que pueda ser digitalizada. Esta información es almacenada en forma codificada a través de patrones de ceros (`0`) y unos (`1`), denominados _bit_ (_**bi**nary digi**t**_) {cite}`zhang_6_2008`. El _bit_ es la unidad de información más básica en los sistemas de comunicaciones digitales.

Los patrones de _bits_ pueden representar valores numéricos, caracteres de un alfabeto, signos de puntuación, imágenes y otras veces representan sonidos. Por conveniencia, el _bit_ `0` representa el valor `False` y el _bit_ `1` representa el valor `True`.

La tasa de transferencia de datos en redes de computadoras se conoce como tasa de _bits_ o ancho de banda, y generalmente se mide en términos de un múltiplo de _bits_ por segundo ({term}`bps`).

El _bit_ también se utiliza como una unidad para medir la capacidad de procesadores como las {term}`CPU` que tratan datos en fragmentos de 32 _bits_ (por ejemplo, procesadores con registros de 32 _bits_ y direcciones de memoria de 32 _bits_) y fragmentos de 64 _bits_. 

## Operaciones booleanas

Los operadores booleanos permiten manipular _bits_. Las operaciones `and`, `or`, y `xor` (`or` exclusivo) son operaciones binarias debido a que combinan dos valores (entradas) para producir un tercer valor (salida). La operación `not` se diferencia de las anteriores porque es unaria, es decir, solo requiere una entrada.

```{note}
Los operadores booleanos son denominados así en honor al matemático [George Boole](https://www.biografiasyvidas.com/biografia/b/boole.htm) (1815-1864), que fue un pionero en el campo de la lógica.
```

- **`and`**, produce una salida verdadera o falsa de una declaración formada por la combinación de dos declaraciones más pequeñas o más simples.
- **`or`**, produce un estado verdadero cuando al menos uno de sus componentes es verdadero.
- **`xor`**, produce una salida verdadera cuando sus entradas son dos valores diferentes.
- **`not`**, produce una salida que es de valor opuesto a su entrada. Por lo tanto, representa la negación de una entrada.

Las posibles entradas y valores de salidas de las operaciones booleandas son presentados en la siguiente tabla.

from myst_nb import glue

import pandas as pd
booleanas = pd.DataFrame({
    'P': [False, False, True, True,], 
    'Q': [False, True, False, True]
    })
booleanas['P and Q'] = booleanas['P'] & booleanas['Q']
booleanas['P or Q'] = booleanas['P'] | booleanas['Q']
booleanas['P xor Q'] = booleanas['P'] != booleanas['Q']
booleanas['not P'] = ~ booleanas['P']
glue('tab-booleanas', booleanas.style.hide_index())

```{glue:figure} tab-booleanas
:figwidth: 370px
:align: center
Entradas y salidas de operaciones booleanas.
```

## Notación hexadecimal

Las actividades internas de una computadora operan con patrones de _bits_, algunos de los cuales puedes contener varios dígitos, por ejemplo, `1011 0100 1000`. Debido a la complejidad en la comprensión de estas cadenas de dígitos, su representa se simplifica por medio de la notación hexadecimal.

La notación hexadecimal utiliza un símbolo para representar un patrón de cuatro _bits_. Así por ejemplo, una cadena de doce _bits_ puede ser representada por tres símbolos hexadecimales. En la siguiente tabla, la columna de la izquierda reproduce todos los patrones de _bits_ posibles de longitud cuatro; la columna de la derecha muestra el símbolo utilizado en notación hexadecimal para representar el patrón de _bits_ a su izquierda.

from src.data_convert import dec2hex, dec2bin

hexa = []
binary = []
for x in range(16):
  hexa.append(dec2hex(x))
  binary.append(dec2bin(x))
table = pd.DataFrame({
  'Patrón de bits': binary, 
  'Hexadecimal': hexa
  })
glue('tab-hexadecimal', table.style.hide_index())

```{glue:figure} tab-hexadecimal
:figwidth: 240px

Sistema de codificación hexadecimal.
```

#:tags: ["remove-cell"]
from src.data_convert import hex2bin

b5_bin = hex2bin('B5')
a4c8_bin = hex2bin('A4C8')

glue('b5-bin', b5_bin)
glue('b5-hex', 'B5')
glue('A4C8-bin', a4c8_bin)
glue('A4C8-hex', 'A4C8')

Por ejemplo, el patrón de _bits_ {glue:text}`b5-bin` se representa como {glue:text}`b5-hex` utilizando la notación hexadecimal. Esto se obtiene dividiendo el patrón de bits en cadenas de cuatro dígitos y luego representando cada cadena por su equivalente en notación hexadecimal. Así, el patrón de 16 _bits_ {glue:text}`A4C8-bin` puede reducirse a {glue:text}`A4C8-hex`.


## Bibliografia

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```