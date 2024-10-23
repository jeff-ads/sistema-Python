# Dicionário para armazenar os clientes cadastrados
clientes = {}

def cadastrar_cliente():
    # Obter o nickname (ID) do cliente
    nickname = input("Por favor, envie seu nickname (ID): ")
    
    if nickname in clientes:
        print("Esse nickname já está em uso. Tente novamente.")
        return
    
    # Criar um dicionário para armazenar as informações do cliente
    cliente_info = {}
    
    # Obter nome
    cliente_info['nickname'] = nickname
    cliente_info['nome'] = input("Obrigado! Agora, por favor, envie seu nome completo: ")
    
    # Obter telefone
    cliente_info['telefone'] = input("Perfeito! Agora, por favor, envie seu telefone: ")
    
    # Obter endereço
    cliente_info['endereco'] = input("Obrigado! Agora, por favor, envie seu endereço: ")
    
    # Obter data de nascimento
    cliente_info['data_nascimento'] = input("Ótimo! Agora, por favor, envie sua data de nascimento (DD/MM/AAAA): ")
    
    # Armazenar as informações do cliente
    clientes[nickname] = cliente_info
    
    # Exibir as informações do cliente
    print("\nCadastro completo! Aqui estão as informações que você enviou:")
    for key, value in cliente_info.items():
        print(f"{key.capitalize()}: {value}")

# Executar o cadastro
cadastrar_cliente()
