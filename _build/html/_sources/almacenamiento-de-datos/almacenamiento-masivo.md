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

# Almacenamiento masivo

Debido a la volatilidad y al tamaño limitado de la memoria principal, la mayoría de los computadores incluyen dispositivos de memoria adicionales llamados sistemas de almacenamiento masivo (o almacenamiento secundario). Entre estos, se incluyen discos magnéticos, {term}`CD`, {term}`DVD`, unidades flash y {term}`SSD`. Las ventajas de los sistemas de almacenamiento masivo sobre la memoria principal, es que incluyen menos volatilidad, poseen grandes capacidades de almacenamiento, son de bajo costo, entre otros.

Una desventaja importante de los sistemas de almacenamiento masivo óptico y magnético es que generalmente requieren de movimientos mecánicos y, por lo tanto, requieren mucho más tiempo para almacenar y recuperar datos que la memoria principal, mientras que en esta última todas las actividades se realizan electrónicamente. Además, los sistemas de almacenamiento con partes móviles son propensos a fallas mecánicas.

## Sistemas magnéticos

Durante años la tecnología magnética ha dominado el campo del almacenamiento masivo. El ejemplo más común es el {term}`HDD`, habitualmente denominado disco duro. Aunque los {term}`HDD` dominan el volumen de almacenamiento producido por los servidores, los ingresos por ventas vienen disminuyendo frente al creciente uso de {term}`SSD` {cite}`oreilly_why_2017`. Estos últimos proporcionan mayores tasas de transferencia de datos, mayor densidad de almacenamiento de área, mayor confiabilidad {cite}`mielke_reliability_2017`, y bajos tiempos de latencia y acceso.

```{figure} ../images/hdd-external.png
:name: fig-disco-duro
:figclass: margin
     
Componentes físicos de un disco duro.
```

Un {term}`HDD` típico ({numref}`fig-disco-duro`) consiste en un eje que contiene discos circulares planos, hechos de un material no magnético (e.g., aleación de aluminio, vidrio, cerámica). Están recubiertos con una capa poco profunda de material magnético, con una capa externa de carbono para su protección. Tienen dos motores eléctricos: un motor que hace girar los discos y un actuador que sitúa el cabezal de lectura/escritura en los discos giratorios. Frente al actuador en el extremo del brazo está el cabezal de lectura/escritura. Los cables delgados de circuito conectan los cabezales de lectura/escritura a los componentes electrónicos del amplificador montado en el pivote del actuador. Los discos contemporáneos giran a velocidades que varían desde 4200 {term}`RPM` en dispositivos portátiles de bajo consumo de energía, hasta 15000 {term}`RPM` para servidores de alto rendimiento, sin embargo, la mayoría de los {term}`HDD` de consumo masivo giran entre 5400 a 7200 {term}`RPM`.

Los {term}`HDD` modernos son su tamaño de 3.5 pulgadas, para computadores de escritorio, y 2.5 pulgadas, principalmente para notebook. Las interfaces de conexión se establecen mediante cables de estándar, tales como, {term}`PATA`, {term}`SATA`, {term}`USB` o {term}`SAS`.

Para la organización y almacenamiento de la información de una unidad de disco, cada disco se divide en _tracks_, los cuales forman círculos completos en cada disco, que se dividen a su vez en un número igual de _sectors_ (ver {numref}`fig-disco-magnetico`).

```{figure} ../images/hdd-internal.png
:name: fig-disco-magnetico
:figclass: margin
     
Sistema de almacenamiento de la información de un disco magnético.
```

- **_Track_**, círculos concéntricos, conocidos como _tracks_. Toda la información almacenada en el disco duro se graba en _tracks_. Comenzando desde cero en el lado externo del disco, el número de _tracks_ continúa aumentando hacia el lado interno.
- **_Cylinder_**, conjunto de _tracks_ alineados verticalmente sobre cada del los discos.
- **_Sector_**. Cada _track_ se divide en unidades más pequeñas llamadas _sectors_. Este es la unidad básica de almacenamiento de datos en un disco duro (e.g., 512 _bytes_).
- **_Cluster_**, agrupación de _sectors_.

