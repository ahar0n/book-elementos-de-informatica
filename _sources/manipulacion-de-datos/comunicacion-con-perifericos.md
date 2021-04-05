# Comunicación con periféricos

La comunicación entre una computadora y dispositivos periféricos, tales como, sistemas de almacenamiento masivo, impresoras, teclados, ratones, pantallas de visualización, cámaras digitales e incluso otras computadoras, se maneja normalmente a través de un intermediario conocido como controlador. En el caso de un computador personal, un controlador puede consistir en circuitos montados permanentemente en la placa base del computador o, para mayor flexibilidad, puede tomar la forma de una placa de circuito que se conecta a una ranura de la placa base. En cualquier caso, el controlador se conecta mediante cables a los dispositivos periféricos dentro de la caja de la computadora o quizás a un conector, llamado puerto, en la parte posterior de la computadora donde se pueden conectar dispositivos externos. Estos controladores son a veces pequeños computadores, cada una con su propio circuito de memoria y una {term}`CPU` simple que ejecuta un programa que dirige las actividades del controlador.

Un controlador traduce mensajes y datos entre formularios compatibles con las características internas de la computadora y las del dispositivo periférico al que está conectado. Originalmente, cada controlador fue diseñado para un tipo particular de dispositivo; por lo tanto, la compra de un nuevo dispositivo periférico a menudo también requería la compra de un nuevo controlador.

Recientemente, se han tomado medidas dentro del campo de las computadoras personales para desarrollar estándares, como el _universal serial bus_ ({term}`USB`) y FireWire, mediante los cuales un solo controlador puede manejar una variedad de dispositivos. Por ejemplo, se puede utilizar un solo controlador {term}`USB` como interfaz entre una computadora y cualquier colección de dispositivos compatibles con {term}`USB`. La lista de dispositivos en el mercado actual que pueden comunicarse con un controlador {term}`USB` incluye ratones, impresoras, escáneres, dispositivos de almacenamiento masivo, cámaras digitales y teléfonos inteligentes.

Cada controlador se comunica con la computadora por medio de conexiones al mismo bus que conecta la {term}`CPU` y la memoria principal de la computadora ({numref}`fig-controladores`). Desde esta posición, puede monitorear las señales que se envían entre la {term}`CPU` y la memoria principal, así como inyectar sus propias señales en el bus.

```{figure} ../images/controladores.png
:height: 340px
:align: center
:name: fig-controladores

Controladores conectados al sistema de bus.
```

## Conexiones populares

La comunicación entre dispositivos informáticos se maneja a través de dos tipos de rutas: paralelo y serie. Estos términos se refieren a la forma en que las señales se transfieren entre sí. En el caso de la comunicación en paralelo, se transfieren varias señales al mismo tiempo, cada una en una línea separada. Esta técnica es capaz de transferir datos rápidamente, pero requiere una ruta de comunicación relativamente compleja. Un ejemplo de este tipo de comunicación es el bus interno de un computador, el cual utiliza múltiples cables para permitir que grandes bloques de datos y otras señales se transfieran simultáneamente.

Por otra parte, la comunicación en serie se basa en la transferencia de señales una tras otra a través de una sola línea. Por lo tanto, requiere una ruta de datos más simple que la comunicación en paralelo, lo que explica su popularidad. {term}`USB` y FireWire, que ofrecen transferencia de datos a una velocidad relativamente alta en distancias cortas de solo unos pocos metros, son ejemplos de sistemas de comunicación en serie. Para distancias un poco más largas (dentro de una casa o un edificio de oficinas), la comunicación en serie a través de conexiones Ethernet (por cable o radiotransmisión), es muy popular.


```{note}
El {term}`USB` es un sistemas de comunicación en serie estandarizado que simplifica el proceso de agregar nuevos dispositivos periféricos a un computador personal. Fue desarrollado bajo la dirección de Intel. En esta configuración, el controlador traduce las características de la señal interna de un computador a la señale estándar USB. A su vez, cada dispositivo conectado al controlador convierte las características internas de las señales internas al mismo estándar USB, lo que permite la comunicación con el controlador. El resultado es que conectar un nuevo dispositivo a un computador no requiere la inserción de un nuevo controlador.

El bajo costo de la tecnología {term}`USB` 2.0 lo ha convertido en el líder en el mercado masivo. También ha comenzado a aparecer nuervas versiones en el mercado, como la versión 3.0.
```

## Tasas de transferencia

La velocidad a la que los _bits_ se transfieren de un componente a otro se mide en _bits_ por segundo (bps). Las unidades comunes incluyen Kbps (kilobps, igual a mil bps), Mbps (megabps, igual a un millón de bps) y Gbps (gigabps, igual a mil millones de bps). Tener presente que, en abreviaturas, una b minúscula generalmente significa _bit_, mientras que una B mayúscula significa _byte_.

Para comunicaciones de corta distancia, USB 2.0 y FireWire proporcionan velocidades de transferencia de varios cientos de Mbps, lo que es suficiente para la mayoría de las aplicaciones multimedia. Esto, combinado con su conveniencia y costo relativamente bajo, es la razón por la que son populares para la comunicación entre computadoras domésticas y periféricos locales como impresoras, unidades de disco externas y cámaras.

Combinando multiplexación (codificación o entrelazado de datos de modo que una sola ruta de comunicación sirva para el propósito de múltiples rutas) y técnicas de compresión de datos, los sistemas telefónicos de voz tradicionales pudieron soportar tasas de transferencia de 57.6 Kbps. Esto no satisface las necesidades de las aplicaciones de Internet y multimedia actuales, como la transmisión de videos de alta definición desde sitios como Netflix o YouTube. Para reproducir grabaciones de música MP3 se requiere una tasa de transferencia de aproximadamente 64 Kbps, y para reproducir incluso videoclips de baja calidad se requieren tasas de transferencia medidas en unidades de Mbps. Esta es la razón por la que alternativas como los enlaces {term}`DSL` y cable, que proporcionan tasas de transferencia dentro del rango de Mbps, han reemplazado a los sistemas telefónicos de audio tradicionales. Por ejemplo, {term}`DSL` ofrece tasas de transferencia del orden de 54 Mbps.

La velocidad máxima disponible en un entorno particular depende del tipo de ruta de comunicación y la tecnología utilizada en su implementación. Esta tasa máxima a menudo se equipara de manera vaga con el ancho de banda (_bandwidth_) de la ruta de comunicación, aunque el término ancho de banda también tiene connotaciones de capacidad en lugar de tasa de transferencia. Esto es, decir que una ruta de comunicación proporciona un servicio de banda ancha, significa que la ruta de comunicación tiene la capacidad de transferir _bits_ a una velocidad alta, así como la capacidad de transportar grandes cantidades de información simultáneamente.

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```