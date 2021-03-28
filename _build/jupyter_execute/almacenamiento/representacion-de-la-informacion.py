# Representación de la información

Habiendo revisado técnicas para almacenar _bits_, ahora se revisan las formas para codificar información como patrones de _bits_. Se presentan algunos métodos populares para codificar texto, datos numéricos e imágenes.

## Texto

El texto normalmente se representa mediante un código en el que a cada uno de los diferentes símbolos (e.g., letras del alfabeto, símbolos, numeros) se le asigna un patrón de _bits_ único. El texto se representa como una larga cadena de _bits_ en la que los patrones sucesivos representan los símbolos sucesivos en el texto original.

import pandas as pd
from src.data_convert import word2charlist, dec2bin
from myst_nb import glue

word = word2charlist('Hola!')
table = pd.DataFrame({'Codificación ASCII o UTF-8': word})
for i in range(len(table)):
    decimal = ord(table.loc[i,'Codificación ASCII o UTF-8'])
    table.loc[i, 'Patrón binario'] = dec2bin(decimal, 8)
glue('tab_hola_ascii', table.style.hide_index())

```{glue:figure} tab_hola_ascii
:name: tab-hola_ascii
:align: left

Palabra "Hola!" codificada en {term}`ASCII`.
``` 

Entre los años 1940 y 1950, muchos de estos códigos fueron diseñados y utilizados en conexión con diferentes equipos, produciendo la correspondiente proliferación de problemas de comunicación. Para aliviar esta situación, el {term}`ANSI` adoptó el {term}`ASCII`. Este código ([ver código](https://www.ascii-code.com/)) utiliza patrones de siete _bits_ para representar las letras mayúsculas y minúsculas del alfabeto inglés, los símbolos de puntuación, los dígitos del 0 al 9 y cierta información de control, como los avances de línea y los retornos de carro. Este código se extiende a un formato de ocho _bits_ por símbolo agregando un 0 en el extremo más significativo de cada uno de los patrones de siete _bits_. Esta técnica no solo produce un código en el que cada patrón encaja convenientemente en una celda de memoria típica de tamaño de un _byte_, sino que también proporciona 128 patrones de _bits_ adicionales (obtenidos al asignar al _bit_ adicional el valor 1) que se pueden usar para representar símbolos más allá de el alfabeto inglés y su puntuación.

La [ISO](https://www.iso.org/) ha desarrollado una serie de extensiones de {term}`ASCII`, cada una fue diseñada para adaptar a un grupo principal de idiomas. Por ejemplo, para incluir símbolos necesarios para expresar el texto de la mayoría de los idiomas. Sin embargo, surgieron dos inconvenientes. El primero, el número de patrones de _bits_ adicionales disponibles en {term}`ASCII` extendido es insuficiente para adaptar el alfabeto de muchos idiomas (e.g., asiáticos, Europa oriental). El segundo, debido a que un documento dado estaba limitado a usar símbolos en el único estándar seleccionado, los documentos que contenían texto de  grupos de idiomas dispares no pudieron ser soportados. Para abordar esta deficiencia, [Unicode](https://home.unicode.org/) se desarrolló a través de la cooperación de varios de los principales fabricantes de hardware y software {cite}`vacca_unicode_1991`. Este código utiliza un patrón único de hasta 21 _bits_ para representar cada símbolo. Cuando el juego de caracteres Unicode se combina con el estándar de codificación UTF-8, los caracteres {term}`ASCII` originales todavía se pueden representar con 8 _bits_, mientras que los miles de caracteres adicionales de idiomas como chino, japonés y hebreo se puede representar con 16 _bits_. Más allá de los caracteres necesarios para todos los idiomas de uso común en el mundo, UTF-8 utiliza patrones de 24 o 32 _bits_ para representar símbolos Unicode más oscuros, lo que deja un amplio espacio para futuras expansiones.

```{note}
UTF-8 es un formato de codificación de caracteres Unicode e [ISO 10646](https://www.iso.org/standard/69119.html) que utiliza símbolos de longitud variable. Divide los caracteres Unicode en varios grupos, en función del número de _bytes_ necesarios para codificarlos. El número de _bytes_ depende exclusivamente del código de carácter asignado por Unicode y del número de _bytes_ necesario para representarlo.
```

Un archivo que consiste en una larga secuencia de símbolos codificados con {term}`ASCII` o Uincode se suele denominar archivo de texto (o archivo de texto plano). Es importante distinguir entre archivos de texto simples que son manipulados por programas de utilidad llamados editores de texto (e.g., [Notepad](https://www.microsoft.com/en-us/p/windows-notepad/9msmlrh6lzf3?activetab=pivot:overviewtab) de Microsoft) y los archivos más elaborados producidos por procesadores de texto como [Word](https://www.microsoft.com/es-ww/microsoft-365/word) de Microsoft. Un archivo de texto contiene solo una codificación carácter por carácter del texto, mientras que un archivo producido por un procesador de textos contiene numerosos códigos propietarios que representan cambios en las fuentes, información de alineación y otros parámetros (texto enriquecido).

## Valores numéricos

El almacenamiento de información en términos de caracteres codificados es ineficiente cuando la información a almacenar es numérica. Los símbolos codificados en {term}`ASCII` usan un _byte_ por símbolo. En consecuencia, el número más grande que podríamos almacenar, por ejemplo, usando 16 _bits_ es 99. Con esta notación podemos almacenar cualquier número entero en el rango de 0 a 65535 en solo 16 _bits_. Debido a esta eficiencia, es común almacenar información numérica en forma de notación binaria en lugar de símbolos codificados.

from src.data_convert import dec2bin
dec_130 = 130
bin_130 = dec2bin(dec_130, 8)
glue('bin-130', bin_130)

```{margin} 
Un algoritmo es un conjunto ordenado de pasos, sin ambigüedades, ejecutables que definen un proceso a concluir {cite}`brookshear_computer_2015`. Informalmente, es un conjunto de pasos para llevar a cabo una tarea, algunos ejemplos que podrían considerarse algoritmos son, recetas de comidas, instruccion de uso de artefactos, instrucciones para llegar a una dirección, entre otros.
```

````{admonition} Tip
:class: tip

Un algoritmo para encontrar la representación binaria de una entero positivo consiste en,

1. Dividir el valor decimal por dos y registrar el resto.
1. Mientras el cociente obtenido no sea cero, continar dividiendo el último cociente por 2 y registrar el resto.
1. Una vez obtenido un cociente de 0, la representación binaria del valor original está formada por los restos listados de derecha a izquierda en el orden en que fueron registrados.

La ejecución del algoritmo permite verificar que la representación del número 130 es {glue:text}`bin-130`.

Para convertir una representación binaria a entero positivo consiste en,

1. Iniciando desde [el _bit_ menos significativo](fig-byte), multiplicar cada dígito binario por dos elevado a la potencia consecutiva, comenzando desde la potencia 0.
2. Sumar todas las multiplicaciones.
````

## Imágenes

Una forma de representar una imagen es interpretar la imagen como una colección de puntos, cada uno de los cuales se denomina _pixel_ (_**pi**cture **el**ement_). La apariencia de cada píxel se codifica y la imagen completa se representa como una colección de estos píxeles codificados. Tal colección se llama mapa de _bits_ ({numref}`fig-bitmap`). Este enfoque es popular porque muchos dispositivos de visualización, como impresoras y pantallas, funcionan con el concepto de píxeles. A su vez, las imágenes en forma de mapa de _bits_ se formatean fácilmente para su visualización.

```{figure} ../images/bitmap.png
:figclass: margin
:name: fig-bitmap

Mapa de _bits_.
```

El método de codificación de los píxeles en un mapa de _bits_ varía entre las aplicaciones. En el caso de una simple imagen en blanco y negro, cada píxel se puede representar con un solo _bit_ cuyo valor depende de si el píxel correspondiente es blanco o negro. Este es el enfoque utilizado por la mayoría de las máquinas de fax. Para fotografías en blanco y negro más elaboradas, cada píxel se puede representar mediante una colección de _bits_ (generalmente ocho), lo que permite representar una variedad de tonos de gris. En el caso de las imágenes en color, cada píxel está codificado por un sistema más complejo. La codificación RGB es un enfoque frecuentemente usado para esto. En esta, cada píxel se representa como tres componentes de color: un componente rojo, un componente verde y un componente azul, correspondientes a los tres colores primarios de la luz. Un _byte_ se usa normalmente para representar la intensidad de cada componente de color. A su vez, se requieren tres _bytes_ de almacenamiento para representar un solo píxel en la imagen original.

Una desventaja de representar imágenes como mapas de _bits_ es que una imagen no se puede escalar fácilmente a ningún tamaño arbitrario. Esencialmente, la única forma de agrandar la imagen es hacer que los píxeles sean más grandes, lo que conduce a una apariencia granulada. Esta técnica es denominada zoom digital utilizada en cámaras digitales en lugar de zoom óptico que se obtiene ajustando la lente de la cámara.

Una forma alternativa de representar imágenes que evita el problema de escala es describir la imagen como una colección de estructuras geométricas, como líneas y curvas, que pueden codificarse utilizando técnicas de geometría analítica. Tal descripción permite que el dispositivo que finalmente muestra la imagen decida cómo deben mostrarse las estructuras geométricas en lugar de insistir en que el dispositivo reproduzca un patrón de píxeles particular. Este es el enfoque utilizado para producir las fuentes escalables que están disponibles a través de los sistemas de procesamiento de texto actuales. Por ejemplo, TrueType (desarrollado por [Microsoft](https://docs.microsoft.com/en-us/typography/) y Apple) es un sistema para describir geométricamente símbolos de texto. 

```{note}
TrueType fue diseñado originalmente por [Apple Computer, Inc](https://www.apple.com/), para ser eficiente en almacenamiento y procesamiento, y extensible. Su implementación lo hace extremadamente potente al diseñar caracteres para mostrar en una pantalla. {cite}`jacobs_brief_2018`
```

Del mismo modo, PostScript (desarrollado por Adobe Systems) proporciona un medio para describir caracteres, así como datos pictóricos más generales. Este medio geométrico para representar imágenes también es popular en los sistemas {cite}`sarcar_computer_2008` {term}`CAD`, o también denominados {term}`CADD`, en los cuales que se muestran y manipulan dibujos de objetos tridimensionales (e.g., diseños estructurales, mapas) en las pantallas de visualización de un computador. AutoCAD es un ejemplo de _software_ {term}`CAD` utilizado para dibujos 2D y modelado 3D. Actualmente es desarrollado y comercializado por la empresa [Autodesk](https://www.autodesk.com/).

```{note}
El término {term}`CAD` se refiere al uso de computadores o estaciones de trabajo para apoyar la creación, modificación, análisis u optimización de un diseño. El resultado generado suele ser en forma de archivos electrónicos para la impresión, el mecanizado u otras operaciones de fabricación.
```

La distinción entre representar una imagen en forma de estructuras geométricas en lugar de mapas de _bits_ es evidente para los usuarios de muchos sistemas de software de dibujo (e.g., Paint de Microsoft) que permiten al usuario dibujar imágenes que consisten en formas preestablecidas, como rectángulos, óvalos y curvas elementales. El usuario simplemente selecciona la forma geométrica deseada de un menú y luego dirige el dibujo de esa forma con un mouse. Durante el proceso de dibujo, el software mantiene una descripción geométrica de la forma que se está dibujando. A medida que el mouse da las instrucciones, la representación geométrica interna se modifica, se convierte a un mapa de _bits_ y se muestra. Esto permite escalar y dar forma fácilmente a la imagen. Sin embargo, una vez que se completa el proceso de dibujo, la descripción geométrica subyacente se descarta y solo se conserva el mapa de _bits_, lo que significa que las alteraciones adicionales requieren un proceso de modificación píxel por píxel. Por otro lado, otros sistemas de dibujo conservan la descripción como formas geométricas que pueden modificarse más adelante. Con estos sistemas, las formas se pueden redimensionar fácilmente, manteniendo una visualización nítida en cualquier dimensión.

Los mapas de _bits_ a menudo son muy grandes. A su vez, se han desarrollado numerosos esquemas de compresión específicamente para representaciones de imágenes.
 
El sistema {term}`GIF` es un formato de imagen de mapa de _bits_ desarrollado por un equipo del proveedor de servicios en línea [CompuServe](https://www.compuserve.com/). Desde entonces, ha tenido un uso generalizado en la {term}`WWW` debido a su amplio soporte y portabilidad entre aplicaciones y sistemas operativos. Este formato admite hasta 8 _bits_ por píxel para cada imagen, lo que permite que una sola imagen haga referencia a su propia paleta de hasta 256 colores diferentes elegidos del espacio de color RGB de 24 _bits_. Si un color de la imagen original no aparece en la tabla de colores de consulta, la aplicación selecciona el color más cercano en la tabla o simula el color mediante una combinación de colores disponibles. En consecuencia, se acerca al problema de la compresión reduciendo el número de colores que se pueden asignar a un píxel a solo 256, sin embargo, esta compresión es con pérdida cuando se aplica a imágenes arbitrarias porque los colores en la paleta pueden no ser idénticos a los colores en la imagen original. 

```{figure} ../images/gif-transparente.png
:figclass: margin
:name: fig-gif_transparente

Ejemplos de transparencia (a la izquierda) en formato {term}`GIF`.
```

Normalmente, a uno de los colores en una paleta {term}`GIF` se le asigna el valor "transparente", lo que significa que el fondo puede mostrarse a través de cada región asignada a este "color" ({numref}`fig-gif_transparente`). Esta opción, combinada con la relativa simplicidad del sistema {term}`GIF`, lo convierte en una opción lógica en aplicaciones de animación simples en las que varias imágenes en movimiento (animación). Por otro lado, su capacidad para codificar solo 256 colores lo hace inadecuado para aplicaciones en las que se requiere una mayor precisión, como en el campo de la fotografía. No admite audio.

```{figure} ../images/gif-compresion.png
:figclass: margin
:name: fig-gif_compresion

Ejemplos de compresión en formato {term}`GIF`.
```

Algunos algoritmos de compresión reducen el tamaño del archivo descartando datos de forma selectiva. Cuanto más alto sea el ajuste de compresión, más datos se descartarán. A menudo se puede aplicar un valor de menos calidad para reducir el tamaño de archivo entre un 5% y un 40% del original ({numref}`fig-gif_compresion`).

Habitualmente, se cree que JPEG es un tipo de imagen. Técnicamente, JPEG no es un tipo de imagen, es un estándar de compresión formalmente conocido como {term}`Exif`. El grado de compresión se puede ajustar, lo que permite una compensación elegible entre el tamaño de almacenamiento y la calidad de la imagen. La base para JPEG es la {term}`DCT` {cite}`khayam_discrete_2003`, una técnica de compresión de imagen con pérdida de calidad. Esta rutina de compresión está integrada en el software de una cámara digital, tomando el flujo de datos del sensor de la cámara y comprimiéndolo o codificándolo en una forma que luego puede ser leída por algún software, como por ejemplo,  navegador web, aplicaciones de edición, entre otros.

```{note}
{term}`Exif` es una especificación para formatos de archivos de imagen usado por las cámaras digitales. La especificación usa los formatos de archivos existentes como JPEG y {term}`TIFF` a los que se agrega etiquetas específicas de metadatos.
```

JPEG es un estándar desarrollado por el _Joint Photographic Experts Group_ de {term}`ISO`. Ha demostrado ser un estándar efectivo para comprimir fotografías en color y es ampliamente utilizado en la industria de la fotografía, como lo demuestra el hecho de que la mayoría de las cámaras digitales usan JPEG como su técnica de compresión predeterminada.

Otro sistema de compresión de imágenes es {term}`TIFF`. Sin embargo, su uso más popular no es como un medio de compresión, sino como un formato estandarizado para almacenar fotografías junto con información relacionada, como la fecha, la hora y la configuración de la cámara. En este contexto, la imagen en sí se almacena normalmente como componentes de píxeles RGB sin compresión. La opción de compresión de imagen en color incluida en los estándares {term}`TIFF` se basa en técnicas similares a las utilizadas por {term}`GIF` y, por lo tanto, no se utilizan ampliamente en la comunidad de la fotografía.

## Bibliografia

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```