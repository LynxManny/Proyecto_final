import tkinter as tk
from tkinter import messagebox, simpledialog
import os

ARCHIVO = "palabras_ahorcado.txt"

#  VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Ahorcado Completo")
ventana.configure(bg="blue")
ventana.geometry("550x600")
ventana.resizable(True, True)

# VARIABLES GLOBALES
palabra_secreta = ""
progreso = []
letras_usadas = set()
errores = 0
max_errores = 6

# CUADRO DE DIBUJO
canvas = tk.Canvas(ventana, width=250, height=310, bg="lightgray")
canvas.pack(padx=10, pady=10)

def nuevo_juego():
    global palabra_secreta, progreso, letras_usadas, errores

    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, "w").close()

    with open(ARCHIVO, "r") as f:
        palabras = f.read().splitlines()

    if not palabras:
        messagebox.showwarning("Sin palabras", "No hay palabras en la lista.")
        return

    import random
    palabra_secreta = random.choice(palabras)
    progreso = ["_"] * len(palabra_secreta)
    letras_usadas = set() # Reinicia las letras usadas
    errores = 0

    actualizar_pantalla() # Actualiza la interfaz
    dibujar_horca_y_cuerpo() # Dibuja la horca sin cuerpo


def agregar_palabra():
    if not os.path.exists(ARCHIVO):
        open(ARCHIVO, "w").close()

    nueva = simpledialog.askstring("Agregar palabra", "Escribe la palabra:").lower() # Solicita nueva palabra

    if not nueva or not nueva.isalpha(): # Validación de palabra
        messagebox.showerror("Error", "La palabra solo debe contener letras.") # Muestra error si la palabra no es válida
        return

    with open(ARCHIVO, "r") as f: # Lee el archivo para verificar duplicados
        lista = f.read().splitlines() # Lista de palabras existentes

    if nueva in lista:
        messagebox.showinfo("Duplicada", "La palabra ya existe.")
        return

    with open(ARCHIVO, "a") as f: # Abre el archivo para agregar la nueva palabra
        f.write(nueva + "\n") # Agrega la nueva palabra al archivo

    messagebox.showinfo("OK", "Palabra agregada correctamente.") # Confirma que la palabra fue agregada


def borrar_lista():
    if os.path.exists(ARCHIVO): # Verifica si el archivo existe
        open(ARCHIVO, "w").close() # Borra el contenido del archivo
        messagebox.showinfo("Borrado", "La lista de palabras ha sido borrada.")


def mostrar_lista():
    if not os.path.exists(ARCHIVO):
        messagebox.showwarning("Sin archivo", "No existe archivo de palabras.") # Muestra advertencia si no hay archivo
        return

    with open(ARCHIVO, "r") as f:   # Lee el archivo para mostrar la lista
        lista = f.read().splitlines() # Lee las palabras del archivo

    if not lista:
        messagebox.showinfo("Lista vacía", "No hay palabras registradas.") # Muestra mensaje si la lista está vacía
    else:
        messagebox.showinfo("Lista de palabras", "\n".join(lista))  # Muestra la lista de palabras


def salir():
    ventana.destroy()


