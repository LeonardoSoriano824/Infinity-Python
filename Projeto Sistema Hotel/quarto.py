class Quarto:
    def __init__(self, num_quarto, tipo_quarto, preco_diaria, status_disponibilidade):
        self.num_quarto = num_quarto
        self.tipo_quarto = tipo_quarto
        self.__preco_diaria = preco_diaria
        self.__status_disponibilidade = status_disponibilidade
        
        
    # Getter preço
    def get_preco_diaria(self):
        return self.__preco_diaria
    
    # Setter preço
    def set_preco_diaria(self, novo_preco_diaria):
        if novo_preco_diaria > 0:
            self.__preco_diaria = novo_preco_diaria
        else:
            print("O preço precisa ser positivo!")
    
    
    # Getter status
    def get_status_disponibilidade(self):
        return self.__status_disponibilidade
    
    # Setter status
    def set_status_disponibilidade(self, novo_status_disponibilidade):
        if novo_status_disponibilidade in ["Disponível", "Ocupado", "Manutenção"]:
            self.__status_disponibilidade = novo_status_disponibilidade
        else:
            print("Status Inválido!")