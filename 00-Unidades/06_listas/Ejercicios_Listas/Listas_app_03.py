import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

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

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="MÁXIMO", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [1,80,5,0,15,-5,1,79]


    def btn_calcular_on_click(self):
        seguir = True

        nivel1cantidad = 0
        nivel2cantidad = 0
        nivel3cantidad = 0
        totaljugadores = 0
        
        nivel_masalcanzado = 0

        principíantes =0
        porcentaje_principiante = 0

        intermedios = 0
        promedio_intermedios_score = 0
        totalscore = 0
        banderamayor = False
        edad_mayor = 0
        categoria_mayor = ""

        scorebandera = False
        score_max = 0
        nombre_maxscore = ""

        
        for ingresos in range (50):
            while seguir:
                nombre = input("Ingrese su nombre :")

                categoria = (input("Ingrese una categoria (Principiante , Intermedio o Avanzado) :"))
                while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                    categoria = (input( "Reingrese una categoria"))

                edad = int (input("Ingrese una edad (entre 18 y 99) :"))
                while edad < 18 and edad > 99 :
                    edad = int(input( "Reingrese una edad"))

                score = int (input("Ingrese un score"))
                while score < 1:
                    score = int(input( "Reingrese un score"))

                nivel_alcanzado = int (input("Ingrese un nivel alcanzado (1 , 2 o 3)"))
                while nivel_alcanzado != 1 and nivel_alcanzado != 2 and nivel_alcanzado != 3:
                    nivel_alcanzado = int(input( "Reingrese un nivel"))

            if nivel_alcanzado == 1:
                nivel1cantidad += 1
            elif nivel_alcanzado == 2:
                nivel2cantidad += 1
            else:
                nivel3cantidad += 1
                
            if categoria == "Principiante":                             #El Porcentaje de jugadores de la categoría principiante sobre el total
                pricipíantes += 1
            elif categoria == "Intermedio":
                intermedios += 1
                totalscore += score

            if edad > edad_mayor or banderamayor == False:           #La categoría del participante de mayor edad   
                edad_mayor = edad
                categoria_mayor = categoria
                banderamayor = True
            
            if score > score_max or scorebandera == False:           #El score y nombre del principiante con mayor score
                score_max = score
                nombre_maxscore = nombre   
                scorebandera = True



            seguir = question ("", "Desea añadir otro participante ?")
        
        totaljugadores = nivel1cantidad + nivel2cantidad + nivel3cantidad
        if principíantes > 0:
            porcentaje_principiante = round(pricipíantes / totaljugadores * 100)

        if intermedios > 0:                                                           #Promedio de score de los participantes intermedios.
            promedio_intermedios_score = totalscore / intermedios

        if nivel3cantidad > nivel2cantidad and nivel3cantidad > nivel1cantidad :                #Informe A- Cuál es el nivel más alcanzado de los jugadores
            nivel_masalcanzado = 3
        elif nivel2cantidad > nivel1cantidad:
            nivel_masalcanzado = 2
        else:
            nivel_masalcanzado = 1
        


        print(f"El nivel mas alcanzado por los jugadores es el {nivel_masalcanzado}")
        print(f"El Porcentaje de jugadores de la categoría principiante sobre el total es de {porcentaje_principiante}%")
        print(f"La categoría del participante de mayor edad es {categoria_mayor}")
        print(f"{nombre_maxscore} es el nombre del participante con mayor score con {score_max}")
        print(f"El promedio de score de los participantes intermedios es de {promedio_intermedios_score}.")



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()