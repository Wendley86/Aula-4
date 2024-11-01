## Sistema de gerenciamento de estoque

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


# Teste cadastro de produto
produtos = []
contador = 0
contador = cadastrar_produto(produtos, contador)
consultar_produto_id(produtos, contador)
