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

        self.label1 = customtkinter.CTkLabel(master=self, text="Nombre")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_nombre = customtkinter.CTkEntry(master=self)
        self.txt_nombre.grid(row=0, column=1)
        
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True
        
        nivel_1_cantidad = 0
        nivel_2_cantidad = 0
        nivel_3_cantidad = 0
        total_jugadores = 0
        principiante = 0
        intermedio = 0
        total_score_intermedio = 0
        bandera_mayor = False
        categoria_mayor = ""
        edad_mayor = 0
        bandera_score_max = False
        score_max = 0
        nombre_max_score = ""
        

        for i in range (50):
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
                nivel_1_cantidad += 1
            elif nivel_alcanzado == 2:
                nivel_2_cantidad += 1
            else:
                nivel_3_cantidad += 1
            
            if categoria == "Principiante" and score > score_max or bandera_score_max == False:
                score_max = score
                nombre_max_score = nombre
                principiante += 1
                bandera_score_max = True
            elif categoria == "Intermedio":
                intermedio += 1
                total_score_intermedio += score
            
            if edad > edad_mayor or bandera_mayor == False:
                edad_mayor = edad
                categoria_mayor = categoria
                bandera_mayor = True

            seguir = question("","Desea seguir?")
            if not seguir:
                break
        
        total_jugadores = nivel_1_cantidad + nivel_2_cantidad + nivel_3_cantidad
        porcentaje_principiantes = round(principiante / total_jugadores * 100)


        if nivel_1_cantidad > nivel_3_cantidad and nivel_1_cantidad > nivel_2_cantidad:
            nivel_mas_concurrido = 1
        elif nivel_2_cantidad > nivel_3_cantidad:
            nivel_mas_concurrido = 2
        else:
            nivel_mas_concurrido = 3
        
        print(f"El nivel mas alcanzado por los jugadores es el {nivel_mas_concurrido}")
        print(f"El porcentaje de los principiantes sobre el total es de {porcentaje_principiantes}%")
        print(f"{categoria_mayor} es la categoria del participante de mayor edad con {edad_mayor} años")
        print(f"{nombre_max_score} es la persona con mas score con {score_max} en categoria principiantes")
        if intermedio > 0:
            promedio_score_intermedio = total_score_intermedio / intermedio
            print(f"El promedio de score de los participantes intermedios es de {promedio_score_intermedio:.2f}")
        else:
            print(f"No hay jugadores intermedios para promediar")


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()