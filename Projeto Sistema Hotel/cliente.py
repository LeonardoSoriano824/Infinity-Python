from pessoa import Pessoa

class Cliente(Pessoa):
    
    _contador_id = 0
    
    def __init__(self, nome, telefone, email, id_cliente):
        super().__init__(nome, telefone, email)
        Cliente._contador_id += 1
        self.id_cliente = Cliente._contador_id 