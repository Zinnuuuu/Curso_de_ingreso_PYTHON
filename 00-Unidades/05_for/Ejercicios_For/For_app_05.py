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

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True

        kilos_total = 0
        acumulador_dia3 = 0
        cantidad_clientes= 0

        bandera_masaltura= False
        altura_max = 0
        nombre_max = 0
        edad_max = 0
        
        cantidad_clientesdia1= 0
        cantidad_clientesdia3 = 0
        cantidad_clientesdia5 = 0

        bandera_dia5 = False

        dia_concurrido = 0

        while seguir == True:

            nombre = prompt("","Ingrese su nombre")

            edad = int(prompt("","Ingrese una edad"))

            while edad < 13:
                
                edad = int(prompt("", "Ingrese una edad"))

            altura = float(prompt("","Ingrese una altura"))

            while altura < 0:
            
                altura= float(prompt("","Ingrese una altura"))

            dias = int(prompt("","Ingrese la cantidad de dias"))
            
            while dias != 1 and dias != 3 and dias != 5:

                dias = int(prompt("", "Ingrese un dia"))

            peso_muerto = float(prompt("","Ingrese una peso_muerto"))

            while peso_muerto < 1:

                peso_muerto= float(prompt("","Ingrese una peso_muerto"))

# El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.
                if dias == 3:
                    kilos_total +=peso_muerto
                    cantidad_clientesdia3 += 1
                elif dias == 1:
                    cantidad_clientesdia1 += 1

# El porcentaje de clientes que asiste solo 1 día a la semana.
            else:
                cantidad_clientesdia5 += 1
            if bandera_dia5 ==False:
                edad_min_5 = edad
                nombre_min = nombre
                kilos_min_5 = peso_muerto
                bandera_dia5 = True
            elif edad < edad_min_5:
                edad_min_5 = edad
                nombre_min = nombre
                kilos_min_5 = peso_muerto
                

                cantidad_clientes += 1
# Nombre y edad del cliente con más altura.
                if altura > altura_max or bandera_masaltura ==False:
                    altura_max = altura
                    nombre_max = nombre
                    edad_max = edad
                    bandera_masaltura = True 

                seguir = question("","Desea seguir?")

            if cantidad_clientesdia5 > cantidad_clientesdia3 and cantidad_clientesdia5 > cantidad_clientesdia1 :
                dia_concurrido = "Dia 5"
            elif cantidad_clientesdia3 > cantidad_clientesdia1:
                dia_concurrido = "Dia 3"
            else:
                dia_concurrido = "Dia 1"




        promedio_kilos = kilos_total / acumulador_dia3
        porcentaje_clientes1 = cantidad_clientes / cantidad_clientesdia1 * 100

        print(f"El promedio de kilos que levantan las personas que asiste solo 3 dias a la semana es de {promedio_kilos}")
        print(f"El porcentaje de clientes que asiste solo 1 día a la semana es de {porcentaje_clientes1}")
        print(f"El nombre y edad de la persona mas alta es : {nombre_max}, {edad_max}")
        print(f"El dia mas concurrido es {dia_concurrido}")
        print(f"El Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana es: {nombre_min} , {edad_min_5} y levanta {kilos_min_5}") 
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
# El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

# El porcentaje de clientes que asiste solo 1 día a la semana.

# Nombre y edad del cliente con más altura.

# Determinar si los clientes eligen más ir 1, 3 o 5 días

# Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
        # bandera = True
        # undiagym= 0
        # tresdiasgym = 0
        # cincodiasgym = 0
        # total_dias_gym = 0
        # contador_kilos= 0
        # acumulador_kilos = 0
        # promedio_kilos = 0
        # nombre_max = 0
        # edad_max =0
        # minimo_edad = 0
        # nombre_minimo= 0
        # kilos_minimo= 0



        # while bandera:
        #     nombre = input("Ingrese su nombre:")
        #     edad = int(input("Ingrese su edad:"))
        #     if edad < 12:
        #         print ("No puede asistir")
        #         break
        #     altura = int(input ("Ingrese su altura (sin puntos):"))
        #     if altura < 0:
        #         break
        #     dias = int(input ("Escoja la cantidad de dias a asistir 1 , 3 o 5:")) #1 , 3 ,5
        #     if dias != 1 and dias != 3 and dias != 5:
        #         break
        #     else:
        #         contador_kilos+= 1
        #     contador_kilos= int(input ("Ingrese la cantidad de kilos que levanta en peso muerto")) # no 0 ni negativo
        #     if contador_kilos== 0 or contador_kilos< 0:
        #         break
        #     bandera = False

        # match dias:
        #     case "1":
        #         undiagym += 1
        #         promedioundia = undiagym
        #     case "3":
        #         tresdiasgym += 1
        #     case "5":
        #         if edad < minimo_edad and cincodiasgym == 1:
        #             cincodiasgym += 1
        #             minimo_edad = edad
        #             nombre_minimo = nombre
        #             kilos_minimo = contador_kilos
                

        # match altura:
        #     case "Altura":
        #         if edad > edad_max:
        #             edad_max = edad
        #             nombre_max = nombre

        # if undiagym == tresdiasgym and undiagym == cincodiasgym:
        #         mas_votado = "La gente elige ir entre los 3 dias"
        # elif tresdiasgym > undiagym and tresdiasgym > cincodiasgym:
        #         mas_votado = "Tres dias a la semana es la mayoria de veces que la gente elige ir"
        # elif undiagym > tresdiasgym and undiagym > cincodiasgym:
        #         mas_votado = "Un dia a la semana es la mayoria de veces que la gente elige ir"
        # elif undiagym == tresdiasgym:
        #         mas_votado = "La gente elige ir entre un dia y tres dias"
        # elif undiagym == cincodiasgym:
        #         mas_votado= "La gente elige ir entre un dia y cinco dias"
        # elif tresdiasgym == cincodiasgym:
        #         mas_votado = "La gente elige ir entre tres dias y cinco dias"
        # else:
        #         mas_votado = "Cinco dias a la semana es la mayoria de veces que la gente elige ir"
        
        
        
            
            
        # promedio_kilos = acumulador_kilos / contador_kilos   
        # total_dias_gym = undiagym + tresdiasgym + cincodiasgym         
        # seguir = question("Seguir", "Ingresar otro cliente")

        # print(f"El promedio de kilos que levantan las personas que asiste solo 3 dias a la semana es de {promedio_kilos}")
        # print(f"El porcentaje de clientes que asiste solo 1 día a la semana es de .")
        # print(f"{nombre_max} de {edad_max} es el cliente con mas altura")
        # print(f"Los clientes eligen ir mas ...")