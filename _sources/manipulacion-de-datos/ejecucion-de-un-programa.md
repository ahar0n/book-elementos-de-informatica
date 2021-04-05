(content:ejecucion-de-un-programa)=
# Ejecución de un programa

Un computador ejecuta un programa almacenado en su memoria copiando las instrucciones desde la memoria a la {term}`CPU` según sea necesario. Una vez en la {term}`CPU`, cada instrucción es decodificada y seguida. El orden en el que se obtienen las instrucciones de la memoria corresponde al orden en el que se almacenan en la memoria.

```{figure} ../images/registros-especiales.png
:height: 230px
:align: center
:name: fig-registros-cpu

Registros de propósito especial de la {term}`CPU`.
```

Para comprender cómo se lleva a cabo el proceso de ejecución general, es necesario considerar dos de los registros de propósito especial dentro de la {term}`CPU`: el registro de instrucción y el contador de programa (ver {numref}`fig-registros-cpu`). El registro de instrucciones se utiliza para mantener la instrucción que se está ejecutando. El contador de programa contiene la dirección de la siguiente instrucción que se ejecutará, por lo que sirve como la forma en que la máquina realiza un seguimiento de dónde se encuentra en el programa.
La {term}`CPU` realiza su trabajo repitiendo continuamente un algoritmo que la guía a través de un proceso de tres pasos conocido como ciclo de la máquina. 

```{figure} ../images/ciclo_maquina.png
:height: 400px
:align: center
:name: fig-ciclo-maquina

El ciclo máquina.
```

Los pasos del ciclo de la máquina son recuperar, decodificar y ejecutar ({numref}`fig-ciclo-maquina`). Durante el paso de recuperar, la {term}`CPU` solicita a la memoria principal la instrucción que está almacenada en la dirección indicada en el contador del programa. La {term}`CPU` coloca la instrucción recibida de la memoria en su registro de instrucciones y luego incrementa el contador del programa para que el contador contenga la dirección de la siguiente instrucción almacenada en la memoria. Por lo tanto, el contador del programa estará listo para la siguiente recuperación.

Con la instrucción en el registro de instrucciones, la {term}`CPU` decodifica la instrucción, luego ejecuta la instrucción activando los circuitos apropiados para realizar la tarea solicitada. Por ejemplo, si la instrucción es una carga de la memoria, la {term}`CPU`  envía las señales apropiadas a la memoria principal, espera a que la memoria principal envíe los datos y luego coloca los datos en el registro solicitado. Si la instrucción es para una operación aritmética, la {term}`CPU` activa el circuito apropiado en la {term}`ALU` con los registros correctos como entradas y espera a que la {term}`ALU` calcule la respuesta y la coloque en el registro apropiado.

Una vez que se ha ejecutado la instrucción en el registro de instrucciones, la {term}`CPU` comienza nuevamente el ciclo de la máquina desde el primer paso. Debido que el contador del programa se incrementó al final de la recuperación anterior, nuevamente proporciona a la {term}`CPU` la dirección correcta.

A continuación se ejemplifica de la ejecución de un programa. {cite}`brookshear_computer_2015` Suponga que el programa se encuentra almacenado en la memoria principal, en direcciones consecutivas, comenzando en la dirección A0 (hexadecimal). La máquina lo ejecute colocando la dirección (A0) de la primera instrucción en el contador del programa ({numref}`fig-programa-memoria`).

```{figure} ../images/programa-en-memoria.png
:height: 260px
:align: center
:name: fig-programa-memoria

El ciclo máquina.
```

La {term}`CPU` comienza el ciclo máquina recuperando la instrucción almacenada en la ubicación A0 de la memoria principal y colocando esta instrucción (156C) en su registro de instrucciones ({numref}`fig-programa-recuperacion`). Notar que en esta máquina las instrucciones tienen una longitud de 16 _bits_ (dos _bytes_). Por lo tanto, la instrucción completa que se recuperar ocupa las celdas de memoria en las direcciones A0 y A1. La {term}`CPU` está diseñada para tener esto en cuenta, por lo que recupera el contenido de ambas celdas y coloca los patrones de _bits_ en el registro de instrucciones, el cual tiene una longitud de 16 _bits_. Luego, la {term}`CPU` agrega dos al contador del programa para que este registro contenga la dirección de la siguiente instrucción ({numref}`fig-programa-incremento`). Al final del paso de recuperación del primer ciclo de la máquina, el contador del programa contiene A2 y el registro de instrucciones contienen 156C.

```{figure} ../images/programa-recuperacion.png
:height: 280px
:align: center
:name: fig-programa-recuperacion

Recuperación de instrucción desde la memoria principal.
```

```{figure} ../images/programa-incremento.png
:height: 280px
:align: center
:name: fig-programa-incremento

Incremento del contador que apunta a la instrucción siguiente.
```

A continuación, la {term}`CPU` analiza la instrucción en su registro de instrucciones y ejecuta las acciones obtenidas de la instrucción. Esta actividad se realiza durante el paso de ejecución del ciclo de la máquina, y luego la {term}`CPU` comienza el siguiente ciclo. Este ciclo comienza obteniendo la instrucción 166D de las dos celdas de memoria que comienzan en la dirección A2. La {term}`CPU` coloca esta instrucción en el registro de instrucciones e incrementa el contador del programa a A4. Por lo tanto, los valores en el contador de programa contiene A4 y el registro de instrucciones contiene 166D. Este proceso se repite hasta que se ejecutan todas las instrucciones del programa almacenado.

