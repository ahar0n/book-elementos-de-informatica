# Windows Commands

> El shell de comandos fue el primer interprete de comandos incorporado en Windows para automatizar tareas rutinarias con archivos por lotes (`.bat`). Es posible automatiza operaciones de forma eficiente utilizando scripts que aceptan todos los comandos disponibles en la línea de comandos.
>
> -- [Microsoft.com](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands)

El interprete de comandos (`cmd.exe`) de Windows es un software que proporciona comunicación directa entre el usuario y el sistema operativo o la aplicación, lo que proporciona un entorno para automatizar las operaciones y scripting básico.

## Iniciar el interprete

Existen dos formas de abrir el interprete de comandos de Windows:

1. Escribir `cmd.exe` en la caja de la barra de búsqueda de la barra de tareas y hacer click en la aplicación Command Prompt de la lista de resultados.

2. Abrir una ventana de ejecutar en Windows con la combinación <kbd>Win</kbd> + <kbd>R</kbd>, escribir la palabra `cdm.exe` y pulsar aceptar.

Por defecto el intérprete de comandos inicia en el directorio del usuario, como se muestra en {numref}`fig-prompt`. En algunas ocasiones es necesario solicitar permisos de administrados para ejecutar acciones con el sistema.

```{figure} ../images/prompt.png
:width: 500px
:name: fig-prompt

Ventana del intérprete de comandos (`cmd.exe`) de Windows 10.
```

Windows inicia el intérprete de comandos en el directorio de usuario. Por ejemplo, en la imagen anterior el prompt está indicando que el usuario se encuentra en el dispositivo `C:` , en el subdirectorio **aharon** del directorio **User**. El intérprete esta esperando que se ingresen comandos.

El _path_ se refiere a la ubicación o nombre de un archivos, dispositivo o página web donde está localizado.

```{figure} ../images/path.png
:height: 100px
:name: fig-path

Esquema de _path_ en Windows.
```

```{note}
- Los comandos se ejecutan uno a uno escribiendo el comando y presionando <kbd>Enter</kbd>.
- El intérprete no distingue entre mayúsculas y minúsculas.
- Para trabajar con nombres de archivos o directorios con un espacio, deben ser ingresados entre comillas. Por ejemplo, el directorio **Mis Documentos** debería teclearse `"Mis Documentos"`.
- Los nombres de archivos pueden tener un archivo largo de 255 caracteres y una extensión de archivo de tres caracteres.
- Cuando se elimina un archivo o directorio en la línea de comandos, no se mueve a la Papelera de reciclaje.
- Para solicitar ayuda con cualquier de los comandos, escriba `/?` después del comando. Por ejemplo, `dir /?` mostraría las opciones disponibles para el comando `dir`.
```

## Comandos básicos

### Listar archivos

Escriba `dir` en el prompt para listar los archivos en el directorio actual. Se debería obtener una salida similar a la imagen de ejemplo de abajo.

```{figure} ../images/dir-out.png
:width: 500px
:name: fig-dir-out
```

Notar que la salida muestra variada información útil, incluyendo la fecha y hora de creación, los directorios (`<DIR>`), y el nombre del directorio o archivo. En el ejemplo, hay 0 archivos listados y 15 directorios como se indica por el estado en la parte inferior de la salida.

Cada comando tiene opciones, que son interruptores y comandos adicionales que pueden añadirse después del comando. Por ejemplo, con el comando `dir` puede aceptar el interruptor `/p` para listar los archivos y directorios en el directorio actual una página a la vez. Este interruptor es útil para ver todos los archivos y directorios de un directorio que tienen muchos archivos.

Cada una de las opciones y conmutadores de comandos puede ser buscado en la [documentación](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands) específica de cada comando.

### Navegar entre directorios

Para moverse a un directorio se usa el comando `cd`, por lo tanto para moverse al **Escritorio** debería teclear (seguido de <kbd>Enter</kbd>):

```plain
cd Escritorio
```

Entonces, en el ejemplo, el prompt debería cambiar  `C:\Users\aharon\Desktop>`.

Antes de cambiar de directorio, será necesario conocer los directorios que están disponibles en el directorio actual. Para ello, puede usar el comando `dir`.

Para retroceder un directorio, puede usar el siguiente comando.

```plain
cd ..
```

