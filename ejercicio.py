class Cuentabancaria:
    pass
    def __init__(self):
        self.nombreC = "Paola Ortiz"
        self.numC =  "0123456"
        self.tipoI = "Taza de Interés Activa"
        self.Saldo = "$600.00"
        
    def imprimir (self):
         return (f"La cuenta contiene la siguiente información \nNombre del Titular: {self.nombreC}\nCon número de cuenta: {self.numC}\nA continuación se le mostrará el interés y el saldo que posee \n{self.tipoI} \nSaldo actual: {self.Saldo}")
       
#Objeto                   
nueva_entrada = Cuentabancaria()
print(nueva_entrada.imprimir())