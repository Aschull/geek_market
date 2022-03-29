from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    menu()

def menu() -> None:
    print('====================================================')
    print('==================== Market ========================')
    print('====================================================')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produto')
    print('3 - Comprar Produto')
    print('4 - Vizualisar Carrinho')
    print('5 - Fechar Pedido')
    print('6 - Sair')
    print('====================================================')
    
    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        vizualizar_carrinho()
    elif opcao == 5:
        fechar_pedido()
    elif opcao == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opcao invalida!')
        sleep(2)
        menu() 

def cadastrar_produto() -> None:
    print('Cadastro de Produto')
    print('===================')
    
    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preco do produto: '))

    produto = Produto(nome, preco)
    produtos.append(produto)

    print(f'O produto: {produto.nome} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Lista de Produtos')
        print('=================')

        for produto in produtos:
            print(produto)
            print('---------------------')
            sleep(0.5)
        menu()
    else:
        print('Nao existem produtos cadastrados!')
        sleep(2)
        menu()

def comprar_produto() -> None:
    if len(produtos) > 0:
        print('Informe o codigo do produto que deseja adicionar ao carrinho.')
        print('=============================================================')
        print('================== Produtos Disponoveis =====================')
        for produto in produtos:
            print(produto)
            print('======================================')
            sleep(0.5)

        codigo: int = int(input()) 
        produto: Produto = pega_produto_por_codigo(codigo)

        if produto is not None:
            if len(carrinho) > 0:
                existe_no_carrinho: bool = False
                
                for item in carrinho:
                    qtd: int = item.get(produto)
                    if qtd:
                        item[produto] = qtd + 1 
                        print(f'O produto: {produto.nome} agora possui {qtd + 1} unidades no carrinho.')
                        existe_no_carrinho = True
                        sleep(1)
                        menu()
                if not existe_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(1)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(f'O produto {produto.nome} foi adicionado ao carrinho!')
                sleep(1)
                menu()
        else:
            print(f'O codigo {codigo} e invalido!')
            sleep(1)
            menu()

    else:
        print('Produto inexistente!')
        sleep(0.5)
       # menu()

def vizualizar_carrinho() -> None:
    print('Carrinho.')
    if len(carrinho) > 0:
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('=======================')
                sleep(0.5)
        menu()
    else:
        print('Carrinho vazio.')
        sleep(1)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) > 0:
        valor_total: float = 0
        
        print('Produtos no carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('===============================')
                sleep(0.5)

        print(f'Valor do carrinho: {formata_float_str_moeda(valor_total)}')
        print('Volte Sempre!')
        carrinho.clear()
        sleep(3)
    else:
        print('Nao existem produtos no carrinho!')
        sleep(2)
        menu()

def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    
    return p

if __name__ == '__main__':
    main()
