
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


    def btn_calcular_on_click(self):
        import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
'''
Lucila Micaela Suarez
Div E

De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:
Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál es la categoría que tiene menos participantes.
Informe B- El Porcentaje de jugadores de la categoría intermedios sobre el total
Informe C- La categoría del participante de mayor Score.
Informe D- El score y nombre del intermedio con menor score.
Informe E- Promedio de score de los participantes avanzados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):

        contador_principiante = 0
        contador_intermedio = 0
        contador_avanzado = 0
        bandera_mayor = True
        score_mayor = 0
        bandera_menor = True
        score_menor = 0
        acumulador_score = 0


        for ingresos in range (50):
            nombre = prompt ("UTN", "Ingrese su nombre:")

            categoria = prompt ("UTN", "Ingrese su categoria:")
            while categoria != "principiante" and categoria != "intermedio" and categoria != "avanzado":
                categoria = prompt ("Error", "Reingrese categoria:")

            edad = int(prompt ("UTN", "Ingrese edad:"))
            while edad >= 17 or edad <= 99:
                edad = int(prompt("Error", "Reingrese edad"))

            score = int(prompt ("UTN", "Ingrese score"))
            while score < 0:
                score = int(prompt ("Error", "Reingrese score"))

            if score > score_mayor or bandera_mayor == True:
                score_mayor = score
                categoria_mayor = categoria
                bandera_mayor = False

            match categoria:
                case "principiante":
                    contador_principiante +=1
                case "intermedio":
                    contador_intermedio += 1
                    if score < score_menor or bandera_menor == True:
                        score_menor = score
                        nombre_menor = nombre
                        bandera_menor = False
                case "avanzado":
                    contador_avanzado += 1
                    acumulador_score += score

            nivel = int (prompt("UTN", "Ingrese nivel"))
            while nivel != 1 and nivel != 2 and nivel != 3:
                nivel = int (prompt  ("Error", "Reingrese nivel"))

        if contador_avanzado < contador_intermedio and contador_avanzado < contador_principiante:
            menor = "La categoría que tiene menos participantes es avanzado."
        elif contador_intermedio < contador_principiante:
            menor = "La categoria que tiene menos participantes es intermedio"
        else:
            menor = "La categoria que tiene menos participantes es principiante"

        total = contador_avanzado + contador_intermedio + contador_principiante
        porcentaje = (contador_intermedio * 100) / total

        promedio = acumulador_score / contador_avanzado

        print (menor)
        print (f"El Porcentaje de jugadores de la categoría intermedios es : {porcentaje}%")
        print (f"La categoría del participante de mayor Score: {categoria_mayor}")
        print (f"El score y nombre del intermedio con menor score: {nombre_menor} score: {score_menor}")
        print (f"Promedio de score de los participantes avanzados: {promedio}")

if __name__ == "__main__": 
    app = App()
    app.geometry("300x300")
    app.mainloop()

    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()