Los cabezales de lectura/escritura se sitúan arriba y/o debajo del disco de modo que a medida que el disco gira, cada cabezal atraviesa un _track_. Cada _track_ se divide en pequeños arcos llamados _sectors_ en los que la información se registra como una cadena continua de _bits_. Al reposicionar los cabezales de lectura/escritura, se puede acceder a diferentes _tracks_. En muchos casos, un sistema de almacenamiento en disco consta de varios discos montados en un eje común, uno encima del otro, con espacio suficiente para que los cabezales de lectura/escritura se deslicen entre los platos. En tales casos, los cabezales de lectura/escritura se mueven al unísono. Cada vez que se vuelven a situar los cabezales de lectura/escritura, se vuelve accesible un _cylinder_. 

Independientemente de los detalles, un sistema de almacenamiento en disco consta de muchos sectores individuales, a cada uno de los cuales se puede acceder como una cadena de _bits_ independiente.

El rendimiento de un {term}`HDD` está relacionados principalmente con la naturaleza mecánica de los discos giratorios y los cabezales móviles, que incluye el tiempo de búsqueda, tiempo de latencia, tiempo de acceso y velocidad de transferencia.

- El __tiempo de búsqueda__ es medida del tiempo que tiempo requerido para mover los cabezales de lectura/escritura de un _track_ a otro.
- El __tiempo de latencia__ es la mitad del tiempo requerido para que el disco haga una rotación completa, que es la cantidad de tiempo promedio requerida para que los datos (_sectors_) deseados giren hacia el cabezal de lectura/escritura una vez que el cabezal ha sido situado sobre el _track_ requerido.
- El __tiempo de acceso__ es la suma del tiempo de búsqueda y el retraso de la rotación (tiempo de latencia).
- La __tasa de transferencia__ corresponde a la velocidad a la que se pueden transferir datos hacia o desde el disco. Es decir, una vez que el cabezal está en la posición correcta, el retraso que depende del número de bloques transferidos.

El tiempo de acceso a los datos puede mejorar aumentando la velocidad de rotación (reduciendo la latencia) o reduciendo el tiempo dedicado a la búsqueda.

```{figure} ../images/disquete.png
:name: fig-disquete
:figclass: margin

Disquete de 3.5 pulgadas.
```

Otras tecnologías de almacenamiento magnético que hoy son menos utilizadas incluyen la cinta magnética, en la que la información se registra en el revestimiento magnético de una cinta de plástico delgada enrollada en carretes, y las unidades de disquete, en las que se colocan discos ({numref}`fig-disquete`) individuales con un revestimiento magnético en un cartucho portátil diseñado para extraerse (portabilidad) fácilmente de la unidad _floppy drive_ ({numref}`fig-disquetera`).  

```{figure} ../images/disquetera.png
:name: fig-disquetera
:figclass: margin

Disquetera (_floppy drive_).
```

## Sistemas ópticos

El {term}`CD` es un ejemplo de tecnología óptica aplicada al almacenamiento masivo. Originalmente, fue aplicada a las grabaciones de audio utilizando un formato de grabación conocido como {term}`CD-DA`, que al igual que los {term}`CD` usados para el almacenamiento de datos utilizan el mismo formato. 

Los discos tienen 12 centímetros (5 pulgadas aprox.) de diámetro y consisten en material reflectante cubierto con una capa protectora transparente. La información se registra en ellos creando variaciones en sus superficies reflectantes. Esta información se puede recuperar por medio de un láser que detecta irregularidades en la superficie reflectante del {term}`CD` a medida que gira.

La información se almacena en una sola pista que gira en espiral alrededor del {term}`CD`, de adentro hacia afuera y en sentido de las manecillas del reloj ({numref}`fig-cd`). Esta pista se divide en unidades llamadas sectores, cada uno con sus propias marcas de identificación y una capacidad de 2 KB de datos, lo que equivale a 1/75 segundos de música en el caso de grabaciones de audio. {cite}`stan_cd-rom_1998`

```{figure} ../images/cd.png
:name: fig-cd
:figclass: margin

Formato de almacenamiento en un {term}`CD`.
```

