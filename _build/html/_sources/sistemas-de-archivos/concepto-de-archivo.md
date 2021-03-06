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

# Concepto de archivo

Para la mayoría de los usuarios, el sistema de archivos es el aspecto más visible de un {term}`OS`. Proporciona el mecanismo para el almacenamiento y el acceso a los datos como a los programas del {term}`OS` y a todos los usuarios del sistema. El sistema de archivos consta de dos partes

- Una colección de archivos, cada uno de los cuales almacena datos relacionados.
- Una estructura de directorios que organiza y proporciona información sobre todos los archivos del sistema.

Los computadores pueden almacenar información en diferentes medios de almacenamiento (e.g., discos magnéticos y discos ópticos). Para que el sistema informático sea conveniente de usar, el {term}`OS` proporciona una vista lógica uniforme de la información almacenada. El {term}`OS` se abstrae de las propiedades físicas de sus dispositivos de almacenamiento para definir una unidad de almacenamiento lógico, denominada archivo. Los archivos son mapeados por el {term}`OS` en los dispositivos físicos, los cuales suelen ser no volátiles, por lo que el contenido es persistente entre los reinicios del sistema.

Un archivo es una colección de información relacionada que se registra en dispositivos de almacenamiento secundario. {cite}`silberschatz_operating_2013` Desde la perspectiva del usuario, un archivo es la asignación más pequeña de almacenamiento secundario lógico; es decir, los datos no pueden escribirse en un almacenamiento secundario a menos que estén dentro de un archivo. En general, los archivos representan programas y datos. Los programas pueden estar almacenados en forma de código fuente u objeto. Los datos pueden ser de tipo numéricos, alfabéticos, alfanuméricos o binarios. Los archivos pueden ser en forma de texto (texto plano), o pueden tener un formato rígido. En general, un archivo es una secuencia de _bits_, _bytes_, líneas o registros, cuyo significado es definido por el creador y el usuario del archivo. Por lo tanto, el concepto de archivo es extremadamente general.

Un archivo puede contener diferente tipo información: código fuente o archivos ejecutables, datos numéricos o de texto, fotos, música, vídeo, etc. Un archivo tiene una estructura definida, la cual depende de su tipo. Un archivo de texto es una secuencia de caracteres organizados en líneas (y posiblemente páginas). Un archivo de código fuente es una secuencia de funciones, cada una de las cuales se organiza a su vez como instrucciones de declaraciones ejecutables. Un archivo ejecutable es una serie de secciones de código que el cargador puede traer a la memoria y ejecutar.

## Atributos de archivos

Para la conveniencia de los usuarios los archivos son identificados, y se hace referencia a él por su nombre. Este nombre suele ser una cadena de caracteres, como por ejemplo `prueba.txt`. Algunos sistemas de archivos diferencian entre mayúsculas y minúsculas en los nombres, mientras que otros sistemas no. Cuando se le asigna nombre a un archivo, éste se independiza del proceso, del usuario e incluso del sistema que lo ha creado. Por ejemplo, un usuario puede crear el archivo `ejemplo.txt` y otro usuario puede editarlo especificando su nombre. El propietario del archivo podría escribirlo en un dispositivo {term}`USB`, enviarlo como un archivo adjunto de correo electrónico o copiarlo a través de una red, y aún así podría llamarse `ejemplo.txt` en el sistema de destino.

Los atributos de un archivo varían de un {term}`OS` a otro, pero normalmente son los siguientes.

- Nombre simbólico del archivo, es la única información que se mantiene en forma legible para las personas.
- Etiqueta única (identificador), normalmente un número, identifica el archivo en el sistema de archivos.
- Información del tipo de archivo, necesaria para los sistemas que admiten diferentes tipos de archivos.
- Puntero a un dispositivo y a la ubicación del archivo (_path_) en el dispositivo.
- El tamaño actual del archivo (generalmente en bytes o bloques) y posiblemente el tamaño máximo permitido.
- Información de control de acceso que determina quién puede leer, escribir, ejecutar, etc.
- Información de la hora, fecha e identificación del usuario. Esta información puede ser guardada para su creación, última modificación y último uso. Estos datos pueden ser útiles para la protección, la seguridad y el control de uso.

```{figure} ../images/archivo-info.png
:height: 500px
:align: center
:name: fig-archivo-info

Atributos de un archivo (ventana de MS Windows)
```

Algunos de los sistemas de archivos más recientes también admiten atributos extendidos de los archivo, incluida la codificación de caracteres (e.g., UTF-8, Unicode) y características de seguridad. La {numref}`fig-archivo-info` muestra los atributos de un archivo en ventanas con información proporcionada por Windows.

La información referida a todos los archivos se mantiene en la estructura de directorios, que también reside en el almacenamiento secundario. Típicamente, una entrada de directorio consiste en el nombre del archivo y su identificador único. El identificador a su vez localiza los demás atributos del archivo. Puede ser necesario más de un kilobyte para registrar esta información para cada archivo. En un sistema con muchos archivos, el tamaño del directorio en sí puede ser de megabytes. Dado que los directorios, como los archivos, deben ser no volátiles, deben ser almacenados en el dispositivo y llevados a la memoria según sea necesario.

