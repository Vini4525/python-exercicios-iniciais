
print('Bem vindo ao diário!')
print('-' * 30)


while True:
    print('Digite 1 para escrever no diário')
    print('Digite 2 para ler o diário')
    print('Digite 3 para sair')

    try:
        o = int(input('Selecione uma opção: '))

        if o == 1:

            conteudo = input('Escreva: ')

            with open('diario.txt', 'a') as file:

                file.write(f'Anotação:\n{conteudo}\n')

            print('Anotação salva!')

        elif o == 2:

            try:
                with open('diario.txt', 'r') as file:
                    lines = file.readlines()
                    if len(lines) > 0:
                        for line in lines:
                            print(line, end='')
                    else:
                        print('O diário está vazio!\n')
            except FileNotFoundError:
                print('o diário ainda não existe! Faça uma anotação primeiro.')
        elif o == 3:
            print('Fechando diário...')
            break
        else:
            print('Opção invalida!\n')
    except ValueError:
        print('Opção invalida!\n')