## Lenguaje máquina

Para aplicar el concepto de programa almacenado, las {term}`CPU` están diseñadas para reconocer instrucciones codificadas como patrones de _bits_. Esta colección de instrucciones junto con el sistema de codificación se denomina lenguaje máquina.

La lista de instrucciones máquina que una {term}`CPU` típica debe poder decodificar y ejecutar es bastante corta. De hecho, una vez que una máquina puede realizar ciertas tareas elementales pero bien elegidas, agregar más funciones no aumenta las capacidades teóricas de la máquina. 

El grado en que los diseños de máquinas deben aprovechar este hecho ha llevado a dos filosofías de la arquitectura de la {term}`CPU`. Una es que una {term}`CPU` debe diseñarse para ejecutar un conjunto mínimo de instrucciones de máquina. Este enfoque conduce a lo que se llama computador de conjunto de instrucciones reducido ({term}`RISC` - _reduced instruction set computer_). El argumento a favor de la arquitectura {term}`RISC` es que dicha máquina es eficiente, rápida y menos costosa de fabricar. Por otro lado, otros argumentan a favor de las {term}`CPU` con la capacidad de ejecutar una gran cantidad de instrucciones complejas, aunque muchas de ellas son técnicamente redundantes. El resultado de este enfoque se conoce como computador de conjunto de instrucciones complejas ({term}`CISC` - _complex instruction set computer_). El argumento a favor de la arquitectura {term}`CISC` es que la {term}`CPU` más compleja puede hacer frente mejor a las complejidades cada vez mayores del software actual. Con {term}`CISC`, los programas pueden explotar un poderoso y rico conjunto de instrucciones, muchas de las cuales requerirían una secuencia de múltiples instrucciones en un diseño {term}`RISC`. En la década de 1990 y en el nuevo milenio, los procesadores {term}`CISC` y {term}`RISC` disponibles comercialmente competían activamente por el dominio en la computación de escritorio. Los procesadores Intel, utilizados en PC, son ejemplos de arquitectura {term}`CISC`. Los procesadores PowerPC (desarrollados por una alianza entre Apple, IBM y Motorola) son ejemplos de arquitectura {term}`RISC` y se utilizaron en Apple Macintosh. A medida que pasaba el tiempo, el costo de fabricación de {term}`CISC` se redujo drásticamente; por lo tanto, los procesadores de Intel (o su equivalente de AMD — Advanced Micro Devices, Inc.) ahora se encuentran en prácticamente todas los computadores de escritorio y portátiles.
Si bien {term}`CISC` aseguró su lugar en los computadores de escritorio, tienen un alto consumo energético. Por el contrario, la empresa Advanced RISC Machine (ARM) ha diseñado una arquitectura {term}`RISC` específicamente para un bajo consumo de energía. Por lo tanto, los procesadores basados ​​en ARM, fabricados por una gran cantidad de proveedores, incluidos Qualcomm y Texas Instruments, se encuentran en controladores de juegos, televisores digitales, sistemas de navegación, módulos automotrices, celulares. teléfonos, teléfonos inteligentes y otros productos electrónicos de consumo. 

Independientemente de la arquitectura, {term}`RISC` o {term}`CISC`, las instrucciones máquina se pueden clasificar en tres grupos:

1. __Grupo de transferencia de datos__ consta de instrucciones que solicitan el movimiento de datos de una ubicación a otra.
1. __Grupo aritmético/lógico__ consta de las instrucciones que le dicen a la unidad de control que solicite una actividad dentro de la {term}`ALU`, tales como, operaciones aritméticas básicas y las [operaciones booleanas](content:operaciones-booleanas).
1. __Grupo de control__ consta de aquellas instrucciones que dirigen la ejecución del programa en lugar de la manipulación de datos. Por ejemplo, saltos incondicionales (de una instrucción a otra) y saltos condicionales (a partir del cumplimiento o no de una condición).

## Rendimiento de una CPU

El reloj de un computador es un circuito, llamado oscilador, que genera pulsos que se utilizan para coordinar las actividades de la máquina; cuanto más rápido genera pulsos este circuito oscilante, más rápido realiza la máquina su ciclo de máquina. Las velocidades del reloj se miden en hercios (abreviado como Hz) con 1 Hz igual a un ciclo (o pulso) por segundo. Las velocidades de reloj típicas en los computadores de escritorio están en el rango de unos pocos cientos de MHz (megahertz, que es un millón de Hz) para modelos más antiguos, a varios GHz (gigahertz, que es 1000 MHz).

Desafortunadamente, diferentes diseños de CPU pueden realizar diferentes cantidades de trabajo en un ciclo de reloj y, por lo tanto, la velocidad del reloj por sí sola no es relevante al comparar máquinas con diferentes CPU. Si está comparando una máquina basada en un procesador Intel con una basada en ARM, sería más significativo comparar el rendimiento mediante la evaluación comparativa, que es el proceso de comparar el rendimiento de diferentes máquinas al ejecutar el mismo programa, conocido como _benchmark_. Al seleccionar puntos de referencia que representan diferentes tipos de aplicaciones, se obtiene comparaciones significativas para varios segmentos del mercado. (por ejemplo, [Comparativa de rendimiento: Intel vs AMD Ryzen](https://www.profesionalreview.com/2020/04/05/procesadores-intel-vs-amd-ryzen/))

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```