En el ejemplo, subirá un nivel en la estructura de directorios, esto es, al directorio `C:\Users\aharon\`. Para volver a retroceder un directorio se tendría que volver a teclear `cd..` y se posicionaría en `C:\Users\`.

Si estuvieras en más de un directorio (por ejemplo, `C:\Users\aharon\Desktop\`) y quisieras volver al directorio raíz `c:\`, podrías usar el siguiente comando.

```plain
cd \
```

La raíz o directorio raíz (_root directory_) es el nivel más alto en una jerarquía de directorios e incluye todos los demás directorios bajo ella.

Para moverse en varios directorios con un solo comando, el comando similar al ejemplo siguiente. En este ejemplo, el comando se movería al directorio del **System**, que es un subdirectorio del directorio de **Windows**.

```plain
cd Windows/System
```

### Crear directorios

Para crear un directorio en el directorio actual, usa el comando `mkdir`. Por ejemplo, el siguiente comando crea el directorio **prueba.** Si se crea con éxito, se le devolverá al prompt sin ningún mensaje de error. Una vez creado el directorio, puede ingresar a él utilizando el comando `cd`.

```plain
mkdir prueba
```

En el siguiente ejemplo se crea el directorio **Nueva carpeta**. Note que para tratar con nombres que incluyen espacios, debe ingresar el nombre entre comillas dobles.

```plain
mkdir "Nueva Carpeta"
```

### Crear archivos de texto

El comando `copy con` permite crear un archivo y escribir su contenido línea por línea.

Al ejecutar el siguiente comando, el cursor se mueve hacia abajo hasta una línea en blanco, lo que permite agregar contenido al nuevo archivo línea por línea. Una vez que agregue todo el contenido deseado, para crear el archivo, presione <kbd>Enter</kbd> para llegar a una línea en blanco, presione la combinación de teclas <kbd>CTRL</kbd> + <kbd>Z</kbd>. Una vez que aparezca `^Z` en la pantalla, presione <kbd>Enter</kbd> para guardar el archivo y salir. En la pantalla se mostrará un mensaje indicando que el archivo ha sido creado.

```plain
copy con mi_archivo.txt
```

Utilizando el comando `dir` podrá comprobar en el listado mostrado que aparecerá el archivo **mi_archivo.txt**.

Alternativamente, puede iniciar el programa Notepad de Windows y cualquier editor de texto para crear un archivo desde la línea de comandos. Por ejemplo,

```plain
start notepad mi_segundo_archivo.txt
```

El comando anterior utiliza el comando de `start` para ejecutar el Notepad y crear **mi_segundo_archivo.txt**. Una vez que se guardan los cambios del archivo, se crea en el mismo directorio en el que se ejecutó el comando de inicio.

El comando `type` muestra el contenido de un archivo de texto, como el creado anteriormente. Por ejemplo, la siguiente expresión mostraría en pantalla el contenido del archivo **mi_archivo.txt**.

```plain
type mi_archivo.txt
```

Debe considerar que si muestra un archivo binario o un archivo creado por un programa, es posible que vea caracteres extraños en la pantalla, estos caracteres representan códigos de control que se utilizan en el archivo binario. En general, no es una buena alternativa usar el comando `type` para mostrar archivos binarios.

### Mover y copiar archivos

El siguiente comando lo sitúa en el directorio raíz.

```plain
cd \
```

Ahora, cree el directorio **dir2** en el directorio raíz. Luego, ingrese con el comando `cd`.

```plain
mkdir dir2
cd dir2
```

A continuación cree el archivo **nuevo_archivo.txt** con el contenido que usted desee, utilizando el siguiente comando. Puede comprobar su existencia usando el comando `dir`.

```plain
copy con nuevo_archivo.txt
```

Ahora, utilizando el comando `move` moveremos el archivo creado en la carpeta **dir2** hacia el directorio raíz.

```plain
move nuevo_archivo.txt c:\
```

Si tiene exito, se mostrará un mensaje que indicará que el archivo ha sido movido. Si en la instrucción anterior, sustituye el comando `move` por el comando `copy`, se generará una copia del archivo la dirección de destino, en lugar de moverlo.

Para copiar múltiples archivos de un lugar a otro podría usar el carácter [comodín asterisco](https://www.notion.so/Windows-commands-306058b939df4317a9a7ff232fbc595e#c3b6382e31c147419c067fd110ad2058) `*`. La ejecución de la siguiente instrucción copia todos los archivos con extensión **txt** desde el directorio actual hacia directorio **dir2**.

```plain
copy *.txt c:/dir2
```

El siguiente código copia todos los archivos del directorio actual hacia el directorio **prueba**.

```plain
copy *.* c:/prueba
```

También es posible realizar copias de archivos en el mismo directorio (duplicar). La siguiente expresión realizaría una copia del archivo **nuevo_archivo.txt** con el nombre **backup.txt**.

```plain
copy nuevo_archivo.txt backup.txt
```

### Renombrar archivos y directorios

El comando `rename` permite renombrar archivos. Por ejemplo, la siguiente expresión modifica el nombre del archivo **nuevo_archivo.txt** a **ejemplo.txt**. Utilizando el comando `dir` podríamos verificar que el archivo **nuevo_archivo.txt** ya no existe, pero si el archivo **ejemplo.txt**.

```plain
rename nuevo_archivo.txt ejemplo.txt
```

Este comando también permite renombrar directorios. La siguiente expresión renombra el directorio **dir2** a **directorio2**. Verificar los resultados de esta acción con el comando `dir`.

```plain
rename dir2 directorio2
```

### Borrar archivos

El comando `del` nos permite borrar archivos. La siguiente expresión eliminaría el archivo **ejemplo.txt**. Si tiene éxito, la pantalla no mostrará errores y el comando `dir` no mostrará el archivo en el listado.

```plain
del ejemplo.txt
```

### Wildcard

También conocido como carácter comodín, es un símbolo que se utiliza para reemplazar o representar uno o más caracteres. Los comodines más comunes son el asterisco (*), que representa uno o más caracteres y el signo de interrogación (?) que representa un solo carácter. 

- El comodín asterisco `*` coincide con cualquier carácter cero o más veces. Por ejemplo, `comp*` coincide con cualquier cosa que empiece por "comp", tales como, "computacion", "completo" y "computador".
- Un signo de interrogación `?` coincide con un solo caracter. Por ejemplo, "c?mp" coincide con "camp" y "comp". El signo de interrogación también puede ser usado más de una vez. Por ejemplo, "c??p" coincidiría con los dos ejemplos anteriores así como con "coop". Un signo de interrogación a continuación de otro coincidirá con cualquier caracter o ninguno. Por ejemplo, "co??" coincidiría con todos los ejemplos anteriores, pero como son signos de interrogación posteriores también coincidiría con "cop" aunque no sean cuatro caracteres.