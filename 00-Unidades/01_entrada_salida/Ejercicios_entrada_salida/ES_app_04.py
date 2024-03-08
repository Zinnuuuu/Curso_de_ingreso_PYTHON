import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Bruno condarco 
47230703
DIV E
De los 11 Jugadores de fútbol se debe ingresar los siguientes datos:
Nombre
Categoría (amateur - profesional - retirado )
Edad (entre 18 y 99 inclusive)
goles puede ser cero
Número de camiseta del 0 al 100
Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál hay más , mayores a 25 años o menores
Informe B- El Porcentaje de jugadores con más de dos goles
Informe C- El nombre y número del jugador de la categoría retirado más joven
Informe D- los goles y nombre del profesional con más goles
Informe E- Promedio de goles de los jugadores mayores a 25.

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
        mayores_25 = 0
        menores_25 = 0
        total_goles_mayores_25 = 0
        jugadores_mas_dos_goles = 0
        total_jugadores = 0
        retirado = 0
        profesional = 0
        amateur = 0
        bandera_retirado_joven = False
        numero_camiseta_joven = 0
        nombre_joven = ""
        edad_joven = 0
        bandera_profesional = False
        goles_max_profesional = 0
        nombre_max_goles_profesional = ""

        
        for i in range (11):
            
            nombre = prompt ("","Ingrese su nombre :")

            categoria = prompt ("","Ingrese su categoria (amateur , profesional o retirado):")
            while categoria != "amateur" and categoria != "profesional" and categoria != "retirado":
                categoria = prompt ("","Reingrese categoria:")

            edad = int (prompt("","Ingrese una edad (entre 18 y 99) :"))
            while edad < 18 or edad > 99 :
                    edad = int (prompt ("","Reingrese una edad válida: "))

            goles = int (prompt ("","Ingrese la cantidad de goles que hizo en su carrera"))
            while goles < 0:
                goles = int(prompt("","Reingrese los goles"))
            
            numero_camiseta = int(prompt("","Ingrese el numero de su camiseta (0, 100)"))
            while numero_camiseta < 0 or numero_camiseta > 100:
                numero_camiseta = int(prompt("","Reingrese el numero de su camiseta"))

            if edad > 25:
                mayores_25 += 1
                total_goles_mayores_25 += goles
            else:
                menores_25 += 1
            
            if categoria == "retirado" and edad < edad_joven or bandera_retirado_joven == False:
                retirado += 1
                numero_camiseta_joven = numero_camiseta
                nombre_joven = nombre
                edad_joven = edad
                bandera_retirado_joven = True
            elif categoria == "profesional" :
                profesional += 1 
            else:
                amateur += 1

            if goles > goles_max_profesional or bandera_profesional == False:
                goles_max_profesional = goles
                nombre_max_goles_profesional = nombre
                bandera_profesional = True

            if goles > 2:
                jugadores_mas_dos_goles += 1
            
            seguir = question("","Desea añadir otra camiseta ?")
            if not seguir:
                break 
        
        total_jugadores = retirado + profesional + amateur
        porcentaje_jugadores_mas_dos_goles = (jugadores_mas_dos_goles / total_jugadores) * 100
        
        if mayores_25 > menores_25:
            edad_mas_alcanzada = "mayores a 25"
        else:
            edad_mas_alcanzada = "menores a 25"
        
        
        
        print(f"En el plantel hay mas jugadores {edad_mas_alcanzada} años")
        print(f"El porcentaje de jugadores con mas de dos goles es de {porcentaje_jugadores_mas_dos_goles:.2f}%")
        if categoria == "retirado":
            print(f"{nombre_joven} con la {numero_camiseta_joven} es el jugador de la categoria retirado mas joven con {edad_joven}")
        else:
            print("No hay jugadores retirados")
        if categoria =="profesional":
            print(f"{nombre_max_goles_profesional} es el profesional con mas goles con {goles_max_profesional} goles")
        else:
            print("No hay jugadores profesionales")
        if mayores_25 > 0:
            promedio_goles_mayores_25 = total_goles_mayores_25 / mayores_25
            print(f"El promedio de goles de jugadores mayores a 25 es de {promedio_goles_mayores_25} goles")
        else:
            print("No hay jugadores mayores a 25 para sacar un promedio")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()