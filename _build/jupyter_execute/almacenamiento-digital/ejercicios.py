from myst_nb import glue
fid = open('./data/binary-msg.txt', 'r')
msg = fid.readlines()[0]
fid.close()
glue('msg-binary', msg)

# Ejercicios

1. ¿Cuál es el valor del _bit_ menos significativo en los patrones de _bits_ representados por las siguientes notaciones hexadecimales?
    - 9A
    - 1B
    - 6E

1. ¿Qué mejora se obtiene aumentando la velocidad de rotación de un disco o CD?

1. ¿Qué factores permiten que todos los discos {term}`CD`, {term}`DVD` y Blu-ray sean leídos por una misma unidad? 

1. ¿Qué ventajas proporcionan las memoriasen comparación con los otros sistemas de almacenamiento masivo?

1. ¿Qué características de las unidades de {term}`HDD` hacen que sigan siendo competitivas?

1. El siguiente código muestra un mensaje codificado en {term}`ASCII` utilizando 8 _bits_ por símbolo. Interprete lo que dice.
    {glue:text}`msg-binary`

1. Codifique las siguientes sentencias en {term}`ASCII`.
    - "Espera!" semáforo en rojo.
    - 12 + 21 = 33?

1. Convertir las siguientes representaciones binarias a su equivalente en base 10.
    - 101010
    - 100001
    - 10111
    - 0110  
    - 11111

1. Convertir cada una de las siguientes representaciones en base 10 a sus equivalente en notación binaria.
    - 32
    - 64
    - 96
    - 15
    - 27

1. ¿Cuál es el valor numérico más grande que se podría representar con 3 _bytes_ si cada dígito se codificara utilizando un patrón {term}`ASCII` por _byte_? ¿Y si se utilizara la notación binaria?
    % Un dígito por byte, en tres bytes permite almacenar tres dígitos. El mayor es 999.
    % 2^(8+8+8) = 16 777 216
1. ¿Cuántos megabytes de espacio de almacenamiento se necesitarían para almacenar un documento de 20 páginas que contiene detalles de los empleados, en el que cada página contiene 100 registros y cada registro tiene 200 caracteres, si se usaran caracteres Unicode de dos _bytes_?
    %  Solución
    %    Peso por registro = 200 char * 2 bytes = 400 bytes
    %    Peso por página = 100 regs. * 400 bytes (reg.) = 40 000 bytes
    %    Peso del documento = 40 000 bytes (pág.) * 20 = 800 000 bytes = 800 kB
1. ¿Cuál es la ventaja de representar imágenes a través de estructuras geométricas en lugar de mapas de _bits_? ¿Qué pasa con las técnicas de mapa de _bits_ en oposición a las estructuras geométricas?
    %  Solución:
    %    Una las ventajas de usar estructuras geométricas es que no sufren deformación al escalar.
1. Suponga que una cámara digital tiene una capacidad de almacenamiento de 500 MB. ¿Cuántas fotografías en blanco y negro de 512 x 512 píxeles (filas por columnas) podrían almacenarse si cada píxel requiriera 1 _bit_ de almacenamiento?
    % Solución:
    %   capacidad de cámara en bits es 500 * 2^20 = 524 288 000 bytes o 512 MB
    %   tamaño en bits de cada fotografías es 512*512 pixeles = 262 144 bits o 246 bytes
    %   cantidad de fotografía es (500*2^20)bytes / (512*512/8)bytes = 16 000
1. Suponga que una imagen está representada en una pantalla de visualización por una matriz cuadrada que contiene 256 x 256 píxeles (columnas por filas). Si para cada píxel se requieren 3 _bytes_ para codificar el color y 8 _bits_ para codificar la intensidad, ¿cuánta memoria (en _bytes_) se requieren para contener la imagen completa?
    % Solución
    %   La imagen de 256x256 (65 536) px requiere de 4 bytes (3 bytes + 8 bits) de memoria por píxel.
    %   Para su visualización se requieren una memoria de 256*256*4 = 262 144 bytes o 256*256*4 / 2^10 = 256 KiB.
1. Suponga que desea crear una copia de seguridad de sus datos de alrededor de 10 GB. ¿Qué medio de almacenamiento basado en un sistema óptico sería razonable utilizar? 
    % Bluray