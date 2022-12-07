"""
Harold David Guerrero Caicedo
8976203
Noviembre 6/2022
Entrega 3 Proyecto Introducción a la Programación
https://onlinejudge.org/external/4/449.pdf
"""


### Se hace una función solutionMajorScale la cual recibe una scale y un interval. Haremos uso de esta función para leer los datos.
### Entrada: En el input recibiremos un scale y un interval. 
### Salida:
def solutionMajorScale(scale, interval):
    list_intervals = interval.split(";")
    print("DATOS LEIDOS")
    print(scale)
    print(interval)
    print("Lista de majoring scale")
    print(list_intervals)
    list_scales = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    list_scales2 = ["B#", "Db", "D", "Eb", "Fb", "E#", "Gb", "G", "Ab", "A", "Bb", "Cb"]

def majoringScale():
    scale = input()
    while scale != "":
        interval = input()
        solutionMajorScale(scale, interval)
        scale = input()

### Se hace una operación calculate la cual se usa para saber en que posición quedara la escala (scale)
### Entrada: dos listas que contienen las escalas, llamadas como: list_scale y list_scales2, también recive interval, la cual la separe con .spli para poder guardar en variables cada posición.
### Salida: Sale la escala en la cual debe de quedar.

def calcualate(list_scales, list_scales2, scale, interval):
    start, direction, moves = interval.split(" ")
    i = 0
    while (list_scales[i] != start) and (list_scales2[i] != start):
        i += 1
    if direction == "UP":
        i += n_steps(moves)

    elif direction == "DOWN":
        i -= n_steps(moves)
    print(i)
    print(start)
    if start in list_scales:
        print(list_scales)
    else:
        print(list_scales2[i])

### Se hace una aperacion n_steps
### Entrada: moves, variable a la cual se le asigna cuantos pasos quiere recorrer.
### Salida: Sale una variable, en este caso la variable move, esta contiene el numero de movientos y esto depende de cuantos movientos nos pide la entrada. 
def n_steps(move):
    steps = 0
    if move == "SECOND":
        steps = 1
    if move == "THIRD":
        steps = 2
    if move == "FOURTH":
        steps = 3
    if move == "FIFTH":
        steps = 4
    if move == "SIXTH":
        steps = 5
    if move == "SEVENTH":
        steps = 6
    if move == "OCTAVE":
        steps = 7
    return steps
calcualate(["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"], ["B#", "Db", "D", "Eb", "Fb", "E#", "Gb", "G", "Ab", "A", "Bb", "Cb"], "C", "B UP SECOND")
#majoringScale()