# Hacer un programa que lea nombre, apellido materno y paterno en 3 cajas separadas, ademas leer dia, mes, y año de nacimiento
# en 3 cajas separadas.
# Al presionar un boton se agregara a un listbox el rfc de la persona, ademas contendra 2 botones para eliminar elementos del listbox
# mediante pilas y colas.

from tkinter import *  # Español: Importar todos los módulos de tkinter / English: Import all modules from tkinter
from tkinter import messagebox  # Español: Importar cuadros de mensaje / English: Import message boxes
from ValidacionP2 import validar  # Español: Importar clase validar / English: Import validar class
class Ventana():  # Español: Clase principal de ventana / English: Main window class
    def __init__(self):  # Español: Constructor de la clase / English: Class constructor
        self.ven = Tk()  # Español: Crear ventana principal / English: Create main window
        self.ven.title('Programa 2')  # Español: Establecer título / English: Set title
        self.ven.geometry('650x300')  # Español: Establecer tamaño / English: Set size
        self.val = validar()  # Español: Instancia para validaciones / English: Instance for validations
        self.lista = []  # Español: Lista para almacenamiento / English: List for storage
        
    def Inicio(self):  # Español: Inicializar interfaz / English: Initialize interface
        Label(self.ven,text='Nombre').place(x=10,y=10)  # Español: Etiqueta nombre / English: Name label
        self.nombre = Entry(self.ven)  # Español: Campo nombre / English: Name field
        self.nombre.place(x=10,y=40)  # Español: Posicionar campo / English: Position field
        Label(self.ven,text='Apellido paterno').place(x=165,y=10)  # Español: Etiqueta apellido paterno / English: Last name label
        self.paterno = Entry(self.ven)  # Español: Campo apellido paterno / English: Last name field
        self.paterno.place(x=165,y=40)  # Español: Posicionar campo / English: Position field
        Label(self.ven,text='Apellido materno').place(x=320,y=10)  # Español: Etiqueta apellido materno / English: Mother's maiden name label
        self.materno = Entry(self.ven)  # Español: Campo apellido materno / English: Mother's maiden name field
        self.materno.place(x=320,y=40)  # Español: Posicionar campo / English: Position field
        Label(self.ven,text='FECHA DE NACIMIENTO').place(x=175,y=80)  # Español: Etiqueta fecha nacimiento / English: Birth date label
        Label(self.ven,text='Dia').place(x=10,y=120)  # Español: Etiqueta día / English: Day label
        self.dia = Entry(self.ven)  # Español: Campo día / English: Day field
        self.dia.place(x=10,y=150)  # Español: Posicionar campo / English: Position field
        Label(self.ven,text='Mes').place(x=165,y=120)  # Español: Etiqueta mes / English: Month label
        self.mes = Entry(self.ven)  # Español: Campo mes / English: Month field
        self.mes.place(x=165,y=150)  # Español: Posicionar campo / English: Position field
        Label(self.ven,text='Año').place(x=320,y=120)  # Español: Etiqueta año / English: Year label
        self.año = Entry(self.ven)  # Español: Campo año / English: Year field
        self.año.place(x=320,y=150)  # Español: Posicionar campo / English: Position field
        self.modo = StringVar(value='Pilas')  # Español: Variable para modo eliminación / English: Variable for deletion mode
        Button(self.ven,text='Calcular RFC',command=self.Calcular).place(x=10,y=180)  # Español: Botón calcular RFC / English: Calculate RFC button
        Button(self.ven,text='Eliminar',command=self.Eliminar).place(x=320,y=180)  # Español: Botón eliminar / English: Delete button
        Radiobutton(self.ven,text='Pilas',variable=self.modo, value='Pilas').place(x=165, y=180)  # Español: Radio pilas / English: Stack radio
        Radiobutton(self.ven,text='Colas',variable=self.modo, value='Colas').place(x=235, y=180)  # Español: Radio colas / English: Queue radio
        self.listview = Listbox(self.ven, height=10, width=15, bg='white', activestyle="dotbox", fg="Black")  # Español: Lista para RFCs / English: List for RFCs
        self.listview.place(x=480, y=10)  # Español: Posicionar lista / English: Position list
        self.ven.mainloop()  # Español: Iniciar loop principal / English: Start main loop
        
    def Calcular(self):  # Español: Calcular RFC / English: Calculate RFC
        a = False; b = False; c = False; d = False; e = False; f = False  # Español: Bandera de validaciones / English: Validation flags
        nombre = self.nombre.get()  # Español: Obtener nombre / English: Get name
        paterno = self.paterno.get()  # Español: Obtener apellido paterno / English: Get last name
        materno = self.materno.get()  # Español: Obtener apellido materno / English: Get mother's maiden name
        dia = self.dia.get()  # Español: Obtener día / English: Get day
        mes = self.mes.get()  # Español: Obtener mes / English: Get month
        anio = self.año.get()  # Español: Obtener año / English: Get year
        if nombre != "" and paterno != "" and materno != "" and dia != "" and mes != "" and anio != "":  # Español: Validar campos vacíos / English: Validate empty fields
            if self.val.ValidarLetra(nombre): a = True  # Español: Validar nombre / English: Validate name
            else:  # Español: Si nombre inválido / English: If name invalid
                messagebox.showerror('Error','Nombre incorrecto')  # Español: Mostrar error / English: Show error
                self.nombre.delete(0,END)  # Español: Limpiar campo / English: Clear field
            if self.val.ValidarLetra(paterno): b = True  # Español: Validar apellido paterno / English: Validate last name
            else:  # Español: Si apellido inválido / English: If last name invalid
                messagebox.showerror('Error','Apellido paterno incorrecto')  # Español: Mostrar error / English: Show error
                self.paterno.delete(0,END)  # Español: Limpiar campo / English: Clear field
            if self.val.ValidarLetra(materno): c = True  # Español: Validar apellido materno / English: Validate mother's maiden name
            else:  # Español: Si apellido materno inválido / English: If mother's maiden name invalid
                messagebox.showerror('Error','Apellido materno incorrecto')  # Español: Mostrar error / English: Show error
                self.materno.delete(0,END)  # Español: Limpiar campo / English: Clear field
            if self.val.ValidarNumeros(dia):  # Español: Validar día numérico / English: Validate numeric day
                if int(dia) < 1 or int(dia) > 31:  # Español: Validar rango día / English: Validate day range
                    messagebox.showerror('Error','Dia inválido')  # Español: Mostrar error / English: Show error
                    self.dia.delete(0,END)  # Español: Limpiar campo / English: Clear field
                else:  # Español: Si día válido / English: If day valid
                    d = True  # Español: Marcar válido / English: Mark valid
            else:  # Español: Si día no numérico / English: If day not numeric
                messagebox.showerror('Error','Dia inválido')  # Español: Mostrar error / English: Show error
                self.mes.delete(0,END)  # Español: Limpiar campo / English: Clear field
            if self.val.ValidarNumeros(mes):  # Español: Validar mes numérico / English: Validate numeric month
                if int(mes) < 1 or int(mes) > 12:  # Español: Validar rango mes / English: Validate month range
                    messagebox.showerror('Error','Mes inválido')  # Español: Mostrar error / English: Show error
                    self.mes.delete(0,END)  # Español: Limpiar campo / English: Clear field
                else:  # Español: Si mes válido / English: If month valid
                    e = True  # Español: Marcar válido / English: Mark valid
            else:  # Español: Si mes no numérico / English: If month not numeric
                messagebox.showerror('Error','Mes inválido')  # Español: Mostrar error / English: Show error
                self.mes.delete(0,END)  # Español: Limpiar campo / English: Clear field
            if self.val.ValidarNumeros(anio):  # Español: Validar año numérico / English: Validate numeric year
                if len(anio) > 4:  # Español: Validar longitud año / English: Validate year length
                    messagebox.showerror('Error','Año inválido')  # Español: Mostrar error / English: Show error
                    self.año.delete(0,END)  # Español: Limpiar campo / English: Clear field
                else:  # Español: Si año válido / English: If year valid
                    f = True  # Español: Marcar válido / English: Mark valid
            else:  # Español: Si año no numérico / English: If year not numeric
                messagebox.showerror('Error','Año inválido')  # Español: Mostrar error / English: Show error
                self.año.delete(0,END)  # Español: Limpiar campo / English: Clear field
            if a == True and b == True and c == True and d == True and e == True and f == True:  # Español: Si todas válidas / English: If all valid
                self.rfc = paterno[0:2].upper()+materno[0].upper()+nombre[0].upper()+anio[2:]+mes.zfill(2)+dia.zfill(2)  # Español: Calcular RFC / English: Calculate RFC
                self.listview.insert(self.listview.size()+1,self.rfc)  # Español: Insertar en lista / English: Insert into list
                self.nombre.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                self.paterno.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                self.materno.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                self.dia.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                self.mes.delete(0,END)  # Español: Limpiar campos / English: Clear fields
                self.año.delete(0,END)  # Español: Limpiar campos / English: Clear fields
        else:  # Español: Si hay campos vacíos / English: If there are empty fields
            messagebox.showerror('Error', "Cajas de texto vacías")  # Español: Mostrar error / English: Show error
            self.nombre.delete(0,END)  # Español: Limpiar campos / English: Clear fields
            self.paterno.delete(0,END)  # Español: Limpiar campos / English: Clear fields
            self.materno.delete(0,END)  # Español: Limpiar campos / English: Clear fields
            self.dia.delete(0,END)  # Español: Limpiar campos / English: Clear fields
            self.mes.delete(0,END)  # Español: Limpiar campos / English: Clear fields
            self.año.delete(0,END)  # Español: Limpiar campos / English: Clear fields
            
    def Eliminar(self):  # Español: Eliminar elemento / English: Delete element
        if self.listview.size() <= 0:  # Español: Si lista vacía / English: If list empty
            messagebox.showerror('Error','La lista está vacía')  # Español: Mostrar error / English: Show error
            return  # Español: Salir función / English: Exit function
        if self.modo.get() == 'Pilas':  # Español: Si modo pilas / English: If stack mode
            self.listview.delete(self.listview.size()-1)  # Español: Eliminar último (LIFO) / English: Delete last (LIFO)
        else:  # Español: Si modo colas / English: If queue mode
            self.listview.delete(0)  # Español: Eliminar primero (FIFO) / English: Delete first (FIFO)
            
if __name__ == '__main__':  # Español: Si es ejecutado directamente / English: If executed directly
    app = Ventana()  # Español: Crear instancia / English: Create instance
    app.Inicio()  # Español: Iniciar aplicación / English: Start application
