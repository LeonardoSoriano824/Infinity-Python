from quarto import Quarto
from cliente import Cliente

class Reserva:
    def __init__(self, dono_reserva, quarto_reserva, data_in_out, status_reserva):
        self.__dono_reserva = dono_reserva
        self.__quarto_reserva = quarto_reserva
        self.__data_in_out = data_in_out
        self.__status_reserva = status_reserva

    # Get dono_reserva
    def get_dono_reserva(self):
        return self.__dono_reserva

    # Set dono_reserva
    def set_dono_reserva(self, novo_dono):
        if isinstance(novo_dono, Cliente):
            self.__dono_reserva = novo_dono
        else:
            print("Cliente inválido! Precisa ser um objeto da classe Cliente.")

    # Get quarto_reserva
    def get_quarto_reserva(self):
        return self.__quarto_reserva

    # Set quarto_reserva
    def set_quarto_reserva(self, novo_quarto):
        if isinstance(novo_quarto, Quarto):
            self.__quarto_reserva = novo_quarto
        else:
            print("Quarto inválido! Precisa ser um objeto da classe Quarto.")

    # Get data_in_out
    def get_data_in_out(self):
        return self.__data_in_out

    # Set data_in_out
    def set_data_in_out(self, nova_data_in_out):
        if isinstance(nova_data_in_out, (list, tuple)) and len(nova_data_in_out) == 2:
            self.__data_in_out = nova_data_in_out
        else:
            print("data_in_out deve ser uma lista ou tupla com data de entrada e saída.")

    # Get status_reserva
    def get_status_reserva(self):
        return self.__status_reserva

    # Set status_reserva
    def set_status_reserva(self, novo_status):
        if novo_status in ['Ativa', 'Cancelada', 'Concluída']:
            self.__status_reserva = novo_status
        else:
            print("Status inválido! Use: 'Ativa', 'Cancelada' ou 'Concluída'.")
            
    
    def exibir_informacoes(self):
        print(f"Dono: {self.__dono_reserva}")
        print(f"Quarto: {self.__quarto_reserva}")
        print(f"Período: {self.__data_in_out}")
        print(f"Status: {self.__status_reserva}")
