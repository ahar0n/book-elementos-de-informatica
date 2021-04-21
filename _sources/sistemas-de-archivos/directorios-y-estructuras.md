# Directorios y estructuras

Ciertamente, ningún ordenador de propósito general almacena sólo un archivo; normalmente son muchos. Los archivos se almacenan en dispositivos de almacenamiento de acceso aleatorio, incluyendo {term}`HDD`, discos ópticos y {term}`SSD`.

Un dispositivo de almacenamiento puede utilizarse en su totalidad para un sistema de archivos. También puede subdividirse para un control más fino. Por ejemplo, un disco puede ser dividido en cuartos, y cada cuarto puede contener un sistema de archivos separado.

La partición de discos es útil para limitar los tamaños de los sistemas de archivos individuales, poner varios tipos de sistemas de archivos en el mismo dispositivo o dejar parte del dispositivo disponible para otros usos, como espacio de intercambio o espacio de disco sin formatear (_raw_). Se puede crear un sistema de archivos en cada una de estas partes del disco. Cualquier entidad que contenga un sistema de archivos se conoce generalmente como volumen. El volumen puede ser un subconjunto de un dispositivo, un dispositivo completo o varios dispositivos vinculados entre sí en un conjunto {term}`RAID`. Cada volumen puede considerarse como un disco virtual. Los volúmenes también pueden almacenar múltiples {term}`OS`s, permitiendo que un computador se inicie y ejecute más de un {term}`OS`.

```{note} 
{term}`RAID` hace referencia a un sistema de almacenamiento de datos que utiliza múltiples unidades ({term}`HDD` o {term}`SSD`), entre las cuales se distribuyen o replican los datos... [leer más acerca de sistemas RAID](https://www.computerlanguage.com/results.php?definition=RAID)
```

```{figure} ../images/file-system-org.png
:height: 250px
:figclass: margin
:name: fig-organizacion-file-system

Organización típica de un sistema de archivos.
```

Cada volumen que contiene un sistema de archivos también debe contener información sobre los archivos del sistema. Esta información se guarda en entradas en un directorio de dispositivos o en un índice de volúmenes. El directorio de dispositivos (comúnmente conocido simplemente como directorio) registra información -como el nombre, la ubicación, el tamaño y el tipo- de todos los archivos de ese volumen. La {numref}`fig-organizacion-file-system` muestra una organización típica de un sistema de archivos.

Considerando que los sistemas de archivos pueden ser extensos, es útil segregar los archivos en grupos y gestionar y actuar sobre esos grupos. Esta organización implica el uso de directorios, que en sí mismos son archivos.

Un directorio puede verse como una tabla de símbolos que traduce los nombres de los archivos a sus entradas de directorio y, puede ser organizado de muchas maneras. La organización debe permitir insertar entradas, borrarlas, buscar una entrada con nombre y listar todas las entradas del directorio. Algunas de las operaciones básicas soportadas por las estructuras de directorio se presentan a continuación {cite}`tanenbaum_modern_2015`.

- __Crear__ un directorio.
- __Eliminar__ un directorio. En general, sólo se puede borrar un directorio vacío.
- __Abrir__, directorios. Los directorios pueden ser leidos, por ejemplo, para listar todos los archivos en un directorio, un programa abre el directorio para leer los nombres de todos los archivos que contiene. Antes de poder leer un directorio, debe abrirse, de forma análoga a abrir y leer un archivo.
- __Cerrar__ directorio. Cuando se ha leído un directorio, debe cerrarse para liberar espacio de tabla interno.
- __Renombrar__ un directorio. En muchos aspectos, los directorios son como archivos y se pueden renombrar de la misma manera que los archivos.
- __Link__, es una técnica que permite que un archivo aparezca en más de un directorio. Esta llamada al sistema especifica un archivo existente y un nombre de ruta (_path_), y crea un enlace desde el archivo existente al nombre especificado por la ruta. De esta forma, el mismo archivo puede aparecer en varios directorios.
- __Unlink__, elimina una entrada de directorio. Si el archivo que se desvincula solo está presente en un directorio (el caso normal), se elimina del sistema de archivos. Si está presente en varios directorios, solo se elimina el nombre de ruta especificado. 

## Rutas

Cuando el sistema de archivos está organizado en estructuras de directorios, se necesita alguna forma para especificar los nombres de los archivos. Normalmente se utilizan dos métodos diferentes: ruta absoluta y ruta relativa.

En el método de __ruta absoluta__, a cada archivo se le asigna un nombre de ruta absoluto que consiste en la ruta desde el directorio raíz hasta el archivo. Como ejemplo,

```plain
\Users\Public\Documents
```

