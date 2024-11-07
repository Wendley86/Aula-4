from typing import List

class Produto:
    def __init__(self, id: int, nome: str, categoria_id: int, quantidade: int, preco: float):
        self.id = id
        self.nome = nome
        self.categoria_id = categoria_id
        self.quantidade = quantidade
        self.preco = preco

class Categoria:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

class Movimentacao:
    def __init__(self, id: int, data: str, quantidade: int, produto_id: int, tipo_movimentacao: str):
        self.id = id
        self.data = data
        self.quantidade = quantidade
        self.produto_id = produto_id
        self.tipo_movimentacao = tipo_movimentacao

def cadastrar_produto(produtos: List[Produto], contador_produtos: int) -> int:
    id = contador_produtos + 1
    nome = input("Digite o nome do produto: ")
    categoria_id = int(input("Digite a categoria do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    produtos.append(Produto(id, nome, categoria_id, quantidade, preco))
    print(f"Produto {nome} cadastrado com sucesso!")
    return id

def consultar_produto_id(produtos: List[Produto], id: int):
    for produto in produtos:
        if produto.id == id:
            print(f'ID: {produto.id}, Nome: {produto.nome}, Categoria: {produto.categoria_id}, Quantidade: {produto.quantidade}, Preço: {produto.preco}')
            return

def registrar_movimentacao(movimentacoes: List[Movimentacao], contador_movimentacoes: int, produtos: List[Produto]) -> int:
    id = contador_movimentacoes
    produto_id = int(input("Digite o ID do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    tipo_movimentacao = input("Digite o tipo de movimentação:\nE - entrada\nS - saída: ").strip().upper()
    data = input("Digite a data da movimentação (dd/mm/aaaa): ")

    produto_encontrado = next((p for p in produtos if p.id == produto_id), None)
    if produto_encontrado:
        if tipo_movimentacao == 'E':
            produto_encontrado.quantidade += quantidade
        elif tipo_movimentacao == 'S':
            if produto_encontrado.quantidade >= quantidade:
                produto_encontrado.quantidade -= quantidade
            else:
                print("Quantidade insuficiente em estoque.")
                return contador_movimentacoes
        else:
            print("Tipo de movimentação inválido.")
            return contador_movimentacoes

        movimentacoes.append(Movimentacao(id, data, quantidade, produto_id, tipo_movimentacao))
        print("Movimentação registrada com sucesso!")
        return id + 1
    else:
        print("Produto não encontrado.")
        return contador_movimentacoes

def gerar_relatorio_estoque(produtos: List[Produto]):
    print("Relatório de estoque:")
    for produto in produtos:
        print(f"ID: {produto.id}, Nome: {produto.nome}, Quantidade: {produto.quantidade}, Preço: {produto.preco:.2f}")

def gerar_relatorio_movimentacoes(movimentacoes: List[Movimentacao], produto_id: int):
    print(f"Movimentações do produto ID {produto_id}:")
    for movimentacao in movimentacoes:
        if movimentacao.produto_id == produto_id:
            print(f"ID: {movimentacao.id}, Data: {movimentacao.data}, Quantidade: {movimentacao.quantidade}, Tipo: {movimentacao.tipo_movimentacao}")

def Menu():
    import os
    import time
    
    produtos = []
    movimentacoes = []
    contador_produto = 0
    contador_movimentacoes = 0

    while True:
        print("Estamos iniciando...")
        time.sleep(2)
        os.system("clear") or None
        print("#### Seja bem vindo ao SISCONF ####")
        escolha = int(input("Escolha uma ação:\n1 - Cadastrar novo produto\n2 - Consultar produto\n3 - Registrar movimentação\n4 - Consultar movimentos\n5 - Gerar relatório de estoque\n6 - Sair\nSelecione o número: "))
        if escolha == 1:
            while True:
              contador_produto = cadastrar_produto(produtos, contador_produto)
              retornar = int(input("Esclha uma ação:\n1 - Cadastrar novo produto\n2 - Retonar ao menu:"))
              if retornar == 2:
                os.system('clear') or None
                break
        elif escolha == 2:
            while True:
             id_produto = int(input("Qual o ID do produto que deseja consultar: "))
             consultar_produto_id(produtos, id_produto)
             retornar = int(input("Esclha uma ação:\n1 - Consultar novo produto\n2 - Retonar ao menu:"))
             if retornar == 2:
                os.system('clear') or None
                break
        elif escolha == 3:
            contador_movimentacoes = registrar_movimentacao(movimentacoes, contador_movimentacoes, produtos)
            retornar = input("Deseja retornar ao menu? (S/N): ")
            if retornar.upper() == "S":
                os.system('clear') or None
                             
        elif escolha == 4:
            id_produto = int(input("Qual o ID do produto que deseja consultar: "))
            gerar_relatorio_movimentacoes(movimentacoes, id_produto)
        elif escolha == 5:
            gerar_relatorio_estoque(produtos)
            retornar = input("Deseja retornar ao menu? (S/N): ")
            if retornar.upper() == "S":
                os.system('clear') or None
        elif escolha == 6:
            break
        else:
            print("Opção inválida. Tente novamente.")

Menu()
