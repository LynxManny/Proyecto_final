import tkinter as tk
from tkinter import messagebox

    #CREACION DE LA VENTANA PRINCIPAL
ventana = tk.Tk()
ventana.title("Ahorcado - Layout")
ventana.configure(bg="green")
ventana.geometry("400x450")
ventana.resizable(False, False)

    #FUNCIONES DE LOS BOTONES
        #INICIAR NUEVO JUEGO
def nuevo_juego():
    messagebox.showinfo("Lista vacía", "La lista esta vacia. No hay palabras guardadas aún.")
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

        #AGREGA LA PALABRA A LA LISTA
def agregar_palabra():
    messagebox.showinfo("Agregar", "Agrega las palabras.")
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

        #MUESTRA LA LISTA DE PALABRAS
def mostrar_lista():
    messagebox.showinfo("Mostrar", "Estas son las palabras guardadas.")
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

        #SALIR DEL JUEGO
def salir():
    messagebox.showinfo("Salida", "Gracias por jugar")
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)


        #DIBUJA LA HORCA Y EL MUÑECO QUE SE DIBUJARA SEGUN ERRORES
def dibujar_horca(canvas):
    canvas.pack(padx=10, pady=10)
    canvas.create_line(40, 300, 200, 300, width=4) # Base
    canvas.create_line(50, 100, 120, 50, width=4) # soporte diagonal
    canvas.create_line(50, 300, 50, 50, width=6) # Poste
    canvas.create_line(50, 50, 150, 50, width=6) # Travesaño
    canvas.create_line(150, 50, 150, 80, width=3) # Cuerda
    canvas.create_oval(125, 80, 175, 130, width=3) # Cabeza
    canvas.create_line(150, 130, 150, 215, width=3) # Cuerpo
    canvas.create_line(150, 150, 115, 180, width=3) # Brazo izquierdo
    canvas.create_line(150, 150, 185, 180, width=3) # Brazo derecho
    canvas.create_line(150, 215, 120, 265, width=3) # Pierna izquierda
    canvas.create_line(150, 215, 180, 265, width=3) # Pierna derecha   


dibujar_horca(canvas=tk.Canvas(ventana, width=300, height=350, bg="white"))

    #ETIQUETAS Y BOTONES
letras_usadas_label = tk.Label(ventana, text="Letras usadas: ")
letras_usadas_label.pack(pady=(0, 6))
btn_frame = tk.Frame(ventana)
btn_frame.pack(pady=6)

    #BOTONES DE ACCION
btn_nuevo = tk.Button(btn_frame, text="Nuevo juego", command=nuevo_juego, width=12).grid(row=0, column=0, padx=5)
btn_agregar = tk.Button(btn_frame, text="Agregar lista", command=agregar_palabra, width=12).grid(row=0, column=1, padx=5)
btn_mostrar = tk.Button(btn_frame, text="Mostrar lista", command=mostrar_lista, width=12).grid(row=0, column=2, padx=6)
btn_salir = tk.Button(btn_frame, text="Salir", command=salir, width=12).grid(row=0, column=3, padx=6) #command=ventana.destroy


ventana.mainloop()