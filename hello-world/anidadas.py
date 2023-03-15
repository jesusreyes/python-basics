def operacion(cantidad, balance, tipo='deposito'):
    def deposito(cantidad, balance):
        return balance + cantidad 
    
    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad
        else:
            return None
    
    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)

resultado = operacion(10, 30, 'retiro')
print(resultado)