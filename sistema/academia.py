alunos = []

while True:
    print("\n=== Academia ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Sair")

    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == "1":

        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno:"))
        telefone = input("Digite o telefone: ")

        print("\nPlanos Disponíveis:")
        print("1. Plano Básico - R$ 100/mês")
        print("2. Plano Premium - R$ 180/mês")
        print("3. Plano Vip - R$ 250/mês")

        opcao = input("Escolha o plano (1, 2 ou 3): ")

        if opcao == "1":
            plano = "Plano Básico"
            valor = 100.00

        elif opcao == "2":
            plano = "Plano Premium"
            valor = 180.00

        elif opcao == "3":
            plano = "Plano Vip"
            valor = 250.00

        else:
            print("Plano inválido!")
            continue

        aluno = {
            "nome": nome,
            "idade": idade,
            "telefone": telefone, 
            "plano": plano,
            "valor": valor
        }

        alunos.append(aluno)

        print("Aluno cadastrado com sucesso!")

    elif opcao_menu == "2":

        if len(alunos) == 0:
            print("Nenhum alunos cadastrado.")

        for aluno in alunos:
            print("\n=== DADOS DO ALUNO ===")
            print(f"Nome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Telefone: {aluno['telefone']}")
            print(f"Plano: {aluno['plano']}")
            print(f"Valor: R${aluno['valor']:.2f}")

    elif opcao_menu == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")