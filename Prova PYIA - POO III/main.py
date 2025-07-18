class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0.0
        
    def depositar(self, valor):
        self.__saldo += valor
        return "Deposito realizado com sucesso!"
    
    def sacar(self, valor):
        if self.__saldo < valor:
            return "Saldo insuficiente."
        else:
            self.__saldo -= valor
            return "Saque concluido com sucesso!"
    
    def exibir_saldo(self):
        print(self.__saldo)


conta1 = ContaBancaria("Leonardo")
print(conta1.depositar(1000))        
print(conta1.sacar(500))        
conta1.exibir_saldo()        