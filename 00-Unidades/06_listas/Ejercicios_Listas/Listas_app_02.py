import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_02
---
Enunciado:
Al presionar el botón 'Calcular' se deberá sumar todos los numeros de la lista, mostrar el resultado de la sumatoria y el promedio por Dialog Alert . 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]
        
    def btn_calcular_on_click(self):
        import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_01
---

Un gimnasio quiere medir el progreso de sus clientes, para ello se debe ingresar:

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)



No sabemos cuántos clientes serán consultados.

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

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        seguir = True

        nombre = ""

        personasdia1 = 0
        personasdia3 = 0
        personasdia5 = 0
        total_personas = 0
        
        porcentajeclientesdia1 = 0

        total_kilos = 0
        promediokilosdia3 = 0

        Banderaaltura= False
        altura_alto= 0
        nombre_alto= 0
        edad_alto= 0

        dia_concurrido = 0

        banderajoven = False
        nombre_joven = 0
        edad_joven = 0
        kilos_joven = 0

        while seguir:
            nombre = input("Ingrese su nombre")

            edad = int (input("Ingrese una edad"))
            while edad < 13:
                
                edad = int(input( "Reingrese una edad"))

            altura = float(input("Ingrese una altura"))
            while altura < 0:
                
                altura = float(input( "Reingrese una altura"))

            dias = int(input("Ingrese los dias que asiste (1 ,3 o 5)"))
            while dias != 1 and dias !=3 and dias != 5:
                
                dias = int(input( "Rengrese los dias que asiste (1 ,3 o 5)"))

            peso_muerto = float(input("Ingrese la cantida que levanta en peso muerto"))
            while peso_muerto < 1:
                
                peso_muerto = float(input( "Reingrese la cantida que levanta en peso muerto"))
            

            if dias == 1:                      
                personasdia1 += 1
            elif dias == 3:                                                   #El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
                personasdia3 += 1
                total_kilos += peso_muerto
            else:
                personasdia5 += 1
            

            if dias == 5 and (edad < edad_joven or banderajoven ==  False):            #Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
                edad_joven = edad
                kilos_joven = peso_muerto
                nombre_joven = nombre
                banderajoven = True

            if altura > altura_alto or Banderaaltura == False:                                             #Nombre y edad del cliente con más altura.
                nombre_alto = nombre
                edad_alto = edad
                altura_alto = altura
                Banderaaltura = True

            seguir = question("","Desea continuar?")

        if personasdia5 > personasdia3 and personasdia5 > personasdia1:                     #Determinar si los clientes eligen más ir 1, 3 o 5 días
            dia_concurrido = 5
        elif personasdia3 > personasdia1 :
            dia_concurrido = 3
        else:
            dia_concurrido = 1

        total_personas = personasdia1 + personasdia3 + personasdia5
        if personasdia1 > 0:                                                        #El porcentaje de clientes que asiste solo 1 día a la semana.
            porcentajeclientesdia1 = round(personasdia1 / total_personas * 100) #porcentaje
                
        if personasdia3 > 0:
            promediokilosdia3 = total_kilos / personasdia3 # promedio


                
        print (f"El promedio de kilos que levantan las personas que asisten solo 3 días a la semana es de {promediokilosdia3}")
        print (f"El porcentaje de clientes que asiste solo 1 día a la semana es de {porcentajeclientesdia1}")
        print (f"{nombre_alto} es el cliente con mas altura y tiene {edad_alto} años")
        print (f"El dia mas concurrido fue el {dia_concurrido}")
        print (f"El Nombre y kilos que levanta de la persona más joven que solo asista 5 días a la semana es {nombre_joven} y levanta {kilos_joven}")




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

        


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()