def intentar_letra(): # Maneja el intento de adivinar una letra
    global errores

    letra = entrada_letra.get().lower() # Obtiene la letra ingresada y la convierte a minúsculas
    entrada_letra.delete(0, tk.END) # Limpia el campo de entrada

    if len(letra) != 1 or not letra.isalpha():  # Validación de entrada
        messagebox.showwarning("Error", "Solo ingrese UNA letra válida.")   # Muestra advertencia si la entrada no es válida
        return

    if letra in letras_usadas:  # Verifica si la letra ya fue usada
        messagebox.showinfo("Aviso", "Ya usaste esa letra.")    # Muestra aviso si la letra ya fue usada
        return

    letras_usadas.add(letra)    # Agrega la letra a las usadas

    if letra in palabra_secreta:
        for i, c in enumerate(palabra_secreta): # Actualiza el progreso si la letra es correcta
            if c == letra:
                progreso[i] = letra
    else:
        errores += 1  # Incrementa errores si la letra no está en la palabra

    actualizar_pantalla()   # Actualiza la interfaz
    dibujar_horca_y_cuerpo()  # Dibuja la horca y el cuerpo según errores

    if "_" not in progreso: # Verifica si el jugador ha ganado
        messagebox.showinfo("Ganaste :)", "¡Has adivinado la palabra!")    # Muestra mensaje de victoria
    elif errores >= max_errores:
        messagebox.showerror("Perdiste :(", f"La palabra era: {palabra_secreta}") # Muestra mensaje de derrota


def actualizar_pantalla(): # Actualiza las etiquetas de la interfaz
    palabra_label.config(text=" ".join(progreso))   # Actualiza la palabra mostrada
    letras_usadas_label.config(text="Letras usadas: " + ", ".join(sorted(letras_usadas)))  # Actualiza las letras usadas mostradas
    intentos_label.config(text=f"Errores: {errores} / {max_errores}")  # Actualiza el contador de errores

# DIBUJA HORCA Y CUERPO 
def dibujar_horca_y_cuerpo(): # Dibuja la horca y el cuerpo según el número de errores
    canvas.delete()    # Limpia el canvas antes de dibujar

    # Horca
    canvas.create_line(40, 300, 200, 300, width=4)  # Base
    canvas.create_line(50, 100, 120, 50, width=4)   # Soporte diagonal
    canvas.create_line(50, 300, 50, 50, width=6)    # Poste
    canvas.create_line(50, 50, 150, 50, width=6)    # Travesaño
    canvas.create_line(150, 50, 150, 80, width=3)   # Cuerda

    # Cuerpo según errores
    if errores >= 1:
        canvas.create_oval(125, 80, 175, 130, width=3)  # Cabeza
    if errores >= 2:
        canvas.create_line(150, 130, 150, 215, width=3)  # Cuerpo
    if errores >= 3:
        canvas.create_line(150, 150, 115, 180, width=3)  # Brazo izq
    if errores >= 4:
        canvas.create_line(150, 150, 185, 180, width=3)  # Brazo der
    if errores >= 5:
        canvas.create_line(150, 215, 120, 265, width=3)  # Pierna izq
    if errores >= 6:
        canvas.create_line(150, 215, 180, 265, width=3)  # Pierna der

# AREA DE LETRAS ACERTADAS
palabra_label = tk.Label(ventana, text="", font=("Arial", 24), bg="lightblue")
palabra_label.pack(pady=10)

# AREA DE INTENTOS Y ERRORES
intentos_label = tk.Label(ventana, text="Errores: 0 / 6", bg="lightgreen")
intentos_label.pack()

# AREA DE LETRAS USADAS
letras_usadas_label = tk.Label(ventana, text="Letras usadas: " , bg="pink")
letras_usadas_label.pack(pady=5)

# AREA DE ESCRIBIR LETRA
entrada_letra = tk.Entry(ventana, font=("Arial", 18), width=5, bg="violet", justify="center")
entrada_letra.pack(pady=5)

# BOTON PARA INTENTAR LETRA
btn_letra = tk.Button(ventana, text="Intentar letra", command=intentar_letra, bg="orange", width=15)
btn_letra.pack(pady=5)

btn_frame = tk.Frame(ventana)
btn_frame.pack(pady=12)

tk.Button(btn_frame, text="Nuevo juego", command=nuevo_juego, width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Agregar palabra", command=agregar_palabra, width=12).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Mostrar lista", command=mostrar_lista, width=12).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Borrar lista", command=borrar_lista, width=12).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Salir", command=salir, width=12).grid(row=0, column=4, padx=5)

ventana.mainloop()
