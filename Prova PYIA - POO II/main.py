class Veiculo:
    def movimentar(self):
        print("Veículo está em movimento.")
        

class Carro(Veiculo):
    def movimentar(self):
        print("Carro está dirigindo.")


class Moto(Veiculo):
    def movimentar(self):
        print("Moto está acelerando.")
        

veiculo1 = Veiculo()
carro1 = Carro()
moto1 = Moto()

veiculo1.movimentar()
carro1.movimentar()
moto1.movimentar()