from tkinter import *  # Español: Importar todos los módulos de tkinter / English: Import all modules from tkinter
from tkinter import messagebox  # Español: Importar cuadros de mensaje / English: Import message boxes
from validaciones import Validar  # Español: Importar clase Validar / English: Import Validar class
import numpy as np  # Español: Importar numpy para arrays / English: Import numpy for arrays
class Principal():  # Español: Clase principal de la aplicación / English: Main application class
    def __init__(self):  # Español: Constructor de la clase / English: Class constructor
        self.val = Validar()  # Español: Instancia para validaciones / English: Instance for validations
        self.ven = Tk()  # Español: Crear ventana principal / English: Create main window
        #self.ven.geometry("320x220")  # Español: Tamaño inicial comentado / English: Initial size commented
        ancho = 320  # Español: Ancho de ventana / English: Window width
        alto = 220  # Español: Alto de ventana / English: Window height
        ventana_alto = self.ven.winfo_screenwidth()  # Español: Ancho de pantalla / English: Screen width
        ventana_ancho = self.ven.winfo_screenheight()  # Español: Alto de pantalla / English: Screen height
        x = (ventana_alto // 2) - (ancho // 2)  # Español: Posición X centrada / English: Centered X position
        y = (ventana_ancho // 2) - (alto // 2)  # Español: Posición Y centrada / English: Centered Y position
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")  # Español: Establecer geometría centrada / English: Set centered geometry
        self.lis = []  # Español: Lista temporal para ordenamiento / English: Temporary list for sorting

    def validarCaja(self):  # Español: Validar y procesar entrada / English: Validate and process input
        valor = self.dato.get()  # Español: Obtener valor de entrada / English: Get input value
        # if (self.val.ValidarLetra(valor)):  # Español: Validación comentada / English: Commented validation
        #     messagebox.showinfo("Correcto", "Si comienza con Mayusculas")
        # else:
        #     messagebox.showinfo("Incorrecto", "No comienza con mayuscula")
        # if (self.val.ValidarNumeros(valor)):  # Español: Validación comentada / English: Commented validation
        #     messagebox.showinfo("Correcto", "Si es un numero")
        # else:
        #     messagebox.showerror("Incorrecto", "No es un numero")
        if (self.val.ValidarNumeros(valor)):  # Español: Validar si es número / English: Validate if it's a number
            if (self.val.ValidarEntradas(valor)):  # Español: Validar longitud / English: Validate length
                self.lista.insert(self.lista.size()+1, valor)  # Español: Insertar en lista / English: Insert into list
                self.dato.delete(0,END)  # Español: Limpiar campo / English: Clear field
            else:  # Español: Si longitud no es válida / English: If length is invalid
                messagebox.showerror("Error", "Solo se permite 2 digitos")  # Español: Mostrar error / English: Show error
                self.dato.delete(0,END)  # Español: Limpiar campo / English: Clear field
        else:  # Español: Si no es número / English: If not a number
            messagebox.showerror("Error", "No son numeros")  # Español: Mostrar error / English: Show error
            self.dato.delete(0,END)  # Español: Limpiar campo / English: Clear field

        # print(f'La cadena tiene {str(self.val.ValidarEntradas(valor))}')  # Español: Debug comentado / English: Commented debug
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')  # Español: Actualizar contador / English: Update counter

    def eliminarDato(self):  # Español: Eliminar dato de lista / English: Delete data from list
        if self.lista.size() <= 0:  # Español: Si lista está vacía / English: If list is empty
            messagebox.showerror("Error", "La lista esta vacia")  # Español: Mostrar error / English: Show error
            return  # Español: Salir de función / English: Exit function
        if self.modo.get() == 'Pilas':  # Español: Si modo es pilas (LIFO) / English: If mode is stacks (LIFO)
            # ultimo que entra primero que sale  # Español: Comentario LIFO / English: LIFO comment
            self.lista.delete(self.lista.size()-1)  # Español: Eliminar último elemento / English: Delete last element
        else:  # Español: Si modo es colas (FIFO) / English: If mode is queues (FIFO)
            # primero que entra primero que sale  # Español: Comentario FIFO / English: FIFO comment
            self.lista.delete(0)  # Español: Eliminar primer elemento / English: Delete first element
        self.label.config(text=f'Elementos en la lista: {str(self.lista.size())}')  # Español: Actualizar contador / English: Update counter

    def ordenar(self):  # Español: Ordenar lista / English: Sort list
        self.lis = list(self.lista.get(0,END))  # Español: Convertir lista a Python list / English: Convert to Python list
        if len(self.lis) <= 0:  # Español: Si lista está vacía / English: If list is empty
            messagebox.showerror("Error ","Lista vacia")  # Español: Mostrar error / English: Show error
        else:  # Español: Si hay elementos / English: If there are elements
            #burbuja  # Español: Algoritmo burbuja / English: Bubble algorithm
            if self.modo2.get() == 'Burguja':  # Español: Si método es burbuja / English: If method is bubble
                for i in range(0,len(self.lis)):  # Español: Bucle externo / English: Outer loop
                    for x in range(0,len(self.lis)-1):  # Español: Bucle interno / English: Inner loop
                        if self.lis[x] > self.lis[x+1]:  # Español: Comparar elementos / English: Compare elements
                            aux = self.lis[x]  # Español: Guardar temporal / English: Save temporary
                            self.lis[x] = self.lis[x+1]  # Español: Intercambiar / English: Swap
                            self.lis[x+1] = aux  # Español: Intercambiar / English: Swap
                print(self.lis)  # Español: Imprimir lista ordenada / English: Print sorted list
                self.lista.delete(0,END)  # Español: Limpiar lista visual / English: Clear visual list
                for i in self.lis:  # Español: Recorrer lista ordenada / English: Iterate sorted list
                    self.lista.insert(self.lista.size()+1, i)  # Español: Insertar elementos / English: Insert elements          
            # self.arreglo = np.array(self.lis)  # Español: Array numpy comentado / English: Numpy array commented
            # for i in self.arreglo:  # Español: Iteración comentada / English: Commented iteration
            #     print(i)
            else:  # Español: Si método es selección / English: If method is selection
                # seleccion  # Español: Algoritmo selección / English: Selection algorithm
                p = 0  # Español: Índice de posición / English: Position index
                for i in range(0,len(self.lis)):  # Español: Bucle externo / English: Outer loop
                    aux = int(self.lis[i])  # Español: Valor actual / English: Current value
                    p = i  # Español: Posición actual / English: Current position
                    for x in range(i,len(self.lis)):  # Español: Bucle interno / English: Inner loop
                        # print(self.lis[x])  # Español: Debug comentado / English: Commented debug
                        if aux < int(self.lis[x]):  # Español: Buscar máximo / English: Find maximum
                            aux = int(self.lis[x])  # Español: Actualizar máximo / English: Update maximum
                            p = x  # Español: Actualizar posición / English: Update position
                    self.lis[p] = self.lis[i]  # Español: Intercambiar / English: Swap
                    self.lis[i] = str(aux)  # Español: Colocar máximo / English: Place maximum
                print(self.lis)  # Español: Imprimir lista ordenada / English: Print sorted list
                self.lista.delete(0,END)  # Español: Limpiar lista visual / English: Clear visual list
                for i in self.lis:  # Español: Recorrer lista ordenada / English: Iterate sorted list
                    self.lista.insert(self.lista.size()+1, i)  # Español: Insertar elementos / English: Insert elements

    def quitar_placeholder(self, event):  # Español: Remover texto guía / English: Remove placeholder text
        if self.dato.get() == self.placeholder:  # Español: Si tiene texto guía / English: If has placeholder text
            self.dato.delete(0, END)  # Español: Limpiar campo / English: Clear field
            self.dato.config(fg="black")  # Español: Cambiar color texto / English: Change text color

    def poner_placeholder(self, event):  # Español: Poner texto guía / English: Set placeholder text
        if self.dato.get() == "":  # Español: Si campo está vacío / English: If field is empty
            self.dato.insert(0, self.placeholder)  # Español: Insertar texto guía / English: Insert placeholder text
            self.dato.config(fg="gray")  # Español: Cambiar color texto / English: Change text color

    def inicio(self):  # Español: Inicializar interfaz / English: Initialize interface
        # self.dato = Entry(self.ven,)  # Español: Entrada comentada / English: Commented entry
        # self.dato.place(x=50, y=10)  # Español: Posición comentada / English: Commented position
        self.nombre = Entry(self.ven).place(x=1,y=1)  # Español: Entrada oculta / English: Hidden entry
        self.placeholder = "Escribe un número"  # Español: Texto guía / English: Placeholder text
        self.dato = Entry(self.ven, fg="gray")  # Español: Campo de entrada / English: Input field
        self.dato.insert(0, self.placeholder)  # Español: Insertar texto guía / English: Insert placeholder text
        self.dato.bind("<FocusIn>", self.quitar_placeholder)  # Español: Evento al enfocar / English: Focus in event
        self.dato.bind("<FocusOut>", self.poner_placeholder)  # Español: Evento al desenfocar / English: Focus out event
        self.dato.bind("<Return>", self.validarCaja)  # Español: Evento Enter / English: Enter key event
        self.dato.place(x=50, y=10, width=100)  # Español: Posicionar campo / English: Position field
        self.modo = StringVar(value="Pilas")  # Español: Variable para modo / English: Variable for mode
        Radiobutton(self.ven, text="Pilas", variable=self.modo, value="Pilas").place(x=50,y=40)  # Español: Radio pilas / English: Stack radio
        Radiobutton(self.ven, text="Colas", variable=self.modo, value="Colas").place(x=100,y=40)  # Español: Radio colas / English: Queue radio
        Button(self.ven, text="Validar", command=self.validarCaja, width=10).place(x=100,y=90)  # Español: Botón validar / English: Validate button
        Button(self.ven, text="Eliminar", command=self.eliminarDato, width=10).place(x=100,y=120)  # Español: Botón eliminar / English: Delete button
        self.modo2 = StringVar(value="Burguja")  # Español: Variable para método ordenamiento / English: Variable for sort method
        Radiobutton(self.ven, text="Burguja", variable=self.modo2, value="Burguja").place(x=50,y=150)  # Español: Radio burbuja / English: Bubble radio
        Radiobutton(self.ven, text="Seleccion", variable=self.modo2, value="Seleccion").place(x=100,y=150)  # Español: Radio selección / English: Selection radio
        Button(self.ven, text="Ordenar", command=self.ordenar, width=10).place(x=100,y=180)  # Español: Botón ordenar / English: Sort button
        self.label = Label(text="Numero")  # Español: Etiqueta inicial / English: Initial label
        self.label.place(x=5,y=70)  # Español: Posicionar etiqueta / English: Position label
        self.lista = Listbox(self.ven, height=10, width=10, bg="white",font=("Helvetica", 12))  # Español: Lista visual / English: Visual list
        self.lista.place(x=190, y=10)  # Español: Posicionar lista / English: Position list
        self.ven.mainloop()  # Español: Iniciar loop principal / English: Start main loop

if __name__=='__main__':  # Español: Si es ejecutado directamente / English: If executed directly
    app = Principal()  # Español: Crear instancia / English: Create instance
    app.inicio()  # Español: Iniciar aplicación / English: Start application
