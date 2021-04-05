# Unidad Central de Procesamiento

La unidad central de procesamiento ({term}`CPU` - _Central Processing Unit_), comunmente denominada procesador, es el conjunto de circuitos de un computador que controla la manipulación de los datos. Este componente se encuentra empaquetado como pequeños cuadrados planos (de 2 pulgadas apróximadamente) cuyas clavijas de conexión se conectan a un zócalo montado en la placa base. En _smartphones_, _tablets_ y otros dispositivos móviles, la {term}`CPU` tienen aproximadamente la mitad del tamaño de una estampilla y, debido a su pequeño tamaño, estos procesadores se denominan microprocesadores

La {term}`CPU` se compone de tres partes ({numref}`fig-cpu`): la {term}`ALU`, que contiene los circuitos que realizan operaciones con datos (como sumas y restas); la unidad de control, que contiene los circuitos para coordinar las actividades de la máquina; y la unidad de registro, que contiene celdas para el almacenamiento de datos (similares a las celdas de memoria principal), llamadas registros, que se utilizan para el almacenamiento temporal de información dentro de la {term}`CPU`. Algunos de estos registros se consideran de propósito general, mientras que otros, son de propósito especial.

```{figure} ../images/cpu.png
:height: 160px
:align: center
:name: fig-cpu

Partes de una CPU
```

Los registros de propósito general se utilizan para el almacenamiento temporal de los datos que manipula la {term}`CPU`. Estos registros contienen las entradas a los circuitos de la {term}`ALU` y proporcionan espacio de almacenamiento para los resultados generados por esta unidad. Para realizar una operación sobre los datos almacenados en la memoria principal, la unidad de control transfiere los datos de la memoria a los registros de propósito general, informa a la {term}`ALU` que contiene los datos, activa el circuito apropiado dentro de la {term}`ALU` y le indica el registro que debe recibir el resultado.

Con el propósito de transferir patrones de _bits_, la {term}`CPU` y la memoria principal de una máquina están conectadas por una colección de cables llamada bus ({numref}`fig-cpu`). A través de este Bus, la {term}`CPU` lee datos de la memoria principal proporcionando la dirección de la celda de memoria pertinente junto con una señal electrónica que le señala al circuito de memoria que se supone que debe recuperar los datos en la celda indicada. De manera similar, la {term}`CPU` escribe datos en la memoria proporcionando la dirección de la celda de destino y los datos que se almacenarán junto con la señal electrónica apropiada que le indica a la memoria principal que se supone que debe almacenar los datos que se le envían.

Con base en este diseño, por ejemplo, la tarea de sumar dos valores almacenados en memoria principal implica más que la mera ejecución de la operación de suma. Los datos deben transferirse desde la memoria principal a los registros dentro de la {term}`CPU`, los valores deben sumarse y el resultado debe almacenarse en un registro, y luego el resultado debe transferirse hacia una celda de memoria.

Los registros de propósito general de la {term}`CPU` son utilizados en el proceso de ejecución de un programa, 

Para comprender cómo tiene lugar el proceso de ejecución general, es necesario considerar dos de los registros de propósito especial dentro de la CPU: el registro de instrucción y el contador del programa (ver nuevamente la Figura 2.4). El registro de instrucciones se utiliza para mantener la instrucción que se está ejecutando. El contador de programa contiene la dirección de la siguiente instrucción que se ejecutará, por lo que sirve como la forma en que la máquina realiza un seguimiento de dónde se encuentra en el programa.

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```