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
Código en python del diagrama de turing
## Diagrama de la maquina de turing 
from graphviz import Digraph

def create_graph(transitions):
    graph = Digraph('G')
    graph.attr(rankdir='LR', size='8,5')

    for state in transitions:
        graph.node(state)

    for state, transitions in transitions.items():
        for symbol, (next_state, write, move) in transitions.items():
            graph.edge(state, next_state, label=f'{symbol}, {write}, {move}')

    return graph

graph = create_graph({
    "0": {"1": ["1","X",1], "X": ["18", "0", 1]},
    "1": {"1": ["2","X",1], "X": ["18", "1", 1]},
    "2": {"1": ["2","1",1], "X": ["3", "0", 1]},
    "3": {"X": ["4", "A", 1]},
    "4": {"X": ["5", "0", 1]},
    "5": {"X": ["12", "A", -1]},
    "7": {"1": ["7", "A", 1], "0": ["7", "0", 1], "A": ["7", "A", 1], "X": ["8", "0", -1]},
    "8": {"1": ["8", "1", -1], "0": ["9", "0", -1], "A": ["10", "1", 1]},
    "9": {"1": ["9", "1", -1], "0": ["12", "0", -1], "A": ["10", "1", 1]},
    "10": {"1": ["10", "1", 1], "0": ["10", "0", 1], "X": ["11", "1", -1]},
    "11": {"1": ["11", "1", -1], "0": ["8", "0", -1]},
    "12": {"1": ["12", "1", -1], "0": ["12", "0", -1], "A": ["12", "A", -1], "X": ["13", "X", 1]},
    "13": {"1": ["14", "X", 1], "0": ["15", "1", 1]},
    "14": {"1": ["14", "1", 1], "0": ["7", "0", 1]},
    "15": {"1": ["15", "A", 1], "0": ["15", "0", 1], "A": ["15", "A", 1], "X": ["16", "X", -1]},
    "16": {"0": ["17", "X", -1], "A": ["16", "1", -1]},
    "17": {"1": ["18", "X", 1], "0": ["17", "X", -1], "A": ["17", "X", -1]}
})

graph.render('G', view=True)

## 3. Análisis Empírico 
* La lista de entradas, así como el diagrama de dispersión, se pueden visualizar desde el archivo Listado de Prueba MAQUINAS DE TURING.xlsx. Además, nótese que los tiempos de ejecución que se tomaron en cuenta fueron cuando la máquina calculaba el n-ésimo término de la sucesión sin indicar todos los estados de la máquina. Sin embargo, realizando pruebas tomando en cuenta todos los estados e imprimiéndolos, los tiempos de ejecución fueron más largos, pero tienen el mismo comportamiento.


* Sea F(n) = nuestra sucesión de Fibonacci. Notese que F(0)=0 y F(1)=1
  Entonces, F(n) = F(n-1) + F(n-2) + O(1) para todo n>1.

  Asuma que F(n-1) = F(n-2).
    
  Por inducción,
  
  ** Paso base
  
  $$F(2) = F(2-1) + F(2-2) + 0 = F(1)+F(0) = 1 + 0 = 1$$

  **  Paso inductivo
  
  Sea $F(n-1) = O(2^{n-1})$
  
  Entonces, $F(n) = F(n-1) + F(n-2) + O(1) = O(2^{n-1}) + O(2^{n-2}) +O(1) = O(2^{n})$

  A pesar de la suposición inicial de F(n-1) = F(n-2), note que F(n-2) $<=$ F(n-1), por lo que es una cota superior, indicando que es una cota superior de la sucesión.

  * La función $0.00007*e^{(0.8584n)}$ puede ser descrita por O(g(n)), pues debido a que esta es de orden exponencial, siempre tiene una función multiplicada por una constante que será mayor o igual a ella. En este caso, la función c(g(n)) = $c2^{n}$ puede visualizarse de forma mas eficiente a partir del primer término de la sucesión de Fibonacci.
  
  Note que $c2^n \geq 0.0007e^{0.8584n}$
  <img width="777" alt="image" src="https://github.com/MEPO29/turing-fibonacci/assets/87022337/ec4d55a0-2927-4fdb-9cdc-976a845fa8a8">
  
  ## 4. Bibliografía
GeeksforGeeks (2023). Turing Machine in TOC. https://www.geeksforgeeks.org/turing-machine-in-toc/

Mark Jago. [Computerphile]. (29 de agosto de 2019). Turing Machines Explained - Computerphile [Video]. YouTube. https://www.youtube.com/watch?v=dNRDvLACg5Q

Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein. 2009. Introduction to Algorithms, Third Edition (3rd. ed.). The MIT Press.
