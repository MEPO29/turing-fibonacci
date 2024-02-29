import itertools
import time
import json

class Turing:
    # Función para inicializar el objeto de la máquina
    def __init__(self, tape, turing_table, initial_pos = 1):
        self.tape = tape
        self.pos = initial_pos
        self.turing_table = turing_table
        self.value = self.tape[self.pos]
        self.state = "0"
    
    def move(self):
        # Obtener valor de la máquina en la posición actual
        self.value = self.tape[self.pos]   
        # Obtener movimiento a realizar          
        new = self.turing_table[self.state][self.value]
        
        # Obtener estado nuevo
        self.state = new[0]
        # Guardar estado nuevo
        self.tape[self.pos] = new[1]
        # Guardar posición nueva
        self.pos += new[2]

        # Reemplazar X por espacio en blanco
        tape_str = ''.join(self.tape).replace("X", "□")
        # Posición del head
        head_str = ''.join([' ']*(self.pos+1)) + '\u2193'
        # String del estado actual
        estado_act = tape_str[:self.pos]+"["+tape_str[self.pos]+"]" + tape_str[self.pos +1:]
        # Imprimir información a la consola
        print(head_str)
        print(estado_act)
        print(f"State: {self.state}")
        print()
        
    def run(self) -> str:
        # Tomar tiempo de inicio de la ejecución
        start_time = time.time()
        while self.state != "18":
            self.move()
        # Imprimir tiempo final
        print("Tiempo: %s segundos" % (time.time() - start_time))
        return "".join(self.tape).replace("X", "") + " = " + str(self.tape.count("1"))
    
    


def multiple(file_name, reglas_turing):
    # Leer archivo de reglas de transición y cargarlo
    f = open(reglas_turing)
    data = json.load(f)
    # Definir la tabla de transiciones como objeto
    turing_table = data["transitions"]
    line_list = []
    output_list = []
    # Limpiar input
    with open(file_name, 'r') as archivo:
        for line in archivo:
            line_list.append(line.strip())
    # Realizar el cálculo del input del tape y correr la máquina para cada input
    for i in line_list:
        tape_r = ["X"] + list(itertools.chain(*i)) + ["X"] *50*((len(line_list))*2-2)
        output_list.append(Turing(tape_r, turing_table).run()+'\n')
    # Devolver el archivo con los resultados
    with open('output.txt', 'a') as file:
        file.truncate(0)
        file.writelines(output_list)
        file.close()

# Definir archivos de entrada
tape_entrada = 'data.txt'
reglas_turing = 'configuration.json'
# Correr la función
multiple(tape_entrada, reglas_turing)