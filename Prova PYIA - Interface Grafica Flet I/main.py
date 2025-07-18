import flet as ft

def main(page: ft.Page):
    
    
    page.title = "Lista de Tarefas"
    
    
    campo_tarefa = ft.TextField(hint_text="Nova Tarefa")
    
    
    lista_tarefas = ft.Column()
    
    
    def adicionar_tarefa(e):
        if campo_tarefa.value != "":
            tarefa = ft.Text(campo_tarefa.value)
            
            lista_tarefas.controls.append(tarefa)
            
            campo_tarefa.value = ""
            
            page.update()
            
    
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar Tarefa",
        on_click=adicionar_tarefa)
    
    
    layout = ft.Column(
        controls=[
            ft.Text("Bem vindo a Lista de Tarefas"),
            campo_tarefa,
            botao_adicionar,
            lista_tarefas
        ]
    )
    
    
    page.add(layout)


ft.app(target=main)