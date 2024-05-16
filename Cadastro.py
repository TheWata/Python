produto = ['produto1','produto2','produto3']
preco = ['5,00','7,50','3,50']
codigo = ['1','2','3']
#Adiciona produtos teste para serem consultados
entrada =[]

def cadastrar(novoproduto,novopreco,novocodigo):
    try:
        valor = codigo.index(novocodigo)
        print("Codigo de Produto já cadastrado!")

    except:
        produto.append(novoproduto)
        preco.append(novopreco)
        codigo.append(novocodigo)

def deletar(cod):
    try:
        valor = codigo.index(cod)
        produto.pop(valor)
        preco.pop(valor)
        codigo.pop(valor)
    except:
        print("Um erro ocorreu ao deletar o produto")


def consulta(nome):
    try:
        valor = int(produto.index(nome))
        #procura o nome do produto na lista de produtos
        print('Nome do produto',produto[valor])
        print('Valor do produto',preco[valor])
        print('Codigo do produto',codigo[valor])
    except:
        print("um erro ocorreu ao consultar o produto")



while entrada != 0:
    print('1 - Cadastrar produto')
    print('2 - Consultar produto')
    print('3 - Deletar produto')
    print('4 - Listar produtos')

    entrada= int(input('digite uma opção'))
    if entrada == 1:
        #Cadastro
        cadastraproduto=input("produto: ")
        cadastrapreco=input("preco: ")
        cadastracodigo=input("Codigo do produto: ")
        cadastrar(cadastraproduto,cadastrapreco,cadastracodigo)

    if entrada == 2:
        #Consulta
        nome = input('digite o nome do produto')
        consulta(nome)

    if entrada == 3:
        #Deletar
        cod = input ("Digite o codigo do produto a ser deletado: ")
        res = input("Tem certeza que deseja deletar o seguinte produto? s/n")
        if res == "s":
            deletar(cod)
        else:
            print("Operação Abortada")

    if entrada == 4:
        #Listar produtos
        print(produto)
