# Organización de un computador

Como ocurre con cualquier sistema complejo, un computador puede ser visto desde diferentes perspectivas {cite}`murdocca_principles_1999`, desde el nivel más alto de usuario hasta el nivel más bajo de transistores (ver {numref}`fig-perspectivas-pc`). Cada uno de estos niveles representa una abstracción del computador, los cuales son independientes entre sí. Por ejemplo, un usuario que ejecuta un programa de procesamiento de texto en una computador no necesita saber nada sobre la programación de este _software_. Asimismo, un programador, que requiere tratar con aspectos tales como el tamaño de los tipos de datos (por ejemplo, usar 16 dígitos binarios para representar un número entero) y los tipos de operaciones que son compatibles (como sumar, restar y llamar a subrutinas), no necesita preocuparse por la estructura de la puerta lógica dentro de la computadora.

```{figure} ../images/perspectivas-arquitectura-pc.png
:height: 180px
:align: center
:name: fig-perspectivas-pc

Perspectivas de un computador.
```

La organización de un computador se ocupa de las relaciones estructurales, como las interfaces con los dispositivos periféricos, la frecuencia del reloj y la tecnología utilizada por la memoria.

## El modelo de von Neumann

Los computadores convencionales tienen una forma común que se atribuye a [John von Neumann](https://www.biografiasyvidas.com/biografia/n/neumann.htm) {cite}`m_ruiza_biografia_2004`, este modelo consta de cinco componentes principales ({numref}`fig-vonneumann`). La Unidad de Entrada proporciona instrucciones y datos al sistema, que posteriormente se almacenan en la Unidad de Memoria. Las instrucciones y los datos son procesados por la Unidad Aritmético-Lógica ({term}`ALU` - _Arithmetic/Logic Unit_) bajo la dirección de la Unidad de Control. Los resultados se envían a la Unidad de Salida.

```{figure} ../images/von_neumann.png
:height: 300px
:align: center
:name: fig-vonneumann

Modelo de computador de von Neumann.
```

El concepto de programa almacenado es el aspecto más importante del modelo de von Neumann. Un programa se almacena en la memoria del computador junto con los datos que se procesarán. Aunque hoy es común, antes de este concepto, los programas de computadores se almacenaban en medios externos, como placas de conexión, tarjetas perforadas o cintas. En el computador de programa almacenado, el programa se puede manipular como si fueran datos. Esto dio lugar a compiladores y sistemas operativos, y hace posible la gran versatilidad del computador moderno.

## Computador típico

Los computadores modernos han evolucionado desde las gigantes máquinas de las décadas de 1950 y 1960 hasta las computadoras mucho más pequeñas y poderosas de hoy.

```{note}
Puedes revisar la [línea de tiempo de la historia de la computación](https://www.computerhistory.org/timeline/computers/).
```

La {numref}`fig-laptop` muestra una configuración típica de un computador de sobremesa o notebook. La unidad de entrada está compuesta por el teclado y el touchpad, a través de los cual el usuario ingresa datos, instrucción y/o comandos. La pantalla y los altavoces corresponden a unidades de salida, que representan las salidas de forma visual y auditiva, respectivamente. La {term}`ALU` y la Unidad de Control están agrupadas en el procesador, el que esta incluido en la placa base. La unidad de memoria consta de circuitos de memoria individuales ({term}`RAM`), como también, de una unidad de almacenamiento secundarios ({term}`SSD`).

```{figure} ../images/laptop-partes.png
:height: 560px
:align: center
:name: fig-laptop

Configuración típica de un notebook.
```

La placa base, denominada tarjeta madre o _motherboard_, se enceuentra al interior de los notebooks, como también dentro de cualquiera de la mayoría de los computadores que nos rodea. Esta placa contiene circuitos integrados, ranuras para tarjetas de expansión y los cables que interconectan los circuitos integrados y las ranuras para tarjetas de expansión.


## La CPU

La unidad central de procesamiento ({term}`CPU` - _Central Processing Unit_), comunmente denominada procesador, es el conjunto de circuitos de un computador que controla la manipulación de los datos. Este componente se encuentra empaquetado como pequeños cuadrados planos (de 2 pulgadas apróximadamente) cuyas clavijas de conexión se conectan a un zócalo montado en la placa base. En _smartphones_, _tablets_ y otros dispositivos móviles, la {term}`CPU` tienen aproximadamente la mitad del tamaño de una estampilla y, debido a su pequeño tamaño, estos procesadores se denominan microprocesadores

La {term}`CPU` se compone de tres partes ({numref}`fig-cpu`): la {term}`ALU`, que contiene los circuitos que realizan operaciones con datos (como sumas y restas); la unidad de control, que contiene los circuitos para coordinar las actividades de la máquina; y la unidad de registro, que contiene celdas para el almacenamiento de datos (similares a las celdas de memoria principal), llamadas registros, que se utilizan para el almacenamiento temporal de información dentro de la {term}`CPU`. Algunos de estos registros se consideran de propósito general, mientras que otros, son de propósito especial.

```{figure} ../images/cpu.png
:height: 160px
:align: center
:name: fig-cpu

Partes de una {term}`CPU`. {cite}`brookshear_computer_2015`
```

Los registros de propósito general se utilizan para el almacenamiento temporal de los datos que manipula la {term}`CPU`. Estos registros contienen las entradas a los circuitos de la {term}`ALU` y proporcionan espacio de almacenamiento para los resultados generados por esta unidad. Para realizar una operación sobre los datos almacenados en la memoria principal, la unidad de control transfiere los datos de la memoria a los registros de propósito general, informa a la {term}`ALU` que contiene los datos, activa el circuito apropiado dentro de la {term}`ALU` y le indica el registro que debe recibir el resultado.

Con el propósito de transferir patrones de _bits_, la {term}`CPU` y la memoria principal de una máquina están conectadas por una colección de cables llamada bus ({numref}`fig-cpu`). A través de este Bus, la {term}`CPU` lee datos de la memoria principal proporcionando la dirección de la celda de memoria pertinente junto con una señal electrónica que le señala al circuito de memoria que se supone que debe recuperar los datos en la celda indicada. De manera similar, la {term}`CPU` escribe datos en la memoria proporcionando la dirección de la celda de destino y los datos que se almacenarán junto con la señal electrónica apropiada que le indica a la memoria principal que se supone que debe almacenar los datos que se le envían.

Con base en este diseño, por ejemplo, la tarea de sumar dos valores almacenados en memoria principal implica más que la mera ejecución de la operación de suma. Los datos deben transferirse desde la memoria principal a los registros dentro de la {term}`CPU`, los valores deben sumarse y el resultado debe almacenarse en un registro, y luego el resultado debe transferirse hacia una celda de memoria.

Los registros de propósito especial de la {term}`CPU` son utilizados en el proceso de [ejecución de un programa](content:ejecucion-de-un-programa).

## Comunicación entre componentes

La {numref}`fig-bus` muestra el modelo de bus de un sistema informático. Aquí, el sistema informático es divido en tres unidades: {term}`CPU`, memoria y entrada/salida (E/S).

```{figure} ../images/sistema-bus.png
:height: 230px
:align: center
:name: fig-bus

Modelo del sistema de bus de un computador. {cite}`murdocca_principles_1999`
```

Para el modelo de bus del sistema, las comunicaciones entre los componentes son por medio de una vía compartida, que está compuesta por el bus de datos (que lleva la información que se transmite), el bus de direcciones (que identifica dónde se envía la información) y el bus de control (que describe aspectos de cómo se envía la información y de qué manera). También hay un bus de potencia para la alimentación eléctrica de los componentes, que no se muestra, pero se entiende su presencia.

Físicamente, los buses están formados por conjuntos de cables agrupados por función. Un bus de datos de 32 _bits_ tiene 32 cables individuales, cada uno de los cuales transporta un bit de datos (a diferencia de la dirección o la información de control). En este sentido, el bus del sistema es en realidad un grupo de buses individuales clasificados por su función.

El bus de datos mueve datos entre los componentes del sistema. Algunos sistemas tienen buses de datos separados para mover información hacia y desde la {term}`CPU`, en cuyo caso hay un bus de entrada de datos y un bus de salida de datos. Habitualmente, un bus de datos solo mueve datos en cualquier dirección, aunque nunca en ambas direcciones al mismo tiempo.

Si el bus se va a compartir entre entidades que se comunican, las entidades deben tener identidades distinguidas: direcciones. En algunos computadores, se asume que todas las direcciones son direcciones de memoria, ya sea que que formen parte de la memoria de la computadora o que sean dispositivos de E/S, mientras que en otros, los dispositivos de E/S tienen direcciones de E/S separadas.

Una dirección de memoria, o ubicación, identifica una ubicación de memoria donde se almacenan los datos, de manera similar a la forma en que una dirección postal identifica la ubicación donde un destinatario recibe y envía correo. Durante una operación de lectura/escritura de la memoria, el bus de direcciones contiene la dirección de la ubicación de la memoria donde se leerán/escribirán los datos.

El bus de control se puede pensar como un coordinandor del acceso al bus de datos y al bus de direcciones, y dirigiendo los datos a componentes específicos.

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```
