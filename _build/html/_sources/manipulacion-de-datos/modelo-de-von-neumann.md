# Modelo de von Neumann

Los computadores convencionales tienen una forma común que se atribuye a [John von Neumann](https://www.biografiasyvidas.com/biografia/n/neumann.htm) {cite}`m_ruiza_biografia_2004`, este modelo consta de cinco componentes principales ({numref}`fig-vonneumann`). La Unidad de Entrada proporciona instrucciones y datos al sistema, que posteriormente se almacenan en la Unidad de Memoria. Las instrucciones y los datos son procesados por la Unidad Aritmético-Lógica ({term}`ALU` - _Arithmetic/logic Unit_) bajo la dirección de la Unidad de Control. Los resultados se envían a la Unidad de Salida.

```{figure} ../images/von_neumann.png
:height: 280px
:align: center
:name: fig-vonneumann

Modelo de compuatador de von Neumann
```

El concepto de programa almacenado es el aspecto más importante del modelo de von Neumann. Un programa se almacena en la memoria del computador junto con los datos que se procesarán. Aunque hoy es común, antes de este concepto, los programas de computadores se almacenaban en medios externos, como placas de conexión, tarjetas perforadas o cintas. En el computador de programa almacenado, el programa se puede manipular como si fueran datos. Esto dio lugar a compiladores y sistemas operativos, y hace posible la gran versatilidad del computador moderno.

```{bibliography} ../refs.bib
:style: plain
:filter: docname in docnames
```