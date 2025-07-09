# 🧩 Enigma del Laberinto Numérico

Este proyecto es una aplicación web desarrollada con Flask, permite al usuario ingresar una matriz numérica en un array e identificar una ruta válida desde un punto A un B. La ruta solo puede seguir casillas adyacentes segun la logica requerida.

---

## 🚀 ¿Cómo funciona?

1) Se ingresa una matriz de enteros separada por espacios y saltos de línea (`\n`).
2) ingresa las coordenadas de inicio y fin.
3) El codigo busca una ruta válida usando BFS, cumpliendo la condición de divisibilidad.
4) Si se llega a encuentrar una ruta, esta se muestra visualmente en una tabla junto a un listado paso a paso.

---

## 💻 Tecnologías utilizadas

 Python 3.12.8
 Flask
 Bootstrap 5
 HTML + Jinja2

---


## 🧪 Validaciones implementadas

✅ Solo se permiten enteros positivos  
✅ Todas las filas deben tener la misma cantidad de columnas  
✅ Tamaño máximo: 10x10  
✅ Coordenadas deben estar dentro del rango
✅ Formato correcto para coordenadas (`fila,columna`)  

---

## 📝 Ejemplo de entrada

Matriz: 64 32 16 8
99 99 99 4
99 99 99 2
99 99 99 1
Inicio: `0,0`  
Fin: `3,3`  
➡️ Ruta válida: sí

---

recuerda instalar Flask (pip install flask) y correr el archivo con python app.py



