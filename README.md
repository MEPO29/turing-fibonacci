# Máquina de Turing que calcula la sucesión de Fibonacci
Para este proyecto se tuvo que diseñar una implementación de una máquina de Turing que con un archivo de configuración pueda leer una cadena y encontrar el número correspondiente F(n) donde n es el número que se desea calcular y F es la función de Fibonacci.

## 1. Convenciones
* El string vacío se tomará como el elemento 0 de la secuencia de Fibonacci. El primer elemento de la sucesión es 1, donde a partir de ese momento el n-ésimo elemento de la sucesión es la suma de los dos elementos anteriores. 

* La máquina de Turing es determinista. Esto quiere decir que se cuenta con una sola regla que la máquina puede seguir según la instrucción que se da.

* El input y el output de la máquina están basados en un string de 1’s. La cantidad de 1s que se pone como input, será el n-ésimo término que se quiere calcular de la secuencia de Fibonacci. La cantidad de 1’s que devuelve como output, es el número que corresponde al n-ésimo término de la secuencia. e.g.
Input: 1111 – Calcular el 4to término de la secuencia.
Output: 111 – 3 es el 4to término de la secuencia.

* Se trabajó con la menor cantidad de reglas posibles, pues el aumento de estor no afectaría en mucho en cuanto el programa, ya que al ser una función exponencial, a partir de cierto punto sin importar la cantidad de reglas el programa sería muy poco eficiente y no podría calcular el n-ésimo número de la sucesión.


## Ejecución
Para ejecutar el programa se debe de ejecutar el archivo "main.py"
Se requiere un archivo json de configuración para la máquina de Turing.

Asimismo se debe de tener un archivo de texto con las cadenas de entrada que se desean simular. Cada cadena debe de estar en una linea diferente. Ejemplo:
```txt
1
11
111
```

El programa mostrará la simulación de la máquina de Turing para cada cadena de entrada. Al finalizar el programa se generará un archivo de texto con el nombre "output.txt" en el cual se mostrará el resultado de cada cadena de entrada.

## 2. Diagrama de la maquina de Turing
![3](https://github.com/MEPO29/turing-fibonacci/assets/83565262/ca523181-fb69-4e49-9a8d-5efbbd546b5e)

## 3. Análisis Empírico 
* La lista de entradas, así como el diagrama de dispersión, se pueden visualizar desde el archivo Listado de Prueba MAQUINAS DE TURING.xlsx. Además, nótese que los tiempos de ejecución que se tomaron en cuenta fueron cuando la máquina calculaba el n-ésimo término de la sucesión sin indicar todos los estados de la máquina. Sin embargo, realizando pruebas tomando en cuenta todos los estados e imprimiéndolos, los tiempos de ejecución fueron más largos, pero tienen el mismo comportamiento.

* La función $0.00007*e^{(0.8584x)}$ puede ser descrita por Ω(g(n)), pues debido a que esta es de orden exponencial, siempre tiene una función multiplicada por una constante que será menor o igual a ella. En este caso, la función c(g(n)) puede visualizarse de forma mas eficiente a partir de $n_0$ = 10; el décimo término de la sucesión de Fibonacci. 
