import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    def enviar_formulario(e):
        if campo_nome.value != "" and campo_email.value != "" and campo_mensagem.value != "":
            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""
            
            page.open(alerta)
            
            page.update()
    
    
    campo_nome = ft.TextField(hint_text="Nome") 
    campo_email = ft.TextField(hint_text="Email") 
    campo_mensagem = ft.TextField(hint_text="Mensagem")
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)
    
    
    alerta = ft.AlertDialog(
    title=ft.Text("Sucesso"),
    content=ft.Text("Formulário enviado com sucesso!")
)
    
    
    layout = ft.Column(
        controls=[
            ft.Text("Formulário de Contato"),
            campo_nome,
            campo_email,
            campo_mensagem,    
            botao_enviar
        ]
    )
    
    page.add(layout)
    
    


ft.app(target=main)