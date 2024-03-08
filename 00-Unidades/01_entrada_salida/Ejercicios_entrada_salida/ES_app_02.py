import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)

Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál es el nivel más alcanzado de los jugadores
Informe B- El Porcentaje de jugadores de la categoría principiante sobre el total
Informe C- La categoría del participante de mayor edad
Informe D- El score y nombre del principiante con mayor score
Informe E- Promedio de score de los participantes intermedios.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        # Inicialización de variables y banderas
        nivel1cantidad = 0
        nivel2cantidad = 0
        nivel3cantidad = 0
        totaljugadores = 0
        principiantes = 0
        intermedios = 0
        totalscore = 0
        edad_mayor = 0
        categoria_mayor = ""
        score_max = 0
        nombre_maxscore = ""
        banderamayor = False
        scorebandera = False

        # Ciclo para ingresar datos de los 50 participantes
        for ingresos in range(50):
            nombre = input("Ingrese el nombre del jugador: ")
            categoria = input("Ingrese la categoría (Principiante, Intermedio o Avanzado): ")
            edad = int(input("Ingrese la edad (entre 18 y 99 años): "))
            score = float(input("Ingrese el score (mayor que 0): "))
            nivel_alcanzado = int(input("Ingrese el nivel alcanzado (1, 2 o 3): "))

            # Validaciones
            if 18 <= edad <= 99 and score > 0:
                totaljugadores += 1
                totalscore += score

                # Conteo de niveles
                if nivel_alcanzado == 1:
                    nivel1cantidad += 1
                    if categoria == "Principiante":
                        principiantes += 1
                        if score > score_max or scorebandera == False:
                            score_max = score
                            nombre_maxscore = nombre
                            scorebandera = True
                elif nivel_alcanzado == 2:
                    nivel2cantidad += 1
                    if categoria == "Intermedio":
                        intermedios += 1
                elif nivel_alcanzado == 3:
                    nivel3cantidad += 1

                # Registro de mayor edad
                if edad > edad_mayor or banderamayor == False:
                    edad_mayor = edad
                    categoria_mayor = categoria
                    banderamayor = True
            else:
                print("Datos inválidos. Por favor, ingrese valores válidos.")

        # Informe A - Nivel más alcanzado
        if nivel1cantidad >= nivel2cantidad and nivel1cantidad >= nivel3cantidad:
            nivel_masalcanzado = 1
        elif nivel2cantidad >= nivel3cantidad:
            nivel_masalcanzado = 2
        else:
            nivel_masalcanzado = 3
        print(f"Informe A: El nivel más alcanzado por los jugadores es: {nivel_masalcanzado}")

        # Informe B - Porcentaje de jugadores principiantes
        porcentaje_principiantes = (principiantes / totaljugadores) * 100
        print(f"Informe B: El porcentaje de jugadores principiantes es: {porcentaje_principiantes:.2f}%")

        # Informe C - Categoría del participante de mayor edad
        print(f"Informe C: La categoría del participante de mayor edad es: {categoria_mayor}")

        # Informe D - Score y nombre del principiante con mayor score
        print(f"Informe D: El principiante con mayor score es {nombre_maxscore} con un score de {score_max}")

        # Informe E - Promedio de score de los participantes intermedios
        if intermedios > 0:
            promedio_intermedios_score = totalscore / intermedios
            print(f"Informe E: El promedio de score de los participantes intermedios es: {promedio_intermedios_score:.2f}")
        else:
            print("No hay participantes intermedios para calcular el promedio.")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()