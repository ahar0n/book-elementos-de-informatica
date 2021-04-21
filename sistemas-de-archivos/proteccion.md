# Protección

Cuando la información se almacena en un sistema informático, es impor- tante mantener ciertos niveles de seguridad de daños físicos (fiabilidad) y del acceso indebido (protección).

La fiabilidad se obtiene generalmente mediante copias duplicadas de los archivos. Muchos informáticos tienen programas de sistemas que copian automáticamente los archivos de disco a sistemas de respaldo con intervalos regulares (una vez al día o a la semana o al mes) para mantener una copia en caso de que un sistema de archivos se destruya accidentalmente. Los sistemas de archivos pueden ser dañados por problemas de hardware (como errores de lectura o escritura), subidas o bajadas de tensión, caídas de cabeza, suciedad, temperaturas extremas, entre otros. Los archivos pueden ser borrados accidentalmente. Los errores en el software del sistema de archivos también pueden causar la pérdida del contenido de los archivos.

La protección se puede proporcionar de muchas maneras. En un sistemas con multiples usuarios se necesitan mecanismos de protección, los cuales proporcionan un acceso controlado limitando los tipos de acceso a los archivos. El acceso se permite o se niega dependiendo de varios factores, uno de los cuales es el tipo de acceso solicitado. Se pueden controlar varios tipos diferentes de operaciones:

- Lectura de un archivo.
- Escritura o re-escritura de archivo.
- Ejecución, carga de un archivo en memoria y ejecución. 
- Adicionar nueva información al final de un archivo. 
- Borrar un archivo.
- Listar el nombre y atributos de un archivos.

También pueden controlarse otras operaciones, como el cambio de nombre, la copia y la edición del archivo. Sin embargo, en muchos sistemas, estas funciones de nivel superior pueden ser implementadas por un programa de sistema.

El enfoque más común del problema de la protección es hacer que el acceso dependa de la identidad del usuario. Diferentes usuarios pueden necesitar diferentes tipos de acceso a un archivo o directorio. El esquema más general para aplicar el acceso dependiente de la identidad es asociar a cada archivo y directorio una lista de control de acceso ({term}`ACL` - _acces-control-list_) en la que se especifiquen los nombres de los usuarios y los tipos de acceso permitidos para cada uno de ellos. Cuando un usuario solicita acceso a un determinado archivo, el {term}`OS` comprueba la lista de acceso asociada a ese archivo. Si ese usuario figura en la lista para el acceso solicitado, el acceso está permitido. De lo contrario, se produce una violación de la protección y se deniega al usuario el acceso al archivo.

En general los {term}`OS`s definen una lista de control de acceso con tres clasificaciones de usuarios en relación con cada archivo:

`owner`
: Usuario que creó el archivo es el propietario. 

`group`
: Usuarios que compartan el archivo. 

`universe` 
: Todos los demás usuarios del sistema.

Entonces, sólo se necesitan tres campos para definir la protección. A menudo, cada campo es una colección de bits, y cada bit permite o impide el acceso asociado a él. Por ejemplo, el sistema UNIX define tres campos de 3 bits cada uno: `rwx`, donde `r` controla el acceso de lectura, `w` controla el acceso de escritura y `x` controla la ejecución. Se mantiene un campo separado para el propietario del archivo, para el grupo del archivo y para todos los demás usuarios. En este esquema, se necesitan 9 bits por archivo para registrar la información de protección. En el siguiente ejemplo, se presenta el nivel de protección de un archivo es sistema UNIX. El primer campo describe indica si es un subdirectorio (`d`) o no. También se muestra el número de enlaces al archivos, el nombre del propietario, el nombre del grupo, el tamaño en bytes, la fecha de modificación y el nombre del archivo.

```plain
-rw-rw-r--   5 aharon  staff.  31200  May 15 06:25  intro.tex
```

Los usuarios de Windows suelen gestionar las listas de control de acceso a través de la {term}`GUI`. La {numref}`fig-proteccion` muestra una ventana de permisos del subdirectorio `dir2` en el sistema de archivos NTFS de Windows 10.

```{figure} ../images/proteccion-win.png
:height: 500px
:align: center
:name: fig-proteccion

Gestión de la {term}`ACL` en Microsoft Windows 10.
```