## Operaciones con archivos

Un archivo es un tipo de dato abstracto. Cualquier sistema de archivos proporciona no solo un medio para almacenar datos organizados como archivos, sino una colección de funciones que se pueden realizar en archivos. Las operaciones típicas incluyen,

- __Crear__, define y posiciona un nuevo archivo dentro de la estructura de archivos.
- __Eliminar__, elimina un archivo de la estructura de archivos y se destruye.
- __Abrir__, un archivo existente se declara para ser _abierto_ por un proceso, lo que permite que el proceso realice funciones en el archivo.
- __Cerrar__, cierra un archivo con respecto a un proceso, de modo que dicho proceso ya no pueda realizar funciones en el archivo, hasta que el proceso lo abra nuevamente.
- __Leer__, un proceso lee todos o una parte de los datos de un archivo.
- __Escribir__, un proceso actualiza un archivo, ya sea agregando nuevos datos que expanden el tamaño del archivo o cambiando los valores de los elementos de datos existentes en el archivo.

Normalmente, un sistema de archivos mantiene un conjunto de atributos asociados con el archivo. Estos incluyen el propietario, la hora de creación, la hora de la última modificación y los privilegios de acceso (ver {numref}`fig-archivo-info`).

La mayoría de las operaciones de archivo mencionadas implican la búsqueda en el directorio de la entrada asociada al archivo nombrado. Para evitar esta búsqueda constante, muchos sistemas requieren que se haga una llamada al sistema (abrir el archivo) antes de utilizar un archivo por primera vez. El {term}`OS` mantiene una tabla de archivos abiertos con la información de todos los archivos abiertos. Cuando se solicita una operación de archivo, el archivo se especifica mediante un índice en esta tabla, por lo que no es necesario realizar ninguna búsqueda. Cuando el archivo ya no se utiliza activamente, el proceso lo cierra (o debe cerrarlo) y el {term}`OS` elimina su entrada de la tabla de archivos abiertos. Las operaciones de creación y eliminación son llamadas al sistema que funcionan con archivos cerrados en lugar de abiertos.

Algunos sistemas abren implícitamente un archivo cuando se hace la primera referencia a él. El archivo se cierra automáticamente cuando termina el trabajo o el programa que lo abrió. Sin embargo, la mayoría de los sistemas requieren que el programador abra un archivo explícitamente con la llamada de sistema antes de que se pueda usar ese archivo. Esta operación toma el nombre de archivo y busca en el directorio, copiando la entrada del directorio en la tabla de archivos abiertos. Esta llamada además puede aceptar el acceso a la información en modo de creación, sólo lectura, lectura-escritura, sólo adición, etc. Este modo se comprueba con los permisos del archivo. Si el modo de solicitud está permitido, el archivo se abre para el proceso.

