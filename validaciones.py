class Validar():  # Español: Clase para validaciones / English: Validation class
    def __init__(self):  # Español: Constructor de la clase / English: Class constructor
        self.con = 0  # Español: Contador para recursión / English: Counter for recursion


    def ValidarNumeros(self, num):  # Español: Validar si es número / English: Validate if it's a number
        if self.con >= len(num):  # Español: Si se recorrió toda la cadena / English: If entire string was traversed
            self.con = 0  # Español: Reiniciar contador / English: Reset counter
            return True  # Español: Retornar verdadero / English: Return true
        
        if ord(num[self.con]) >= 47 and ord(num[self.con]) <= 58:  # Español: Verificar si es dígito (0-9) / English: Check if it's a digit (0-9)
            self.con += 1  # Español: Incrementar contador / English: Increment counter
            return self.ValidarNumeros(num)  # Español: Llamada recursiva / English: Recursive call
        else:  # Español: Si no es dígito / English: If not a digit
            self.con = 0  # Español: Reiniciar contador / English: Reset counter
            return False  # Español: Retornar falso / English: Return false
        
    def ValidarLetra(self, dato):  # Español: Validar letra mayúscula / English: Validate uppercase letter
        if ord(dato[0]) >= 65 and ord(dato[0])<= 90:  # Español: Verificar código ASCII (A-Z) / English: Check ASCII code (A-Z)
            return True  # Español: Es mayúscula / English: Is uppercase
        else:  # Español: Si no es mayúscula / English: If not uppercase
            return False  # Español: Retornar falso / English: Return false
    
    def ValidarEntradas(self, dato):  # Español: Validar longitud de entrada / English: Validate input length
        if dato == "":  # Español: Si está vacío / English: If empty
            return False  # Español: Retornar falso / English: Return false
        if len(dato) == 2:  # Español: Si longitud es 2 / English: If length is 2
            return True  # Español: Retornar verdadero / English: Return true
        else:  # Español: Si longitud no es 2 / English: If length is not 2
            return False  # Español: Retornar falso / English: Return false
            
    def ValidarNombre(self, nom):  # Español: Validar formato de nombre / English: Validate name format
        c = 0  # Español: Contador de caracteres válidos / English: Valid characters counter
        for i in nom:  # Español: Recorrer cada carácter / English: Iterate through each character
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i)==32):  # Español: Verificar si es letra o espacio / English: Check if letter or space
                c += 1  # Español: Incrementar contador / English: Increment counter
        if c == len(nom):  # Español: Si todos los caracteres son válidos / English: If all characters are valid
            return True  # Español: Retornar verdadero / English: Return true
        else:  # Español: Si hay caracteres inválidos / English: If there are invalid characters
            return False  # Español: Retornar falso / English: Return false