significa que el directorio raíz contiene un subdirectorio `Users`, que a su vez contiene un subdirectorio `Public`, que contiene `Documents`. Los nombres de ruta absolutos siempre comienzan en el directorio raíz y son únicos. En sistemas UNIX, los componentes de la ruta están separados por `/`, en Windows, el separador es `\`.

El otro métodos, es el de __ruta relativa__. Esto se usa junto con el concepto de  "directorio actual". Un usuario puede designar un directorio como el directorio de trabajo actual, en cuyo caso todos los nombres de ruta que no comienzan en el directorio raíz se consideraran en relación con el directorio de trabajo. Por ejemplo, si el directorio de trabajo actual es,

```plain
\Users\Public
```

entonces, el archivo cuya ruta absoluta es `\Users\Public\Documents` puede ser referenciado simplemente como `Documents`.

La mayoría de los {term}`OS` que admiten un sistema de directorio jerárquico tienen dos entradas especiales en cada directorio, `.` y `..`, que generalmente se pronuncian punto y punto punto, respectivamente. El punto se refiere al directorio actual; el punto punto se refiere a su padre (excepto en el directorio raíz, donde se refiere a sí mismo). Por ejemplo, considere la lista de directorios de Windows de la {numref}`fig-rutas-win`, si un proceso tiene `\Users\Public` como directorio de trabajo, puede usar `..` para referirse al un nivel más alto en la estructura de directorios, en este caso al nivel `\Users`.


```{figure} ../images/rutas-windows.png
:width: 600px
:name: fig-rutas-win

Ejemplo de lista de directorios en Windows.
```

## Estructura de un nivel

La estructura de directorio más simple es el directorio de un solo nivel. Todos los archivos están contenidos en el mismo directorio, lo que es fácil de apoyar y entender. Tiene limitaciones importantes cuando el número de archivos aumenta o cuando el sistema tiene más de un usuario. Dado que todos los archivos están en el mismo directorio, deben tener nombres únicos, de los contrario, se viola la regla del nombre único. Afortunadamente, la mayoría de los sistemas de archivos admiten nombres de archivos de hasta 255 caracteres, por lo que es relativamente fácil seleccionar nombres de archivos únicos.

## Estructura de dos niveles

En una estructura de directorios de dos niveles, cada usuario tiene su propio _user file directory_ ({term}`UFD`). Estos directorios, tienen estructuras similares, pero cada uno enumera sólo los archivos de un único usuario.

```{figure} ../images/two-level-dir.png
:width: 600px
:name: fig-dir-dos-niveles

Estructura de directorios de dos niveles.
```

Cuando se inicia un trabajo de usuario, se busca en el _master file directory_ ({term}`MFD`) del sistema. El {term}`MFD` se indexa por nombre de usuario, y cada entrada apunta al UFD para ese usuario. Esta estructura aísla efectivamente a un usuario de otro. Algunos sistemas simplemente no permiten que otros usuarios accedan a los archivos locales de otro usuario. Para que se permita el acceso, un usuario debe tener la capacidad de nombrar un archivo en el directorio de otro usuario. Para nombrar un archivo en particular de manera única en un directorio de dos niveles, debemos dar tanto el nombre de usuario como el nombre del archivo.

Un directorio de dos niveles puede considerarse como un árbol invertido, de altura 2. La raíz del árbol (_root_) es el {term}`MFD`. Sus directorios descendientes directos son los {term}`MFD`s. Los descendientes de los {term}`UFD`s son los propios archivos. La especificación de un nombre de usuario y un nombre de archivo define una ruta en el árbol desde la raíz (el {term}`MFD`) hasta una el archivo especificado. Así, un nombre de usuario y un nombre de archivo definen un nombre de ruta. Cada archivo del sistema tiene un nombre de ruta (_path_). Para nombrar un archivo de manera única, el usuario debe conocer el nombre de la ruta del archivo.

Por ejemplo, si la usuaria A desea acceder a su propio archivo de pruebas llamado `prueba.txt`, puede simplemente referirse a `prueba.txt`. Sin embargo, para acceder al archivo llamado `prueba.txt` del usuario B, puede que tenga que referirse a `\userb\prueba.txt`. Cada sistema tiene su propia sintaxis para nombrar los archivos en directorios distintos del del usuario.

Adicionalmente, se necesita una sintaxis adicional para especificar el volumen de un archivo. Por ejemplo, en Windows se especifica con una letra seguida de dos puntos. Por lo tanto, una especificación de archivo podría ser,

```
C:\userb\prueba.txt
```

Otros sistemas, como UNIX y Linux, simplemente tratan el nombre del volumen como parte del nombre del directorio. El primer nombre que se da es el del volumen, y el resto es el directorio y el archivo. Por ejemplo, la siguiente dirección,

```
/u/pbg/prueba.txt
```

podría especificar el volumen `u`, el directorio `pbg`, y el archivo `prueba.txt`.

## Estructura de árbol


La generalización de extender la estructura del directorio a un árbol de altura arbitraria, permite a los usuarios crear sus propios subdirectorios y organizar sus archivos. Un árbol es la estructura de directorios más común. El árbol tiene un directorio raíz, y cada archivo del sistema tiene un nombre de ruta único.

Un directorio (o subdirectorio) contiene un conjunto de archivos o subdi- rectorios. Un directorio es simplemente otro archivo, pero se trata de manera especial. Todos los directorios tienen el mismo formato interno. Un bit en cada entrada del directorio define la entrada como un archivo (0) o como un subdirectorio (1). Se utilizan llamadas especiales del sistema para crear y borrar directorios.

En el uso normal, cada proceso tiene un directorio actual. El directorio actual debe contener la mayoría de los archivos que son de interés actual para el proceso. Cuando se hace referencia a un archivo, se busca en el directorio actual. Si se necesita un archivo que no está en el directorio actual, entonces el usuario normalmente debe o bien especificar un nombre de ruta o cambiar el directorio actual para que sea el directorio que contiene ese archivo. Para cambiar de directorio, se proporciona una llamada al sistema que toma un nombre de directorio como parámetro y lo utiliza para redefinir el directorio actual. De esta manera, el usuario puede cambiar su directorio actual cuando lo desee. Todas las llamadas de sistema de apertura de archivo buscan en el directorio actual el archivo especificado.

El directorio actual inicial en el _shell_ de un usuario se designa cuando se inicia el trabajo del usuario. El directorio actual de cualquier subproceso suele ser el directorio actual del padre cuando fue originado el subproceso.

```{figure} ../images/tree-level-dir.png
:width: 600px
:name: fig-arbol-directorios

