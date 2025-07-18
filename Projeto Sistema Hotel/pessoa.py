class Pessoa:
    def __init__(self, nome, telefone, email):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
    
    # Getter nome
    def get_nome(self):
        return self.__nome
    
    # Setter nome
    def set_nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            print("O nome precisa ser uma string!")
    
    # Getter email
    def get_email(self):
        return self.__email
    
    # Setter nome
    def set_email(self, novo_email):
        if isinstance(novo_email, str):
            self.__email = novo_email
        else:
            print("O email precisa ser uma string!")
    
    # Getter telefone
    def get_telefone(self):
        return self.__telefone
    
    # Setter Telefone
    def set_telefone(self, novo_telefone):
        if isinstance(novo_telefone, str):
            self.__telefone = novo_telefone
        else:
            print("O número de telefone precisa ser uma string!")
        
    # Metodo para exibir informações  
    def exibir_informacoes(self):
        print(f"Nome: {self.__nome}")
        print(f"Email: {self.__email}")
        print(f"Telefone: {self.__telefone}")