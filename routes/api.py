from flask import Blueprint, render_template, request
from collections import deque

api = Blueprint("main", __name__)

def encontrar_ruta(matriz, inicio, fin):
    N, M = len(matriz), len(matriz[0])
    casilla_usada = [[False] * M for _ in range(N)]
    padres = {}
    queue = deque()
    queue.append(inicio)
    casilla_usada[inicio[0]][inicio[1]] = True
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        fila, col = queue.popleft()

        if (fila, col) == fin:
            ruta = []
            actual = fin
            while actual != inicio:
                ruta.append(actual)
                actual = padres[actual]
            ruta.append(inicio)
            ruta.reverse()
            return ruta
        actual_valor = matriz[fila][col]
        for dx, dy in movimientos:
            nx, ny = fila + dx, col + dy
            if 0 <= nx < N and 0 <= ny < M and not casilla_usada[nx][ny]:
                siguiente_valor = matriz[nx][ny]
                if actual_valor % siguiente_valor == 0:
                    padres[(nx, ny)] = (fila, col)
                    queue.append((nx, ny))
                    casilla_usada[nx][ny] = True
    return None

@api.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        matriz_capturada = request.form["matriz"]
        inicio = request.form["inicio"]
        fin = request.form["fin"]
        try:
            filas_raw = matriz_capturada.strip().split("\\n")
            matriz = []
            for fila in filas_raw:
                numeros = fila.strip().split()
                valores_filas = []
                for num in numeros:
                    valor = int(num)
                    #en caso de que se ingresen numeros negativos
                    if valor <= 0: 
                        raise ValueError("por favor solo usar numeros positivos.")
                    valores_filas.append(valor)
                matriz.append(valores_filas)
        except Exception as e: 
            return render_template("form.html", error=f"matriz erronea: {str(e)}")
        #validamos el tamaño de la fila
        if len(matriz) == 0 or any(len(fila) != len(matriz[0]) for fila in matriz):
            return render_template("form.html", error="las filas no son iguales.")  
        #validamos el maximo de 10x10
        if len(matriz) > 10 or len(matriz[0]) > 10:
            return render_template("form.html", error="el tamaño maximo permitido es de 10x10 cuadrados") 
        try:
            fila_inicio, col_inicio = map(int, inicio.strip().split(","))
            fila_fin, col_fin = map(int, fin.strip().split(","))
            #validamos que ambas coordenadas sean del formato
        except:
            return render_template("form.html", error="Coordenadas inválidas (ej: 0,0)") 
        #validamos que las coordenadas esten dentro de la matriz
        if not (0 <= fila_inicio < len(matriz) and 0 <= col_inicio < len(matriz[0])):
            return render_template("form.html", error="Las coordenadas estan fuera del rango permitido") 
        if not (0 <= fila_fin < len(matriz) and 0 <= col_fin < len(matriz[0])):
            return render_template("form.html", error="Las coordenadas estan fuera del rango permitido")
        ruta = encontrar_ruta(matriz, (fila_inicio, col_inicio), (fila_fin, col_fin))
        return render_template(
            "resultado.html",
            matriz=matriz,
            ruta=ruta,
            inicio=(fila_inicio, col_inicio),
            fin=(fila_fin, col_fin)
        )

    return render_template("form.html", error=None)