Estructura de árbol de directorios.
```

Los nombres de las rutas (_path_) pueden ser de dos tipos: absolutos y relativos. Un nombre de ruta absoluto comienza en la raíz y sigue una ruta hasta el archivo especificado, dando los nombres de los directorios en la ruta. Un nombre de ruta relativo define una ruta desde el directorio actual. Por ejemplo, en el sistema de archivos estructurados en árbol de la {numref}`fig-arbol-directorios`, si el directorio actual es `root/spell/mail`, entonces el nombre de ruta relativo exp/list se refiere al mismo archivo que el nombre de ruta absoluto `root/spell/mail/exp/list`.

Permitir que un usuario defina sus propios subdirectorios le permite imponer una estructura a sus archivos. Esta estructura puede dar lugar a directorios separados para los archivos asociados a diferentes contenidos o diferentes formas de información.

## Estructura de grafo acíclico

Una estructura de árbol prohíbe compartir archivos o directorios. Un grafo acíclico permite que los directorios compartan subdirectorios y archivos ({numref}`fig-grafo-aciclico`). El mismo archivo o subdirectorio puede estar en dos directorios diferentes. El grafo acíclico es una generalización natural del esquema de directorios estructurados en árbol.

```{figure} ../images/acyclic-graph.png
:width: 600px
:name: fig-grafo-aciclico

