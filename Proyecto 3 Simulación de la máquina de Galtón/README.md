# Mi Proyecto: La Máquina de Galton (Módulo 3)

¡Hola! Este es mi proyecto final para el tercer módulo de Python. 

## ¿De qué trata esto?
Básicamente, el programa simula 3,000 canicas que van cayendo y chocando con 12 niveles de obstáculos. En cada choque, la canica tiene que decidir: "¿Me voy a la izquierda o a la derecha?". Es como lanzar una moneda al aire en cada nivel.

## ¿Cómo lo hice?
Para que esto funcionara, seguí las reglas del PDF:
* **Dos funciones:** Una que hace todo el "trabajo sucio" de los cálculos (`simular_galton`) y otra que se encarga de dibujar la gráfica (`graficar_resultados`).
* **Puro azar:** Usé `random.randint` para que cada canica decidiera su camino. Nada de trucos con funciones prefabricadas como `normal()`.
* **Dibujitos:** Usé la librería `matplotlib` para crear el histograma. Le puse sus nombres a los ejes y un título para que se entienda qué estamos viendo.
* **Comentarios:** El código está lleno de notas para que cualquiera que lo lea sepa qué pasa en cada parte.
