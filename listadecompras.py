print('Bem-vindo à lista!')

lista = []

while True:
    print('\n1 - Adicionar item')
    print('2 - Ver lista')
    print('3 - Remover item')
    print('4 - Sair')

    o = int(input('Escolha uma opção: '))

    if o == 1:
        i = input('Digite o item: ')
        lista.append(i.lower())
        print('Item adicionado!')

    elif o == 2:
        if len(lista) == 0:
            print('A lista está vazia.')
        else:
            for n in range(len(lista)):
                print(f'{n + 1}- {lista[n].title()}')

    elif o == 3:
        if len(lista) == 0:
            print('A lista está vazia. Não há item para remover.')
        else:
            i = input('Digite o item: ')
            if i.lower() in lista:
                lista.remove(i.lower())
                print('Item removido!')
            else:
                print('Esse item não está na lista.')

    elif o == 4:
        print('Obrigado por usar a lista!\nVolte sempre!')
        break

    else:
        print('Digite uma opção válida!')

