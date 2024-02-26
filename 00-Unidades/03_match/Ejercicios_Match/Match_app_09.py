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
Ejercicio: Match_09
---
Una agencia de viajes cobra $15.000 por cada estadía como base. 
Luego para calcular las tarifas total realiza el siguiente cálculo, 
en función de la estación del año y del destino elegido:
    Si es invierno: 
        Bariloche tiene un aumento del 20% 
        Cataratas y Córdoba tienen un descuento del 10%
        Mar del plata tiene un descuento del 20%
    Si es Verano:
        Bariloche tiene un descuento del 20%
        Cataratas y Cordoba tienen un aumento del 10%
        Mar del plata tiene un aumento del 20%
    Si es Primavera u Otoño:
        Bariloche tiene un aumento del 10%
        Cataratas tiene un aumento del 10%
        Mar del plata tiene un aumento del 10%
        Córdoba tiene precio sin descuento

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_estaciones = customtkinter.CTkLabel(master=self, text="Estaciones")
        self.label_estaciones.grid(row=0, column=0, padx=20, pady=10)
        estaciones = ['Verano', 'Otoño', 'Invierno', 'Primavera']
        self.combobox_estaciones = customtkinter.CTkComboBox(master=self, values=estaciones)
        self.combobox_estaciones.grid(row=1, column=0, padx=20, pady=(10, 10))

        
        self.label_destinos = customtkinter.CTkLabel(master=self, text="Destinos")
        self.label_destinos.grid(row=2, column=0, padx=20, pady=10)
        destinos = ['Bariloche', 'Mar del plata', 'Cataratas', 'Cordoba']
        self.combobox_destino = customtkinter.CTkComboBox(master=self, values=destinos)
        self.combobox_destino.grid(row=3, column=0, padx=20, pady=(10, 10))

        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=4, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        destinos = self.combobox_destino.get()
        estaciones = self.combobox_estaciones.get()
        precio_base = 15000
        aumento = 0
        descuento = 0
        match destinos:
            #agarra la caja de texto que elegiste en match
            case "Bariloche":
                if estaciones == "Invierno":
                    aumento = 20
                elif estaciones == "Verano":
                    descuento = 20
                else:
                    aumento = 10
                
            case "Cataratas" | "Cordoba":
                if estaciones == "Invierno":
                    descuento = 20
                elif estaciones == "Verano":
                    aumento = 10
                else: 
                    if estaciones == "Primavera" or "Otoño" and destinos == "Cataratas":
                        aumento = 10
                    else: 
                        if destinos == "Cordoba":
                            aumento = 0 
            
            case "Mar del plata":
                if estaciones == "Invierno":
                    descuento = 20
                elif estaciones == "Verano":
                    aumento = 20
                else:
                    aumento = 10
                    
        if descuento:   
            operacion_d = (descuento / 100) * 15000
            precio_final = precio_base - operacion_d
        else:
            operacion_a = (aumento / 100) * 15000
            precio_final = operacion_a + precio_base
        
        alert("Tp 9",precio_final)
        
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()