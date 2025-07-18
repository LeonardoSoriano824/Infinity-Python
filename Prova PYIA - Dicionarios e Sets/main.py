dicionario_contatos = {}

nome_contato = input("Digite o nome do contato: ")
telefone_contato = input("Digite o telefone do contato: ")
email_contato = input("Digite o email do contato: ")

dicionario_contatos["nome"] = nome_contato
dicionario_contatos["telefone"] = telefone_contato
dicionario_contatos["email"] = email_contato

print(f"Nome: {dicionario_contatos['nome']}")
print(f"Telefone: {dicionario_contatos['telefone']}")
print(f"Email: {dicionario_contatos['email']}")
