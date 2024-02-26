import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:Bruno
apellido:Condarco

Ejercicio: if_05
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el contenido de la caja de texto txtEdad, 
transformarlo en número e informar si la persona "NO ES ADOLESCENTE" utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)
                
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        edad= int(self.txt_edad.get())
        if (edad >=0  and edad <= 17):
            alert("", "No es adolescente")

        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
    '''
    OR= es como un puente donde solo basta q uno sea verdadero
    And= Necesita q ambos sean verdaderos


    Tabla de verdad de OR

    V    V     V
    V    F     V
    F    V     V
    F    F     F
    
    Tabla de verdad de AND
    V    V     V
    F    V     F
    V    F     F
    F    F     F
    
    '''