# Métodos de acceso

Los archivos almacenan información. Cuando se utiliza, se debe acceder a esta información y leerla en la memoria del ordenador. Se puede acceder a la información del archivo de varias maneras. Algunos sistemas sólo proporcionan un método de acceso a los archivos, mientras que otros admiten muchos métodos de acceso.


_Secuential access_
: En el método de acceso secuencial la información del archivo se procesa en orden, un registro tras otro. Este modo de acceso es el más común; por ejemplo, los editores de texto y compiladores {cite}`aho_compilers_2006` funciona tan bien en los dispositivos de acceso secuencial como en los de acceso aleatorio.

```{note}
Compilador es un software que traduce el código fuente de un lenguaje de programación de alto nivel a un lenguaje de bajo nivel (por ejemplo, lenguaje ensamblador, código objeto o código de máquina) para crear un programa ejecutable.
```

_Direct access_
: En el método de acceso directo o acceso relativo), un archivo está compuesto por registros lógicos de longitud fija que permiten a los programas leer y escribir registros rápidamente sin ningún orden en particular. Con este método se permite el acceso aleatorio a cualquier bloque de archivos. El archivo se ve como una secuencia numerada de bloques o registros. Así, es posible leer el bloque 14, luego leer el bloque 53, y luego escribir el bloque 7. No hay restricciones en el orden de lectura o escritura para un archivo de acceso directo. Los archivos de acceso directo son de gran utilidad para el acceso inmediato a grandes cantidades de información. Las bases de datos suelen ser de este tipo. Cuando llega una solicitud de información, se calcula el bloque que contiene la respuesta y luego se ese bloque directamente para proporcionar la información deseada.

No todos los {term}`OS`s admiten el acceso secuencial y directo a los archivos. Algunos sistemas sólo permiten el acceso secuencial a los archivos; otros sólo permiten el acceso directo. Algunos sistemas requieren que un archivo se defina como secuencial o directo cuando se crea. Sólo se puede acceder a ese fichero de manera coherente con su declaración.

## Bibliografia

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```