Estructura de grafo acíclico.
```

Es importante señalar que un archivo (o directorio) compartido no es lo mismo que dos copias del archivo. Con dos copias, cada usuario puede ver una copia en lugar del original, pero si un usuario cambia el archivo, los cambios no aparecerán en la copia del otro. Con un archivo compartido, sólo existe un archivo real, por lo que cualquier cambio realizado por un usuario es inmediatamente visible para la otra. Compartir es particularmente importante para los subdirectorios; un nuevo archivo creado por un usuario aparecerá automáticamente en todos los subdirectorios compartidos.

Los archivos y subdirectorios compartidos pueden implementarse de varias maneras. Una forma común, ejemplificada por muchos de los sistemas UNIX, es crear una nueva entrada de directorio llamada enlace. Un enlace es efectivamente un puntero a otro archivo o subdirectorio. Por ejemplo, un enlace puede implementarse como un nombre de ruta absoluto o relativo.

Otro enfoque común para implementar archivos compartidos es simple- mente duplicar toda la información sobre ellos en ambos directorios compartidos. Un problema importante de las entradas de directorio duplicadas es mantener la coherencia cuando se modifica un archivo.

Una estructura de grafo acíclica es más flexible que una simple estructura de árbol, pero también es más compleja. Uno de los problemas es el de la eliminación de archivos. Una posibilidad es eliminar el archivo cada vez que alguien lo borre, pero esta acción puede dejar punteros colgantes al archivo ahora inexistente. Peor aún, si los punteros del archivo restante contienen direcciones reales del disco, y el espacio se reutiliza posteriormente para otros archivos, estos punteros colgantes pueden apuntar hacia otros archivos.

En un sistema en el que compartir archivos se realiza mediante enlaces simbólicos ({numref}`fig-enlace-simbolico`), la eliminación de un enlace no tiene por qué afectar al archivo original; sólo se elimina el enlace. Si se borra la entrada del archivo en sí, el espacio para el archivo se deslocaliza, dejando los enlaces colgando. Podemos buscar estos enlaces y eliminarlos también, pero a menos que se mantenga una lista de los enlaces asociados con cada archivo, esta búsqueda puede ser costosa. Alternativamente, podemos dejar los enlaces hasta que se intente usarlos. En ese momento, podemos determinar que el archivo del nombre dado por el enlace no existe y puede fallar en la resolución del nombre del enlace; el acceso se trata como con cualquier otro nombre de archivo ilegal. En el caso de UNIX, los enlaces simbólicos se mantienen cuando se elimina un archivo, y depende del usuario darse cuenta de que el archivo original ha desaparecido o ha sido reemplazado. Microsoft Windows utiliza el mismo enfoque.

```{figure} ../images/enlace-simbolico.png
:height: 500px
:name: fig-enlace-simbolico

Enlace simbólico en Microsoft Windows.
```

Otro enfoque para la eliminación es preservar el archivo hasta que se eli- minen todas las referencias a él. Para aplicar este enfoque, se debe disponer de algún mecanismo para determinar que se ha suprimido la última referencia al fichero. Cuando se elimina un enlace o una entrada de directorio, se elimina su entrada en la lista. El archivo se elimina cuando su lista de referencia de archivos está vacía.

Para evitar problemas como los que se acaban de exponer, algunos sistemas simplemente no permiten directorios o enlaces compartidos.

## Montaje del sistema de archivos

Al igual que un archivo debe abrirse antes de ser utilizado, un sistema de archivos debe montarse antes de que pueda estar disponible para los procesos en el sistema. Más concretamente, la estructura de directorios puede estar construida a partir de múltiples volúmenes, que deben montarse para que estén disponibles dentro del espacio de nombres del sistema de archivos. 

El procedimiento de montaje es sencillo. Se le da al sistema operativo el nombre del dispositivo y el punto de montaje, es decir, la ubicación dentro de la estructura de archivos en la que se debe montar el sistema de archivos. Algunos sistemas operativos requieren que se proporcione un tipo de sistema de archivos, mientras que otros inspeccionan las estructuras del dispositivo y determinan el tipo de sistema de archivos. Normalmente, un punto de montaje es un directorio vacío.

A continuación, el {term}`OS` verifica que el dispositivo contiene un sistema de archivos válido. Lo hace pidiendo al controlador del dispositivo que lea el directorio del dispositivo y verificando que el directorio tiene el formato esperado. Finalmente, el sistema operativo anota en su estructura de directorios que un sistema de archivos está montado en el punto de montaje especificado. Este esquema permite al sistema operativo recorrer su estructu- ra de directorios, cambiando entre sistemas de archivos, e incluso sistemas de archivos de diversos tipos, según proceda.

Considere las acciones del {term}`OS` de macOS X. Siempre que el sistema se encuentra con un disco por primera vez (ya sea en el momento del arranque o mientras el sistema está funcionando), el {term}`OS` busca un sistema de archivos en el dispositivo. Si lo encuentra, monta automáticamente el sistema de archivos en el directorio `/Volumes`, añadiendo un icono de carpeta etiquetado con el nombre del sistema de archivos (tal y como está almacenado en el directorio del dispositivo). El usuario puede entonces hacer clic en el icono y así mostrar el nuevo sistema de archivos montado.

```{figure} ../images/administrador-discos.png
:height: 400px
:name: fig-administrador-discos

Herramienta administrativa de discos de Windows 10.
```

La familia de {term}`OS`s de Microsoft Windows mantiene una estructura de directorios ampliada de dos niveles, con letras de unidad asignadas a dispositivos y volúmenes ({numref}`fig-administrador-discos`). Los volúmenes tienen una estructura de directorios gráfica general asociada con la letra de unidad. Como por ejemplo, la ruta `C:\Users\Public>` identificada en el prompt de la {numref}`fig-rutas-win`, hace referencia al disco duro local como la unidad `C:`.

## Bibliografia

```{bibliography} ../refs.bib   
:style: plain
:filter: docname in docnames
```