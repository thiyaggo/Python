# Lista para armazenar os cadastros.
# Cada cadastro será um dicionário.
cadastros = []

def menu():
    """Exibe o menu de opções."""
    print("\n--- Sistema de Cadastro ---")
    print("1. Cadastrar novo usuário")
    print("2. Fazer login")
    print("3. Listar usuários")
    print("4. Sair")
    return input("Escolha uma opção: ")

def cadastrar_usuario():
    """Coleta informações e adiciona um novo usuário à lista de cadastros."""
    print("\n--- Cadastro de Usuário ---")
    email = input("Digite o email: ")
    senha = input("Digite a senha: ")

    # Verifica se o e-mail já existe
    for usuario in cadastros:
        if usuario['email'] == email:
            print("Erro: Este e-mail já está cadastrado.")
            return

    novo_usuario = {
        'email': email,
        'senha': senha,
    }
    cadastros.append(novo_usuario)
    print("Cadastro realizado com sucesso!")

def fazer_login():
    """Verifica se as credenciais do usuário estão corretas."""
    print("\n--- Login ---")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    for usuario in cadastros:
        if usuario['email'] == email and usuario['senha'] == senha:
            print("Login bem-sucedido! Bem-vindo(a),", email)
            return

    print("Erro: E-mail ou senha incorretos.")

def listar_usuarios():
    """Exibe todos os usuários cadastrados."""
    if not cadastros:
        print("\nNenhum usuário cadastrado ainda.")
    else:
        print("\n--- Lista de Usuários ---")
        for i, usuario in enumerate(cadastros):
            print(f"Usuário {i + 1}:")
            for chave, valor in usuario.items():
                print(f"  - {chave}: {valor}")
            print("-" * 20)

# Loop principal do programa
while True:
    opcao = menu()

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        fazer_login()
    elif opcao == '3':
        listar_usuarios()
    elif opcao == '4':
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")

