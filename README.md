# Máquina de Turing que calcula la sucesión de Fibonacci
Para este proyecto se tuvo que diseñar una implementación de una máquina de Turing que con un archivo de configuración pueda leer una cadena y encontrar el número correspondiente F(n) donde n es el número que se desea calcular y F es la función de Fibonacci.

## Convenciones
* La sucesión de Fibonacci empieza en 0.
* La máquina de Turing admite una cadena de entrada compuesta de 1's. El numero de 1's en la cadena es el numero de la sucesión de Fibonacci que se desea encontrar. Ejemplo: 1111 es el numero 4 de la sucesión de Fibonacci.
* La máquina de Turing regresa igualmente una cadena de 1's, o el numero 0 si la cadena de entrada es vacia.
* Al momento de simular la máquina de Turing, el caracter "□" representa el espacio en blanco. Y el puntero de la máquina de Turing se representa por el caracter rodeado de corchetes "[ ]" y una flecha hacia abajo que simboliza la cabeza de la simulación.

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

## Diagrama de la maquina de Turing
![3](https://github.com/MEPO29/turing-fibonacci/assets/83565262/ca523181-fb69-4e49-9a8d-5efbbd546b5e)
