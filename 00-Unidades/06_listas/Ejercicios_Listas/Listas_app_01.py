import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


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
        personasdia1 = 0
        personasdia3 = 0
        personasdia5 = 0
        totalpersonas = 0

        total_kilos = 0

        banderaaltura = False
        altura_max = 0
        edad_max = 0
        nombre_max = 0

        dia_concurrido = 0

        banderadia5 = False
        nombre_joven = 0
        kilos_joven = 0
        edad_joven = 0


        
        
        while seguir == True:
            nombre = prompt("","Ingrese su nombre")

            edad = int(prompt("","Ingrese una edad"))
            while edad < 13:
                
                edad = int(prompt("", "Ingrese una edad"))

            altura = float(prompt("","Ingrese su altura (en cm)"))
            while altura < 0:
                
                altura = float(prompt("", "Reingrese su altura (en cm)"))

            dias = int(prompt("","Ingrese los dias que vendra"))
            while dias != 1 and dias != 3 and dias != 5:
                
                dias = int(prompt("", "Reingrese los dias que vendra"))

            peso_muerto = float(prompt("","Ingrese cuanto levanta en peso muerto"))
            while peso_muerto < 1:
                
                peso_muerto = float(prompt("", "Reingrese cuanto levanta en peso muerto"))
        
        
        if dias == 1:
            personasdia1 += 1
        elif dias == 3:                                                                   # El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
            personasdia3 += 1
            promedio_kilo = total_kilos + peso_muerto / personasdia3
        else:
            personasdia5 += 1
            


        if banderadia5 == False:                                       #Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
            edad_joven = edad
            nombre_joven = nombre
            kilos_joven = peso_muerto
            banderadia5 = True
        elif edad < edad_joven:
            edad_joven = edad
            nombre_joven = nombre
            kilos_joven = peso_muerto
            banderadia5 = True


        if altura > altura_max and banderaaltura == False:                                   #Nombre y edad del cliente con más altura.
            altura_max = altura
            nombre_max = nombre
            edad_max = edad
            banderaaltura =  True

            seguir = question("","Desea continuar?")
        
        if personasdia5 > personasdia3 and personasdia5 > personasdia1:                          #Determinar si los clientes eligen más ir 1, 3 o 5 días
            dia_concurrido = 5
        elif personasdia3 > personasdia1:
            dia_concurrido = 3
        else:
            dia_concurrido = 1

        

        totalpersonas = personasdia1 + personasdia3 + personasdia5                         #El porcentaje de clientes que asiste solo 1 día a la semana.
        porcentaje_pers_dia1 = (totalpersonas / personasdia1 )* 100

        print(f" El promedio de kilos que levantan las personas que asisten solo 3 días a la semana es de {promedio_kilo}") 
        print(f"El porcentaje de clientes que asiste 1 vez a la semana es de {porcentaje_pers_dia1}")
        print(f"El cliente mas alto es {nombre_max} y tiene {edad_max} años")
        print(f"El dia mas concurrido fue el dia {dia_concurrido}")
        print(f"El Nombre y kilos que levanta de la persona más joven que solo asista 5 días a la semana es {nombre_joven} y levanta {kilos_joven}")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()