Considerando que la distancia alrededor de la pista en espiral es mayor hacia el borde exterior del disco que en la parte interior, se almacena más información en un bucle alrededor de la porción externa de la espiral que en un bucle alrededor de la porción interna. A su vez, se leerán más sectores en una sola revolución del disco cuando el láser esté escaneando la parte externa de la pista en espiral que cuando el láser esté escaneando la parte interna de la pista. Por lo tanto, para obtener una velocidad uniforme de transferencia de datos, los reproductores de {term}`CD-DA` están diseñados para variar la velocidad de rotación dependiendo de la ubicación del láser. Sin embargo, la mayoría de los sistemas de {term}`CD` utilizados para el almacenamiento de datos giran a una velocidad más rápida y constante y, por lo tanto, deben adaptarse a las variaciones en las velocidades de transferencia de datos.

Como consecuencia del diseño, los sistemas de almacenamiento {term}`CD` operan mejor cuando se manejan cadenas de datos largas y continuas, como cuando se reproduce música. Por el contrario, cuando una aplicación requiere acceso a elementos de datos de manera aleatoria, el enfoque utilizado en el almacenamiento en disco magnético (pistas individuales y céntricas divididas en sectores accesibles individualmente) supera al enfoque en espiral utilizado en los {term}`CD`.

Las unidades ópticas son dispositivos que pueden leer y escribir datos en discos ópticos {cite}`von_guide_2019`. Existen diferencias entre los distintos formatos. Por ejemplo, un {term}`CD` típico tienen capacidades entre 600 a 700 MB. Por otra parte, los {term}`DVD`, que están construidos a partir de múltiples capas semitransparentes que sirven como superficies distintas cuando son enfocadas con un láser (color rojo), proporcionan capacidades de almacenamiento de varios GB. Finalmente, la tecnología Blu-ray, que utiliza un láser en el espectro de luz azul-violeta, puede enfocar su rayo láser con una precisión muy fina. Como resultado, los discos Blu-ray proporcionan más de cinco veces la capacidad de un {term}`DVD`.

## Unidades flash

Una característica común de los sistemas de almacenamiento masivo basados en tecnología magnética u óptica es que requieren movimientos mecánicos para almacenar y recuperar datos, lo cual es lento en comparación con la velocidad de los circuitos electrónicos. La tecnología de memoria _flash_ tiene el potencial de aliviar este inconveniente. En un sistema de memoria flash, los _bits_ se almacenan enviando señales electrónicas directamente al medio de almacenamiento donde hacen que los electrones queden atrapados en pequeñas cámaras de dióxido de silicio, alterando así las características de los pequeños circuitos electrónicos. Dado que estas cámaras pueden mantener sus electrones cautivos durante muchos años sin alimentación externa.

```{figure} ../images/pendrive.png
:name: fig-pendrive
:figclass: margin

Unidad(pendrive).
```

Aunque se puede acceder a los datos almacenados en los sistemas de memoriaen pequeñas unidades de tamaño de byte como en las aplicaciones {term}`RAM`, el borrado repetido daña lentamente las cámaras de dióxido de silicio, lo que significa que la tecnología actual de memoriano es adecuada para aplicaciones generales de memoria principal en las que su contenido puede verse alterado muchas veces por segundo. Sin embargo, en aquellas aplicaciones en las que las alteraciones pueden controlarse a un nivel razonable, como en cámaras digitales y teléfonos inteligentes, la memoriase ha convertido una tecnología de almacenamiento masivo.

```{figure} ../images/ssd-componentes.png
:name: fig-ssd
:figclass: margin

Componentes de un {term}`SSD`.
```

Los dispositivos de memoria (unidades _flash_), están disponibles para aplicaciones generales de almacenamiento masivo con capacidades de cientos de GB. Algunas de estas unidadesse empaquetan en cajas de plástico cada vez más pequeñas con una tapa extraíble en un extremo para proteger el conector eléctrico de la unidad cuando se encuentra desconectada ({numref}`fig-pendrive`). La alta capacidad de estas unidades portátiles, así como el hecho de que se conectan y desconectan fácilmente de una computadora, las hace ideales para el almacenamiento portátil de datos.

