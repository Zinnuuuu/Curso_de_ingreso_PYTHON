import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
Simulacro Turno Tarde

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)


No sabemos cuántos clientes serán consultados. (uso de while..)

Se debe informar al usuario:

El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

El porcentaje de clientes que asiste solo 1 día a la semana.

Nombre y edad del cliente con más altura.

Determinar si los clientes eligen más ir 1, 3 o 5 días

Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        seguir = True

        nivel1cantidad = 0
        nivel2cantidad = 0
        nivel3cantidad = 0
        totaljugadores = 0
        
        nivel_masalcanzado = 0

        principiantes = 0
        porcentaje_principiante = 0

        intermedios = 0
        promedio_intermedios_score = 0
        total_score_intermedios = 0

        banderamayor = False
        edad_mayor = 0
        categoria_mayor = ""

        scorebandera = False
        score_max = 0
        nombre_maxscore = ""

        vueltas = 1

        
        for ingresos in range (vueltas):
            while seguir:
                nombre = input("Ingrese su nombre :")

                categoria = input ("Ingrese su categoria:")
                while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                    categoria = input ("Reingrese categoria:")

                edad = int(input("Ingrese una edad (entre 18 y 99) :"))
                while edad < 18 or edad > 99 :
                        edad = int(input("Reingrese una edad válida: "))

                score = int(input("Ingrese un puntaje: "))
                while score < 1:
                        score = int(input("Reingrese un puntaje válido: "))

                nivel_alcanzado = int (input("Ingrese nivel"))
                while nivel_alcanzado  != 1 and nivel_alcanzado != 2 and nivel_alcanzado != 3:
                        nivel_alcanzado = int (input  ("Reingrese nivel"))
        
                if nivel_alcanzado == 1:
                    nivel1cantidad += 1
                elif nivel_alcanzado == 2:
                    nivel2cantidad += 1
                else:
                    nivel3cantidad += 1
                
                if categoria == "Principiante" :
                    principiantes += 1
                elif categoria == "Intermedio":
                    intermedios += 1
                    total_score_intermedios += score

                if edad > edad_mayor or banderamayor == False:
                    edad_mayor = edad
                    categoria_mayor = categoria
                    banderamayor = True
            
                if categoria == "Principiante" and (score > score_max or scorebandera == False):
                    score_max = score
                    nombre_maxscore = nombre   
                    scorebandera = True

            seguir = question("", "¿Desea añadir otro participante?")
        
        totaljugadores = nivel1cantidad + nivel2cantidad + nivel3cantidad
        if totaljugadores > 0:
            porcentaje_principiante = round(principiantes / totaljugadores * 100)

        if intermedios > 0:
            promedio_intermedios_score = total_score_intermedios / intermedios

        nivel_masalcanzado = max(nivel1cantidad, nivel2cantidad, nivel3cantidad)

        print(f"El nivel más alcanzado por los jugadores es el {nivel_masalcanzado}")
        print(f"El porcentaje de jugadores de la categoría principiante sobre el total es del {porcentaje_principiante}%")
        print(f"La categoría del participante de mayor edad es {categoria_mayor}")
        print(f"{nombre_maxscore} tiene el puntaje más alto con {score_max}")
        print(f"El promedio de puntaje de los participantes intermedios es de {promedio_intermedios_score}.")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()