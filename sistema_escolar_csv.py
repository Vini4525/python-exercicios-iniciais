import csv
from ex007 import definir_situacao, ler_notas


def Cadastrar_aluno():

    Nome = input('Digite o nome do aluno: ').title()
    n1, n2 = ler_notas()
    m = (n1 + n2)/2
    sit = definir_situacao(m)

    with open('alunos.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([Nome, n1, n2, m, sit])

    print('aluno cadastrado com sucesso!\n')

def mostrar_alunos():

    alunos = []

    try:
        with open('alunos.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                alunos.append(row)

        for aluno in sorted(alunos, key=lambda aluno: aluno["Nome"]):

            print(f'Nome: {aluno["Nome"]}')
            print(f'Primeira Nota: {aluno["N1"]}')
            print(f'Segunda Nota: {aluno["N2"]}')
            print(f'Média: {aluno["m"]}')
            print(f'Situação: {aluno["sit"]}')
            print('-' * 30)
        if len(alunos) == 0:
            print('O sistema está sem alunos!')

    except FileNotFoundError:
        print('o arquivo não existe!')

def buscar_aluno():
    nm = input('Digite o nome do aluno: ').title().strip()
    try:
        with open('alunos.csv', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Nome'] == nm:

                    print(f'Nome: {row["Nome"]}')
                    print(f'Primeira Nota: {row["N1"]}')
                    print(f'Segunda Nota: {row["N2"]}')
                    print(f'Média: {row["m"]}')
                    print(f'Situação: {row["sit"]}')
                    print('-' * 30)

                    return

            print('aluno não encontrado')

    except FileNotFoundError:
        print('O arquivo não existe!')



#-----------------------------------------------------------------------------------------------------------------

print('Bem vindo ao sistema escolar!')
print('\n1- Cadastrar aluno')
print('2- Ver todos os alunos')
print('3- Buscar aluno pelo nome')
print('4- sair' )
print('-' * 30)

while True:
    try:
        o = int(input('Digite uma opção: '))
        if o == 1:
            Cadastrar_aluno()
        elif o == 2:
            mostrar_alunos()
        elif o == 3:
            buscar_aluno()
        elif o == 4:
            print('Saindo do sistema...')
            break
        else:
            print('Digite uma opção válida!')
    except ValueError:
        print('Digite uma opção válida!')











