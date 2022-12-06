"""
Harold David Guerrero Caicedo
8976203
Noviembre 22/2022
Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
Entrega 4 Proyecto Introducción a la Programación
https://onlinejudge.org/external/4/449.pdf
"""

### Función majoringScale
### Entrada:
### Salida:
### Descripción general: Se lee la entrada y separa los intervalos por el ;.
def majoringScale():
    scale = input()
    while scale != "":
        interval = input()
        list_intervals = interval.split(";")
        solutionMajorScale(scale, list_intervals)

        scale = input()

### Función createMajorScale
### Entrada: Recibe scale, la cual se digita por medio de un input.
### Salida: list_exit lista creada según donde este la escala. La crea con ayuda de la tupla progression.
### Descripción general: Operación que crea la lista de major scale, la cual se retorna en list_scale.
def createMajorScale(scale):
    list_scales = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    list_scales2 = ["B#", "Db", "D", "Eb", "Fb", "E#", "Gb", "G", "Ab", "A", "Bb", "Cb"]
    val = -1
    sc = None
    if scale in list_scales:
        val = list_scales.index(scale)
        list_exit = [(list_scales[val], list_scales2[val])]
        sc = True
    else:
        val = list_scales2.index(scale)
        list_exit = [(list_scales[val], list_scales2[val])]
        sc = False
    progression = ("tone", "tone", "semitone", "tone", "tone", "tone", "semitone")

    for i in progression:
        if i == "tone":
            if val == 11:
                val = 1
            elif val == 10:
                val = 0
            else:
                val += 2
            if "#" in list_scales2[val] and scale != "Ab" and scale != "Bb" and scale != "Db" and scale != "Eb" and (
                    "C" in list_scales[val]):
                list_exit.append((list_scales[val], list_scales2[val]))
            elif "b" in list_scales2[val] and (
                    "E" in list_scales[val] or "B" in list_scales[val] or "D#" in list_scales[val] or "G#" in
                    list_scales[val] or "A#" in list_scales[val] or "F#" in list_scales[val] or "C#" in list_scales[
                        val]):
                list_exit.append((list_scales[val], list_scales2[val]))
            else:
                list_exit.append((list_scales2[val], list_scales[val]))

        elif i == "semitone":
            if val == 11:
                val = 0
            else:
                val += 1
            if "b" in list_scales2[val] and scale != "F" and (
                    "E" in list_scales[val] or "B" in list_scales[val] or "F#" in list_scales[val] or "C#" in
                    list_scales[val] or "G#" in list_scales[val] or "D#" in list_scales[val] or "A#" in list_scales[
                        val]):
                list_exit.append((list_scales[val], list_scales2[val]))
            elif "#" in list_scales2[val] and ("F" in list_scales[val] or "C" in list_scales[val]):
                list_exit.append((list_scales[val], list_scales2[val]))
            else:
                list_exit.append((list_scales2[val], list_scales[val]))

    return list_exit

### Función solutionMajorScale
### Entrada: recibe la escala (scale) y la lista de intervalos correspondientes al scale.
### Salida: Sale el intervalo gracias a la operación calculate.
### Descripción general: imprime el intervalo con ayuda de la operación calculate.
def solutionMajorScale(scale, interval):
    listExit = createMajorScale(scale)
    print("Key of " + scale)
    for each_interval in interval:
        calculate(each_interval, listExit, scale)
    print()

### Función calculate.
### Entrada: recibe cada intervalo de la escala, la lista que se crea en listExit, que hace referencia a las major scales de la escala correspondiente y la escala correspondiente.
### Salida: imprime la escala final correspondiente después de haberla calculado.
### Descripción general: Se encarga de calcular en qué escala quedará según la dirección (UP, DOWN) y los movimientos calculados en la operación n_steps.
def calculate(each_interval, listExit, scale):
    start, direction, moves = each_interval.split(" ")
    j = None
    for i in range(len(listExit)):
        if "b" in scale:
            if listExit[i][1] == start:
                j = i
        else:
            if listExit[i][0] == start:
                j = i
    value = n_steps(moves)
    if j == None:
        print(start + ": invalid note for this key")
    else:
        if direction == "DOWN":
            if "b" in scale:
                opIndexDown = ((j - value) % 7)
                a = listExit[opIndexDown][1]
            else:
                opIndexDown = ((j - value) % 7)
                a = listExit[opIndexDown][0]

        elif direction == "UP":
            if "b" in scale:
                opIndexUp = ((j + value) % 7)
                a = listExit[opIndexUp][1]
            else:
                opIndexUp = ((j + value) % 7)
                a = listExit[opIndexUp][0]

        print(start + ":", direction, moves, ">", a)

### Función n_steps
### Entrada: move que serian los espacios o pasos que se debe de mover la nota indicada.
### Salida: Los pasos que se va a mover.
### Descripción general: Esta función indica la cantidad de espacios o pasos que debe moverse la nota indicada para llegar a una nota final, segun lo que se encuentre en move.
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


majoringScale()