Memoriasde mayor capacidad son los llamados {term}`SSD`, diseñados explícitamente para reemplazar los {term}`HDD`. Los {term}`SSD` se comparan favorablemente con los discos duros en su resistencia a las vibraciones y golpes físicos, su funcionamiento silencioso (debido a la ausencia de piezas móviles) y sus tiempos de acceso más bajos. Los {term}`SSD` siguen siendo más costoso que los discos duros de capacidad comparable y, por lo tanto, todavía se consideran una opción de gama alta al comprar un computador. Los sectores {term}`SSD` sufren una vida útil más limitada de todas las tecnologías de memoria _flash_ , pero el uso de técnicas de nivelación de desgaste puede reducir el impacto de esto al reubicar bloques de datos frecuentemente modificados en ubicaciones nuevas en el disco.

Un {term}`SSD` (ver {numref}`fig-ssd`) no contiene muchas partes únicas y la diferenciación de ellos entre los diferentes fabricantes a menudo ocurre en el controlador y el _firmware_. A continuación se presenta una breve descripción los componentes principales de un {term}`SSD` {cite}`noauthor_ssd_2010`.

```{note}
_Firmware_ es una tipo específico de _software_ que proporciona el control de bajo nivel para el _hardware_ específico de un dispositivo. Puede proporcionar un entorno operativo estandarizado para un software de dispositivo o actuar como el sistema operativo completo del dispositivo, realizando todas las funciones de control, monitoreo y manipulación de datos.
```

- Controlador del dispositivo, es el _software_ creado por el {term}`OEM` para ejecutarse en la familia de procesadores _host_ de destino en un sistema operativo y sistema de archivos en particular. El controlador del dispositivo proporciona acceso desde el _host_ al producto {term}`SSD`.
- Interfaz eléctrica entre el procesador _host_ y el dispositivo periférico {term}`SSD` , e.g., {term}`SATA`, {term}`USB`, {term}`IDE`.
- Controlador {term}`SSD` , componentes electrónicos que proporcionan interfaz de nivel de dispositivo {term}`SSD` y ejecución de _firmware_. Se incluye un procesador integrado, {term}`ROM` de datos, {term}`RAM` de datos, interfaz de componentes _flash_ , código de corrección de errores, nivelación de desgaste y características de seguridad.
- Componentes de memoria flash, dispositivosindividuales que utilizan tecnología NAND o NOR. Las densidades varían entre 2 GB y 64 GB.
- Componentes de memoria intermedia o caché, componente de memoria {term}`RAM` de alta velocidad utilizados para la coincidencia de velocidad y para aumentar el rendimiento de datos.
- Controlador _firmware_, _software_ escrito y almacenado en memoria para su ejecución por el controlador.

```{figure} ../images/flash-sd.png
:name: fig-sd
:height: 100px
:figclass: margin

Mini y micro {term}`SD`.
```

```{figure} ../images/flash-sdhc.png
:name: fig-sd-sdhc
:height: 100px
:figclass: margin

Secure Digital High Capacity ({term}`SDHC`).
```

```{figure} ../images/flash-sdxc.png
:name: fig-sd-sdxc
:height: 100px
:figclass: margin

Secure Digital Extended Capacity ({term}`SDXC`).
```

Otra aplicación de la tecnologíase encuentra en las tarjetas de memoria {term}`SD`. Estos proporcionan hasta 2 GB de almacenamiento y están empaquetados en plástico con el tamaño aproximado de una estampilla, también se encuentran disponibles en tamaños mini y micro {term}`SD`. Las tarjetas de memoria {term}`SDHC` pueden proporcionar hasta 32 GB y la tarjetas de memoria {term}`SDXC` puede superar 1 TB. Dado su tamaño físico compacto, estas tarjetas se deslizan convenientemente en ranuras de pequeños dispositivos electrónicos. En general, son usados en cámaras digitales, _smartphones_, GPS, entre otros dispositivos electrónicos.

## Bibliografia

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```