La información asociadas a un archivo abierto puede resumirse en: el rastreo de la ultima posición de lectura/escritura, un recuento de los archivos abiertos, la información necesaria para localizar el archivo en disco y los tipos de permisos de acceso al archivo para autorizar o denegar solicitudes. Algunos {term`}OS`s ofrecen facilidades para bloquear un archivo, impidiendo que otros procesos accedan a él. Esta funcionalidad impide, por ejemplo, que archivos compartidos por varios procesos puedan modificarlo de forma simultánea, hasta que se libere el bloqueo. En otros casos, podría proporcionarse accesos de lectura de un archivo compartido, que se encuentra bloqueado por algún proceso.

## Tipos de archivos

Si un {term}`OS` reconoce un tipo de un archivo, puede entonces operar con el archivo de maneras razonables. Una técnica común para implementar los tipos de archivo es incluir su tipo como parte del nombre del archivo. El nombre de un archivo se divide en el nombre y una extensión, normalmente separados por un punto. De esta forma, el usuario y el {term}`OS` pueden saber, sólo por el nombre, qué tipo de archivo es.

La mayoría de los sistemas operativos permiten a los usuarios especificar un nombre de archivo como una secuencia de caracteres seguida de un punto y terminada por una extensión compuesta de caracteres adicionales.

```{code-cell} ipython3
:tags: ["remove-cell"]

from myst_nb import glue

import pandas as pd

tipos = pd.read_csv('./data/tipos_archivos.csv', delimiter="\t")
glue('tab-tipos-archivos', tipos.style.hide_index())
```

```{glue:figure} tab-tipos-archivos
:name: tab-hola_ascii
:align: left

Ejemplos de tipos de archivos.
``` 

El {term}`OS` utiliza la extensión para indicar el tipo de archivo y el tipo de opera- ciones que se pueden realizar en ese archivo. Los programas de aplicación también utilizan extensiones para indicar los tipos de archivos en los que están interesados. Estas extensiones no siempre son necesarias, por lo que un usuario puede especificar un archivo sin la extensión (para evitar tener que escribir), y la aplicación buscará un archivo con el nombre y la extensión que espera.

## Estructura de archivos

Los tipos de archivos también pueden utilizarse para indicar la estructura interna del archivo. Los siguientes términos ({numref}`fig-estructura-archivo`) son de uso común en este contexto {cite}`stallings_operating_2015`:

```{figure} ../images/estructura-archivo.png
:height: 180px
:align: center
:name: fig-estructura-archivo

Conceptos comunes de estructuras de archivos.
```

Campo
: Es el elemento básico de los datos. Un campo individual contiene un valor único, como el apellido de un empleado, una fecha o el valor de la lectura de un sensor. Se caracteriza por su longitud y tipo de datos (por ejemplo, cadena {term}`ASCII`, decimal. Dependiendo del diseño del archivo, los campos pueden tener una longitud fija o variable. En el último caso, el campo a menudo consta de dos o tres subcampos: el valor real que se va a almacenar, el nombre del campo y, en algunos casos, la longitud del campo. En otros casos de campos de longitud variable, la longitud del campo se indica mediante el uso de símbolos de demarcación especiales entre campos.

Registro
: Es una colección de campos relacionados que algún software de aplicación puede tratar como una unidad. Por ejemplo, un registro de empleado contendría campos como nombre, número de seguro social, clasificación del trabajo, fecha de contratación, etc. Nuevamente, dependiendo del diseño, los registros pueden tener una longitud fija o variable. Un registro será de longitud variable si algunos de sus campos son de longitud variable o si el número de campos puede variar. En el último caso, cada campo suele ir acompañado de un nombre de campo.

Archivo
: Es una colección de registros similares. Los usuarios y las aplicaciones tratan el archivo como una entidad única y se puede hacer referencia a él por su nombre.
Los archivos tienen nombre y se pueden crear y eliminar. Las restricciones de control de acceso generalmente se aplican a nivel de archivo. Es decir, en un sistema compartido, a los usuarios y programas se les concede o restringe el acceso a archivos completos.

Base de datos
: Es una colección de datos relacionados. Los aspectos esenciales de una base de datos son que las relaciones que existen entre los elementos de los datos son explícitas y que la base de datos está diseñada para ser utilizada por varias aplicaciones diferentes. Una base de datos puede contener toda la información relacionada con una organización o un proyecto, como una empresa o un estudio científico. La base de datos en sí consta de uno o más tipos de archivos. Por lo general, existe un sistema de administración de base de datos independiente que es independiente del {term}`OS`, aunque ese sistema puede hacer uso de algunos programas de administración de archivos. 

Cabe señalar que no todos los archivos presentan el tipo de estructura presentado anteriormente. En algunos sistemas, la estructura de archivo básica es solo un flujo de bytes. Por ejemplo, un programa en Python se almacena como un archivo pero no tiene campos, registros, etc. 

Todos los {term}`OS` deben soportar al menos una estructura de archivo, la de un archivo ejecutable, para que el sistema sea capaz de cargar y ejecutar programas. Además, cada software de aplicación debe incluir su propio código para interpretar un archivo de entrada en cuanto a la estructura apropiada, de lo contrario, cuando las nuevas aplicaciones requieren información estructurada de manera no soportada por el {term}`OS`, pueden errores.

Los sistemas de disco suelen tener un tamaño de bloques bien definido determinado por el tamaño de un sector. Todas las entradas/salidas de los discos se realizan en unidades de un bloque (registro físico), y todos los bloques tienen el mismo tamaño. Es poco probable que el tamaño del registro físico coincida exactamente con la longitud del registro lógico deseado. Los registros lógicos pueden incluso variar en longitud. El empaquetamiento de varios registros lógicos en bloques físicos es una solución común a este problema.

El tamaño del registro lógico, el tamaño del bloque físico y la técnica de empaquetamiento determinan cuántos registros lógicos hay en cada bloque físico. El empaquetamiento puede ser hecho por el programa de aplicación del usuario o por el {term}`OS`. En cualquier caso, el archivo puede ser considerado como una secuencia de bloques. Todas las funciones básicas de entrada/salida operan en términos de bloques. La conversión de registros lógicos a bloques físicos es un problema de software relativamente simple.

Dado que el espacio de disco siempre se asigna en bloques, generalmente se desperdicia una parte del último bloque de cada archivo. Si cada bloque fuera de 512 bytes, por ejemplo, a un fichero de 1949 bytes se le asignarían cuatro bloques (2048 bytes); los últimos 99 bytes se desperdiciarían. El desperdicio que se produce al mantener todo en unidades de bloques (en lugar de bytes) se conoce como fragmentación interna. Todos los sistemas de archivos sufren de fragmentación interna; cuanto mayor sea el tamaño del bloque, mayor será la fragmentación interna.

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```