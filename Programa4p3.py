from tkinter import *  # Español: Importar todos los módulos de tkinter / English: Import all modules from tkinter
from tkinter import messagebox  # Español: Importar cuadros de mensaje / English: Import message boxes
from tkinter import ttk  # Español: Importar widgets temáticos / English: Import themed widgets
from validaciones import Validar  # Español: Importar clase Validar / English: Import Validar class
import numpy as np  # Español: Importar numpy para cálculos / English: Import numpy for calculations
import random  # Español: Importar generador de números aleatorios / English: Import random number generator

class Principal():  # Español: Clase principal de la aplicación / English: Main application class
    def __init__(self):  # Español: Constructor de la clase / English: Class constructor
        self.val = Validar()  # Español: Instancia para validaciones / English: Instance for validations
        self.ven = Tk()  # Español: Crear ventana principal / English: Create main window
        self.ven.title('Practica 4')  # Español: Establecer título / English: Set title
        #self.ven.geometry("500x300")  # Español: Tamaño inicial comentado / English: Initial size commented
        ancho = 500  # Español: Ancho de ventana / English: Window width
        alto = 300  # Español: Alto de ventana / English: Window height
        ventana_alto = self.ven.winfo_screenwidth()  # Español: Ancho de pantalla / English: Screen width
        ventana_ancho = self.ven.winfo_screenheight()  # Español: Alto de pantalla / English: Screen height
        x = (ventana_alto // 2) - (ancho // 2)  # Español: Posición X centrada / English: Centered X position
        y = (ventana_ancho // 2) - (alto // 2)  # Español: Posición Y centrada / English: Centered Y position
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}")  # Español: Establecer geometría centrada / English: Set centered geometry
        self.cont = 0  # Español: Contador para claves / English: Counter for keys
        self.bandera = False  # Español: Bandera para modo edición / English: Flag for edit mode
        self.renglon = -1  # Español: Fila seleccionada / English: Selected row
        self.index = ""  # Español: Índice temporal / English: Temporary index

    def validarCaja(self):  # Español: Validar selección de tabla / English: Validate table selection
        self.renglon = self.tabla.selection()  # Español: Obtener fila seleccionada / English: Get selected row
        if not self.renglon:  # Español: Si no hay selección / English: If no selection
            messagebox.showerror("Error","Elige una fila")  # Español: Mostrar error / English: Show error
        else:  # Español: Si hay selección / English: If there is selection
            valores = self.tabla.item(self.renglon, "values")  # Español: Obtener valores de fila / English: Get row values
            #valores = self.tabla.item(self.renglon)  # Español: Alternativa comentada / English: Alternative commented
            print(valores)  # Español: Imprimir valores / English: Print values
            self.index = valores[0]  # Español: Obtener clave / English: Get key
            self.index = self.index[:len(self.index)-2]  # Español: Remover sufijo / English: Remove suffix
            print(self.index)  # Español: Imprimir índice / English: Print index
            self.nombre.insert(0,valores[1])  # Español: Insertar nombre en caja / English: Insert name in box
            self.edad.insert(0,valores[3])  # Español: Insertar edad en caja / English: Insert age in box
            self.correo.insert(0,valores[2])  # Español: Insertar correo en caja / English: Insert email in box
            self.bandera= True  # Español: Activar modo edición / English: Activate edit mode

    def agregarElemento(self):  # Español: Agregar o editar elemento / English: Add or edit element
        if(len(self.nombre.get())==0 or len(self.edad.get())== 0 or len(self.correo.get())== 0):  # Español: Validar campos vacíos / English: Validate empty fields
            messagebox.showerror("Error","Faltan datos")  # Español: Mostrar error / English: Show error
        else:  # Español: Si todos los campos tienen datos / English: If all fields have data
            if (self.val.ValidarNombre(self.nombre.get())):  # Español: Validar nombre / English: Validate name
                if (self.val.ValidarNumeros(self.edad.get())):  # Español: Validar edad numérica / English: Validate numeric age
                    nombre = self.nombre.get()  # Español: Obtener nombre / English: Get name
                    edad = self.edad.get()  # Español: Obtener edad / English: Get age
                    correo = self.correo.get()  # Español: Obtener correo / English: Get email
                    if self.bandera == False:  # Español: Si no está en modo edición / English: If not in edit mode
                        self.cont += 1  # Español: Incrementar contador / English: Increment counter
                        clave = str(self.cont)+str(random.randint(1,100))+self.nombre.get()[0:2].upper()  # Español: Generar clave única / English: Generate unique key
                        self.tabla.insert("","end",values=(clave,nombre,correo,edad))  # Español: Insertar en tabla / English: Insert into table
                        self.nombre.delete(0,END)  # Español: Limpiar campo nombre / English: Clear name field
                        self.edad.delete(0,END)  # Español: Limpiar campo edad / English: Clear age field
                        self.correo.delete(0,END)  # Español: Limpiar campo correo / English: Clear email field
                    else:  # Español: Si está en modo edición / English: If in edit mode
                        clave = self.index+self.nombre.get()[0:2].upper()  # Español: Generar nueva clave / English: Generate new key
                        print("Modo edicion activado")  # Español: Mensaje de depuración / English: Debug message
                        self.tabla.item(self.renglon, values=(clave,nombre,correo,edad))  # Español: Actualizar fila / English: Update row
                        self.nombre.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                        self.edad.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                        self.correo.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                        self.bandera = False  # Español: Desactivar modo edición / English: Deactivate edit mode
                        self.renglon= -1  # Español: Reiniciar fila seleccionada / English: Reset selected row
                        messagebox.showinfo("Correcto","Datos Actualizados")  # Español: Mostrar confirmación / English: Show confirmation
                else:  # Español: Si edad es inválida / English: If age is invalid
                    messagebox.showinfo("Incorrecto","La edad esta mal")  # Español: Mostrar error / English: Show error
            else:  # Español: Si nombre es inválido / English: If name is invalid
                messagebox.showinfo("Incorrecto","El nombre esta mal")  # Español: Mostrar error / English: Show error

    def eliminar(self):  # Español: Eliminar elemento / English: Delete element
        renglon = self.tabla.selection()  # Español: Obtener fila seleccionada / English: Get selected row
        if not renglon:  # Español: Si no hay selección / English: If no selection
            messagebox.showerror("Error","Elige una fila")  # Español: Mostrar error / English: Show error
        else:  # Español: Si hay selección / English: If there is selection
            self.tabla.delete(renglon)  # Español: Eliminar fila / English: Delete row
            messagebox.showinfo("Correcto","Fila eliminada")  # Español: Mostrar confirmación / English: Show confirmation

    def inicio(self):  # Español: Inicializar interfaz / English: Initialize interface
        Label(self.ven, text="Nombre").place(x=10,y=10)  # Español: Etiqueta nombre / English: Name label
        self.nombre = Entry(self.ven, fg="blue")  # Español: Caja de texto nombre / English: Name text box
        self.nombre.place(x=10, y=40, width=100)  # Español: Posicionar caja nombre / English: Position name box
        Label(self.ven, text="Edad").place(x=130,y=10)  # Español: Etiqueta edad / English: Age label
        self.edad = Entry(self.ven, fg="green")  # Español: Caja de texto edad / English: Age text box
        self.edad.place(x=125, y=40, width=100)  # Español: Posicionar caja edad / English: Position age box
        Label(self.ven, text="Correo").place(x=250,y=10)  # Español: Etiqueta correo / English: Email label
        self.correo = Entry(self.ven, fg="purple")  # Español: Caja de texto correo / English: Email text box
        self.correo.place(x=240, y=40, width=100)  # Español: Posicionar caja correo / English: Position email box
        Button(self.ven, text="Agregar", command=self.agregarElemento, width=10).place(x=380,y=50, width=100,height=30)  # Español: Botón agregar / English: Add button
        Button(self.ven, text="Eliminar", command=self.eliminar, width=10).place(x=380,y=90, width=100,height=30)  # Español: Botón eliminar / English: Delete button
        Button(self.ven, text="Selecionar", command=self.validarCaja, width=10).place(x=380,y=130, width=100,height=30)  # Español: Botón seleccionar / English: Select button
        #dataGrid  # Español: Tabla de datos / English: Data table
        columnas = ("Clave","Nombre","Correo","Edad")  # Español: Columnas de tabla / English: Table columns
        self.tabla = ttk.Treeview(self.ven, columns= columnas, show="headings")  # Español: Crear tabla / English: Create table
        self.tabla.place(x=10, y=100, width=350,height=190)  # Español: Posicionar tabla / English: Position table
        for col in columnas:  # Español: Configurar columnas / English: Configure columns
            self.tabla.heading(col,text=col)  # Español: Establecer encabezados / English: Set headings
            self.tabla.column(col, anchor="center", width=30)  # Español: Configurar columnas / English: Configure columns
        scrolly = ttk.Scrollbar(self.ven,orient="vertical", command=self.tabla.yview)  # Español: Barra scroll vertical / English: Vertical scrollbar
        scrollx = ttk.Scrollbar(self.ven, orient="horizontal", command=self.tabla.xview)  # Español: Barra scroll horizontal / English: Horizontal scrollbar
        scrolly.place(x=360,y=90,height=200)  # Español: Posicionar scroll vertical / English: Position vertical scroll
        scrollx.place(x=10,y=280, width=350)  # Español: Posicionar scroll horizontal / English: Position horizontal scroll

        self.ven.mainloop()  # Español: Iniciar loop principal / English: Start main loop

if __name__=='__main__':  # Español: Si es ejecutado directamente / English: If executed directly
    app = Principal()  # Español: Crear instancia / English: Create instance
    app.inicio()  # Español: Iniciar aplicación / English: Start application