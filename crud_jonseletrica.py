import os
import time
import json

DB = "servicos.json"

def carregar():
    if not os.path.exists(DB):
        return []
    with open(DB, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except (json.JSONDecodeError, ValueError):
            return []

def salvar(lista_servicos):
    with open(DB, "w", encoding="utf-8") as f:
        json.dump(lista_servicos, f, indent=4, ensure_ascii=False)

def servicos(lista_servicos):
    print(os.system('cls'))
    print("\n=== Lista de Serviços ===")
    if not lista_servicos:
        print("Nenhum serviço encontrado.Cadastre um serviço primeiro.")
        time.sleep(1)
        return
    for i in lista_servicos:
        print(f"\nID: {i['id']} | Serviço: {i['nome']} | Valor: R${i['valor']}")
    time.sleep(1)

def criar_servico(lista_servicos):
    print("\n=== Criar Serviço ===")
    servico  = {}
    novo_id = len(lista_servicos) + 1
    while True:
        try:
            nome_servico = input("Descrição do Serviço: ").strip()
            valor_servico = float(input("Valor do Serviço: R$").strip())
            break
        except ValueError:
            print("Valor inválido.")
            time.sleep(1)
            continue
    servico.update({"id": novo_id, "nome": nome_servico, "valor": valor_servico})
    lista_servicos.append(servico)
    salvar(lista_servicos)
    print("Serviço cadastrado com sucesso.")
    time.sleep(1)

def orcamento(lista_servicos):
    print(os.system('cls'))
    print("\n=== Orçamento Jon's Elétrica ===")
    if not lista_servicos:
        print("Nenhum serviço encontrado. Cadastre um serviço primeiro.")
        time.sleep(1)
        return
    servicos(lista_servicos)
    orcamento_servico = []
    while True:
        try:
            servico_orcamento = int(input("\nDigite o número do serviço desejado ou 0 para sair: "))
        except ValueError:
            print("Entrada inválida.")
            time.sleep(1)
            continue
        if servico_orcamento == 0:
            break
        else:
            servico = None
            for i in lista_servicos:
                if i["id"] == servico_orcamento:
                    servico = i
                    break
            if servico:
                orcamento_servico.append(servico)
                print(f"\nServiço '{servico['nome']}' adicionado ao orçamento!")
            else:
                print("\nServiço não encontrado!")
            time.sleep(0.5)

    if orcamento_servico:
        total = sum(i['valor'] for i in orcamento_servico)
        print(f"\n=== Orçamento Final ===")
        for i in orcamento_servico:
            print(f"- {i['nome']}: R${i['valor']:.2f}")
        print(f"Total a pagar: R${total:.2f}")
        input("\nPressione Enter para voltar ao menu...")
        os.system('cls')

def atualizar_servico():
    pass

def deletar_servico():
    pass

def menu():
    lista_servicos = carregar()
    while True:
        print("\n=== Gerenciamento de Serviços - Jon's Elétrica ===")
        print("1 - Listar Serviços")
        print("2 - Criar Serviços")
        print("3 - Orçamento")
        print("4 - Atualizar Serviços")
        print("5 - Deletar Serviços")
        print("0 - Sair")
        op = int(input("> ").strip())

        if op == 1:
            servicos(lista_servicos)
        elif op == 2:
            criar_servico(lista_servicos)
        elif op == 3:
            orcamento(lista_servicos)
        elif op == 4:
            atualizar_servico()
        elif op == 5:
            deletar_servico()
        elif op == 0:
            print("Saindo do sistema", end="", flush=True)
            for i in range(10):
                time.sleep(0.2)
                print(".", end="", flush=True)
            print()
            break
        else:
            print("Opção inválida.")


menu()