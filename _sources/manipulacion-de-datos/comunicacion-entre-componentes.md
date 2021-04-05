# Comunicación entre componentes

Aunque el modelo de Von Neumann prevalece en las computadoras modernas, se ha simplificado. La Figura 1-3 muestra el modelo de bus del sistema de un sistema informático. Este modelo divide un sistema informático en tres subunidades: CPU, memoria y entrada / salida (E / S). Este refinamiento del modelo von Neumann combina la ALU y la unidad de control en una unidad funcional, la CPU. Las unidades de entrada y salida también se combinan en una sola unidad de E / S.

Lo más importante para el modelo de bus del sistema, las comunicaciones entre los componentes son por medio de una vía compartida llamada bus del sistema, que está compuesto por el bus de datos (que lleva la información que se transmite), el bus de direcciones (que identifica dónde se envía la información) y el bus de control (que describe aspectos de cómo se envía la información y de qué manera). También hay un bus de potencia para la alimentación eléctrica de los componentes, que no se muestra, pero se entiende su presencia. Algunas arquitecturas también pueden tener un bus de E / S independiente.

Físicamente, los buses están formados por conjuntos de cables agrupados por función. Un bus de datos de 32 bits tiene 32 cables individuales, cada uno de los cuales transporta un bit de datos (a diferencia de la dirección o la información de control). En este sentido, el bus del sistema es en realidad un grupo de buses individuales clasificados por su función.

El bus de datos mueve datos entre los componentes del sistema. Algunos sistemas tienen buses de datos separados para mover información hacia y desde la CPU, en cuyo caso hay un bus de entrada de datos y un bus de salida de datos. Más a menudo, un solo bus de datos mueve datos en cualquier dirección, aunque nunca en ambas direcciones al mismo tiempo.

Si el bus se va a compartir entre entidades comunicantes, las entidades deben tener identidades distinguidas: direcciones. En algunas computadoras, se asume que todas las direcciones son direcciones de memoria, ya sea que de hecho formen parte de la memoria de la computadora o que sean en realidad dispositivos de E / S, mientras que en otras, los dispositivos de E / S tienen direcciones de E / S separadas. (Este tema de direcciones de E / S se trata con más detalle en el Capítulo 8, Entrada, salida y comunicación).

Una dirección de memoria, o ubicación, identifica una ubicación de memoria donde se almacenan los datos, de manera similar a la forma en que una dirección postal identifica la ubicación donde un destinatario recibe y envía correo. Durante una operación de lectura o escritura de la memoria, el bus de direcciones contiene la dirección de la ubicación de la memoria donde se leerán o escribirán los datos. Tenga en cuenta que los términos "leer" y "escribir" se refieren a la CPU: la CPU lee datos de la memoria y escribe datos en la memoria. Si los datos se van a leer de la memoria, el bus de datos contiene el valor leído de esa dirección en la memoria. Si los datos se van a escribir en la memoria, el bus de datos contiene el valor de los datos que se van a escribir en la memoria.

El bus de control es algo más complejo y aplazamos la discusión de este bus para capítulos posteriores. Por ahora, se puede pensar en el bus de control como coordinando el acceso al bus de datos y al bus de direcciones, y dirigiendo los datos a componentes específicos.

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```