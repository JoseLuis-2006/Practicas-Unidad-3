class validar():  # Español: Clase para validaciones / English: Validation class
    def __init__(self):  # Español: Constructor de la clase / English: Class constructor
        self.con = 0  # Español: Contador para recursión / English: Counter for recursion
        
    def ValidarNumeros(self,num):  # Español: Validar si es número / English: Validate if it's a number
        if self.con >= len(num):  # Español: Si se recorrió toda la cadena / English: If entire string was traversed
            self.con = 0  # Español: Reiniciar contador / English: Reset counter
            return True  # Español: Retornar verdadero / English: Return true
        if ord(num[self.con])>=47 and ord(num[self.con])<=58:  # Español: Verificar si es dígito (0-9) / English: Check if it's a digit (0-9)
            self.con +=1  # Español: Incrementar contador / English: Increment counter
            return self.ValidarNumeros(num)  # Español: Llamada recursiva / English: Recursive call
        else:  # Español: Si no es dígito / English: If not a digit
            self.con = 0  # Español: Reiniciar contador / English: Reset counter
            return False  # Español: Retornar falso / English: Return false
            
    def ValidarLetra(self, dato):  # Español: Validar letras en cadena / English: Validate letters in string
        if dato == "":  # Español: Si cadena vacía / English: If string empty
            return True  # Español: Retornar verdadero / English: Return true
        if ord(dato[0])>=65 and ord(dato[0])<=90 or ord(dato[0])>=97 and ord(dato[0])<=122 or ord(dato[0]) == 32:  # Español: Verificar si es letra o espacio / English: Check if letter or space
            return self.ValidarLetra(dato[1:])  # Español: Llamada recursiva con resto de cadena / English: Recursive call with remaining string
        else:  # Español: Si carácter no válido / English: If character not valid
            return False  # Español: Retornar falso / English: Return false
            
    def ValidarEntradas(self,dato):  # Español: Validar longitud de entrada / English: Validate input length
        if dato=="":  # Español: Si está vacío / English: If empty
            return False  # Español: Retornar falso / English: Return false
        if len(dato) == 2:  # Español: Si longitud es 2 / English: If length is 2
            return True  # Español: Retornar verdadero / English: Return true
        else:  # Español: Si longitud no es 2 / English: If length is not 2
            return False  # Español: Retornar falso / English: Return false