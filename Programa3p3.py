from tkinter import *  # Español: Importar todos los módulos de tkinter / English: Import all modules from tkinter
from tkinter import messagebox  # Español: Importar cuadros de mensaje / English: Import message boxes
from validaciones import Validar  # Español: Importar clase Validar / English: Import Validar class
class Ventana():  # Español: Clase principal de ventana / English: Main window class
    def __init__(self):  # Español: Constructor de la clase / English: Class constructor
        self.val = Validar()  # Español: Instancia para validaciones / English: Instance for validations
        self.ven = Tk()  # Español: Crear ventana principal / English: Create main window
        self.ven.title('Programa 3')  # Español: Establecer título / English: Set title
        ancho = 350  # Español: Ancho de ventana / English: Window width
        alto = 250  # Español: Alto de ventana / English: Window height
        ventana_alto = self.ven.winfo_screenmmwidth()  # Español: Ancho de pantalla en mm / English: Screen width in mm
        ventana_ancho = self.ven.winfo_screenmmwidth()  # Español: Alto de pantalla en mm / English: Screen height in mm
        x = (ventana_alto // 2) - (ancho // 2)  # Español: Posición X centrada / English: Centered X position
        y = (ventana_ancho // 2) - (alto // 2)  # Español: Posición Y centrada / English: Centered Y position
        self.ven.geometry(f'{ancho}x{alto}+{x+550}+{y+150}')  # Español: Establecer geometría con offset / English: Set geometry with offset
        
    def quitar_placeholder1(self, event):  # Español: Remover texto guía nombre / English: Remove name placeholder
        if self.nombre.get() == self.placeholder1:  # Español: Si tiene texto guía / English: If has placeholder text
            self.nombre.delete(0, END)  # Español: Limpiar campo / English: Clear field
            self.nombre.config(fg="black")  # Español: Cambiar color texto / English: Change text color
            
    def poner_placeholder1(self, event):  # Español: Poner texto guía nombre / English: Set name placeholder
        if self.nombre.get() == "":  # Español: Si campo vacío / English: If field empty
            self.nombre.insert(0, self.placeholder1)  # Español: Insertar texto guía / English: Insert placeholder text
            self.nombre.config(fg="gray")  # Español: Cambiar color texto / English: Change text color
            
    def quitar_placeholder2(self, event):  # Español: Remover texto guía teléfono / English: Remove phone placeholder
        if self.telefono.get() == self.placeholder2:  # Español: Si tiene texto guía / English: If has placeholder text
            self.telefono.delete(0, END)  # Español: Limpiar campo / English: Clear field
            self.telefono.config(fg="black")  # Español: Cambiar color texto / English: Change text color
            
    def poner_placeholder2(self, event):  # Español: Poner texto guía teléfono / English: Set phone placeholder
        if self.telefono.get() == "":  # Español: Si campo vacío / English: If field empty
            self.telefono.insert(0, self.placeholder2)  # Español: Insertar texto guía / English: Insert placeholder text
            self.telefono.config(fg="gray")  # Español: Cambiar color texto / English: Change text color
            
    def quitar_placeholder3(self, event):  # Español: Remover texto guía domicilio / English: Remove address placeholder
        if self.domicilio.get() == self.placeholder3:  # Español: Si tiene texto guía / English: If has placeholder text
            self.domicilio.delete(0, END)  # Español: Limpiar campo / English: Clear field
            self.domicilio.config(fg="black")  # Español: Cambiar color texto / English: Change text color
            
    def poner_placeholder3(self, event):  # Español: Poner texto guía domicilio / English: Set address placeholder
        if self.domicilio.get() == "":  # Español: Si campo vacío / English: If field empty
            self.domicilio.insert(0, self.placeholder3)  # Español: Insertar texto guía / English: Insert placeholder text
            self.domicilio.config(fg="gray")  # Español: Cambiar color texto / English: Change text color
            
    def Inicio(self):  # Español: Inicializar interfaz / English: Initialize interface
        self.placeholder1 = 'Nombre'  # Español: Texto guía nombre / English: Name placeholder text
        self.nombre = Entry(self.ven, fg="gray")  # Español: Campo nombre / English: Name field
        self.nombre.insert(0, self.placeholder1)  # Español: Insertar texto guía / English: Insert placeholder text
        self.nombre.bind("<FocusIn>", self.quitar_placeholder1)  # Español: Evento al enfocar / English: Focus in event
        self.nombre.bind("<FocusOut>", self.poner_placeholder1)  # Español: Evento al desenfocar / English: Focus out event
        self.nombre.bind("<Return>", self.ValidarCaja)  # Español: Evento Enter / English: Enter key event
        self.nombre.place(x=10, y=10, width=100)  # Español: Posicionar campo / English: Position field
        self.placeholder2 = "Telefono"  # Español: Texto guía teléfono / English: Phone placeholder text
        self.telefono = Entry(self.ven, fg="gray")  # Español: Campo teléfono / English: Phone field
        self.telefono.insert(0, self.placeholder2)  # Español: Insertar texto guía / English: Insert placeholder text
        self.telefono.bind("<FocusIn>", self.quitar_placeholder2)  # Español: Evento al enfocar / English: Focus in event
        self.telefono.bind("<FocusOut>", self.poner_placeholder2)  # Español: Evento al desenfocar / English: Focus out event
        self.telefono.bind("<Return>", self.ValidarCaja)  # Español: Evento Enter / English: Enter key event
        self.telefono.place(x=120, y=10, width=100)  # Español: Posicionar campo / English: Position field
        self.domicilio = Entry(self.ven, fg="gray")  # Español: Campo domicilio / English: Address field
        self.placeholder3 = "Dimicilio"  # Español: Texto guía domicilio / English: Address placeholder text
        self.domicilio.insert(0, self.placeholder3)  # Español: Insertar texto guía / English: Insert placeholder text
        self.domicilio.bind("<FocusIn>", self.quitar_placeholder3)  # Español: Evento al enfocar / English: Focus in event
        self.domicilio.bind("<FocusOut>", self.poner_placeholder3)  # Español: Evento al desenfocar / English: Focus out event
        self.domicilio.bind("<Return>", self.ValidarCaja)  # Español: Evento Enter / English: Enter key event
        self.domicilio.place(x=230, y=10, width=100)  # Español: Posicionar campo / English: Position field
        Label(self.ven, text='Sexo').place(x=10, y=30)  # Español: Etiqueta sexo / English: Gender label
        self.modo = StringVar(value='F')  # Español: Variable para sexo / English: Variable for gender
        Radiobutton(self.ven, text='F', variable=self.modo, value='F').place(x=10, y=50)  # Español: Radio femenino / English: Female radio
        Radiobutton(self.ven, text='M', variable=self.modo, value='M').place(x=10, y=70)  # Español: Radio masculino / English: Male radio
        self.lista = Listbox(self.ven, height=8, width=35, activestyle="dotbox", fg="Black")  # Español: Lista para personas / English: List for people
        self.lista.place(x=10, y=100)  # Español: Posicionar lista / English: Position list
        Button(self.ven, text='Agregar', command=self.ValidarCaja, width=10).place(x=230, y=100, width=100, height=50)  # Español: Botón agregar / English: Add button
        self.ven.mainloop()  # Español: Iniciar loop principal / English: Start main loop
        
    def ValidarCaja(self, event=0):  # Español: Validar y agregar datos / English: Validate and add data
        a = False  # Español: Bandera nombre válido / English: Name valid flag
        b = False  # Español: Bandera teléfono válido / English: Phone valid flag
        if (self.nombre.get() == self.placeholder1 or  # Español: Verificar campos con texto guía / English: Check fields with placeholder
            self.telefono.get() == self.placeholder2 or
            self.domicilio.get() == self.placeholder3 or
            self.domicilio.get() == ""):  # Español: O domicilio vacío / English: Or address empty
            messagebox.showerror('Error','Faltan datos')  # Español: Mostrar error / English: Show error
        else:  # Español: Si todos los campos tienen datos / English: If all fields have data
            nombre = self.nombre.get()  # Español: Obtener nombre / English: Get name
            telefono = self.telefono.get()  # Español: Obtener teléfono / English: Get phone
            domicilio = self.domicilio.get()  # Español: Obtener domicilio / English: Get address
            if self.modo.get() == 'F':  # Español: Determinar sexo / English: Determine gender
                sexo = 'Femenino'  # Español: Femenino / English: Female
            else:  # Español: Si es masculino / English: If male
                sexo = 'Masculino'  # Español: Masculino / English: Male
            if self.val.ValidarLetra(nombre):  # Español: Validar nombre / English: Validate name
                a = True  # Español: Marcar válido / English: Mark valid
            else:  # Español: Si nombre inválido / English: If name invalid
                self.nombre.delete(0, END)  # Español: Limpiar campo / English: Clear field
                messagebox.showerror('Error','Nombre incorrecto')  # Español: Mostrar error / English: Show error
            if self.val.ValidarNumeros(telefono):  # Español: Validar teléfono numérico / English: Validate numeric phone
                if len(telefono) == 10:  # Español: Validar longitud teléfono / English: Validate phone length
                    b = True  # Español: Marcar válido / English: Mark valid
                else:  # Español: Si longitud incorrecta / English: If length incorrect
                    self.telefono.delete(0, END)  # Español: Limpiar campo / English: Clear field
                    messagebox.showerror('Error','Telefono incorrecto')  # Español: Mostrar error / English: Show error
            else:  # Español: Si teléfono no numérico / English: If phone not numeric
                self.telefono.delete(0, END)  # Español: Limpiar campo / English: Clear field
                messagebox.showerror('Error','Telefono incorrecto')  # Español: Mostrar error / English: Show error
            if a == True and b == True:  # Español: Si ambos válidos / English: If both valid
                clabe = nombre[0]+telefono[0]+domicilio[0]  # Español: Generar clave / English: Generate key
                persona = clabe+"-"+nombre+"-"+telefono+"-"+domicilio+"-"+sexo  # Español: Crear registro persona / English: Create person record
                self.lista.insert(self.lista.size()+1, persona)  # Español: Insertar en lista / English: Insert into list
                
if __name__ == '__main__':  # Español: Si es ejecutado directamente / English: If executed directly
    app = Ventana()  # Español: Crear instancia / English: Create instance
    app.Inicio()  # Español: Iniciar aplicación / English: Start application