import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÁXIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]

    ''' 
    Bruno Condarco
    DivisionE 
    47230703

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

    def btn_calcular_on_click(self):
        seguir = True

        nivel1cantidad = 0
        nivel2cantidad = 0
        nivel3cantidad = 0
        totaljugadores = 0

        principiantes = 0
        intermedios = 0
        total_score_intermedios = 0

        banderamayor = False
        edad_mayor = 0
        categoria_mayor = ""

        scorebandera = False
        score_max = 0
        nombre_maxscore = ""

        for i in range (2):
            nombre = input("Ingrese su nombre :")

            categoria = input ("Ingrese su categoria:")
            while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                categoria = input ("Reingrese categoria:")

            edad = int (input("Ingrese una edad (entre 18 y 99) :"))
            while edad < 18 or edad > 99 :
                    edad = int (input("Reingrese una edad válida: "))

            score = int( input ("Ingrese un puntaje: "))
            while score < 1:
                    score = int( input("Reingrese un puntaje válido: "))

            nivel_alcanzado = int(  input("Ingrese nivel"))
            while nivel_alcanzado  != 1 and nivel_alcanzado != 2 and nivel_alcanzado != 3:
                    nivel_alcanzado = int (input ("Reingrese nivel"))
    
            if nivel_alcanzado == 1:
                nivel1cantidad += 1
            elif nivel_alcanzado == 2:
                nivel2cantidad += 1
            else:
                nivel3cantidad += 1
            
            if categoria == "Principiante" :
                principiantes += 1
                if score > score_max or scorebandera == False:
                    score_max = score
                    nombre_maxscore = nombre  
                    scorebandera = True

            elif categoria == "Intermedio":
                intermedios += 1
                total_score_intermedios += score

            if edad > edad_mayor or banderamayor == False:
                edad_mayor = edad
                categoria_mayor = categoria
                banderamayor = True

        
            seguir = question("","¿Desea añadir otro participante?")
            if not seguir:
                break
    
                
        
        totaljugadores = nivel1cantidad + nivel2cantidad + nivel3cantidad
        if totaljugadores > 0:
            porcentaje_principiante = round(principiantes / totaljugadores * 100)

        if nivel1cantidad > nivel2cantidad and nivel1cantidad > nivel3cantidad:
            nivel_masalcanzado = 1
        elif nivel2cantidad > nivel3cantidad:
            nivel_masalcanzado = 2
        else:
            nivel_masalcanzado = 3

        print(f"El nivel más alcanzado por los jugadores es el {nivel_masalcanzado}")
        print(f"El porcentaje de jugadores de la categoría principiante sobre el total es del {porcentaje_principiante}%")
        print(f"La categoría del participante de mayor edad es {categoria_mayor}")
        print(f"{nombre_maxscore} es el principiante que tiene el puntaje más alto con {score_max}")
        if intermedios > 0:
            promedio_intermedios_score = total_score_intermedios / intermedios
            print(f"El promedio de puntaje de los participantes intermedios es de {promedio_intermedios_score}.")
        else:
            print("No hay participantes intermedios para calcular el promedio.")


App().mainloop()
