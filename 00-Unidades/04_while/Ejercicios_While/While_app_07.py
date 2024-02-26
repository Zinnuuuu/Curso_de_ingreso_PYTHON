import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_07
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario quiera, 
hasta que presione el botón Cancelar (en el prompt). 
Calcular la suma acumulada y el promedio de los números ingresados. 
Luego informar los resultados en las cajas de texto txt_suma_acumulada y txt_promedio

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.txt_suma_acumulada = customtkinter.CTkEntry(master=self, placeholder_text="Suma acumulada")
        self.txt_suma_acumulada.grid(row=0, padx=20, pady=20)

        self.txt_promedio = customtkinter.CTkEntry(master=self, placeholder_text="Promedio")
        self.txt_promedio.grid(row=1, padx=20, pady=20)

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
# UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
# que promete revolucionar el mercado. 
# Las posibles aplicaciones son las siguientes: 
# # Inteligencia artificial (IA),
# # Realidad virtual/aumentada (RV/RA), 
# # Internet de las cosas (IOT)  

# Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

# Los datos a ingresar por cada encuestado son:
#     * nombre del empleado
#     * edad (no menor a 18)
#     * genero (Masculino - Femenino - Otro)
#     * tecnologia (IA, RV/RA, IOT)   

# En esta opción, se ingresaran empleados hasta que el usuario lo desee.

# Una vez finalizado el ingreso, mostrar:

    #! 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #! 2) - Tecnología que mas se votó.
    #! 3) - Porcentaje de empleados por cada genero
    #! 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #! 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #! 6) - Nombre y género del empleado que voto por RV/RA con menor edad.}
            seguir = True
            contador_masculino_IOT_IA = 0

            contador_IOT= 0
            contador_IA = 0
            contador_RV_RA = 0

            contador_masculino = 0
            contador_femenino = 0
            contador_otro = 0

            contador_IOT_edad = 0

            contador_IA_femenino= 0
            acumulador_edad_femenino_IA= 0

            minimo_edad = 0

            while seguir:
                nombre = input ("Ingrese nombre")
                edad = input ("Ingrese edad")
                edad = int (edad)
                while edad < 18:
                    edad = input("Reingrese edad")
                    edad = int(edad)
                genero = input ("Ingrese su genero")
                while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                    genero = input("Reingrese genero")
                tecnologia = input ("Ingrese tecnologia")
                while tecnologia != "IOT" and tecnologia != "IA" and tecnologia != "RV/RA":
                    tecnologia = input("Reingrese tecnologia")
                #Procesamiento de datos(repetitivo)

                
                match tecnologia:
                    case "IOT":
                        contador_IOT +=1
                        if (edad > 18 and edad < 25) or (edad > 33 and edad < 43 ):
                            contador_IOT_edad+= 1
                    case "IA":
                        contador_IA +=1
                    case "RV/RA":
                        contador_RV_RA +=1
                        if edad < minimo_edad or contador_RV_RA == 1:
                            minimo_edad = edad
                            nombre_minimo = nombre
                            genero_minimo = genero
                            bandera_RV_RA = True
                            


                match genero:
                    case "Masculino":
                        contador_masculino +=1
                        if (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <=50:
                            contador_masculino_IOT_IA += 1
                    case "Femenino":
                        contador_femenino +=1
                        if tecnologia == "IA":
                            contador_IA_femenino += 1
                            acumulador_edad_femenino_IA += 1
                    case "Otros":
                        contador_otro +=1

                seguir = question ("Seguir", "Ingresar otro empleado")

                #Procesamiento de datos (no se repite)
                #2)
            if contador_IA == contador_IOT and contador_IA == contador_RV_RA:
                mas_votado = "Hubo empate entre los 3"
            elif contador_IOT > contador_IA and contador_IOT > contador_RV_RA:
                mas_votado = "IOT es la tecnologia mas votada"
            elif contador_IA > contador_IOT and contador_IA > contador_RV_RA:
                mas_votado = "IA es la tecnologia mas votada"
            elif contador_IA == contador_IOT:
                mas_votado = "Hubo empate entre IA Y IOT"
            elif contador_IA == contador_RV_RA:
                mas_votado= "Hubo empate entre IA y RV/RA"
            elif contador_IOT == contador_RV_RA:
                mas_votado = "Hubo empate entre IOT y RV/RA"
            else:
                mas_votado = "Se voto mas a RV/RA"
                
                #3)
                total_empleados= contador_otro + contador_masculino + contador_femenino

                porcentaje_femenino = (contador_femenino * 100) / total_empleados
                porcentaje_masculino = (contador_masculino * 100) / total_empleados
                porcentaje_otros = 100 - (porcentaje_femenino + porcentaje_masculino)
                
                porcentaje_IOT_edad = (contador_IOT_edad * 100) / total_empleados
                
                if contador_IA_femenino > 0:
                    promedio_edad_femenino = acumulador_edad_femenino_IA / contador_IA_femenino
                else:
                    promedio_edad_femenino = "No hay femeninos que votarion IA"
                #SALIDA
                print (f"Cantidad de masculinos que votaron IOT/IA en el rango buscado {contador_masculino_IOT_IA}")
                print (f"Tecnologia mas votada :{mas_votado}")
                print (f"Porcentaje:\n\t Masculino: {porcentaje_masculino}%\n\t{porcentaje_femenino}\n\t{porcentaje_otros}")
                print (f"Porcentaje IOT : {porcentaje_IOT_edad}")
                print (f"Promedio edad:{promedio_edad_femenino} ")
                print (f"{nombre_minimo} de genero {genero_minimo} voto por RV/RA siendo menor de edad")


                
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

                