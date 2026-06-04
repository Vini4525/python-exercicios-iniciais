alunos = []

class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def definir_situacao(self):

        m = self.calcular_media()

        if m >= 7:
            return 'Aprovado'

        elif m >= 5:
            return 'Rec'

        else:
            return 'Reprovado'



def buscar_aluno():
    nome = input("Digite o nome do aluno: ")
    for aluno in alunos:
        if aluno.nome == nome.title().strip():

            media = aluno.calcular_media()
            sit = aluno.definir_situacao()

            print(f'Nome: {aluno.nome}\n'
                  f'Nota1: {aluno.nota1}\n'
                  f'Nota2: {aluno.nota2}\n'
                  f'Media: {media:.2f}\n'
                  f'Situacao: {sit}')
            return

    print('Aluno não encontrado')


def cadastrar_aluno():
    try:
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))

        if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0:
            raise ValueError('Digite uma nota válida de 0 a 10')

        aluno = Aluno(nome.title().strip(), nota1, nota2)
        alunos.append(aluno)

        print('aluno cadastrado com sucesso')

    except ValueError:
        print('Notas inválidas')


def mostrar_alunos():

    if len(alunos) == 0:
        print('Nenhum aluno cadastrado!')
        return

    for aluno in alunos:

        media = aluno.calcular_media()
        sit = aluno.definir_situacao()

        print('-' *30)
        print(f'Nome: {aluno.nome}\n'
              f'Nota1: {aluno.nota1}\n'
              f'Nota2: {aluno.nota2}\n'
              f'Media: {media:.2f}\n'
              f'Situacao: {sit}')


def main():
    print('Bem vindo ao sistema escolar!')
    print('designed by Vinicius Mahon')

    while True:
        print('\n1- Cadastrar aluno')
        print('2- Ver todos os alunos')
        print('3- Buscar aluno pelo nome')
        print('4- sair')
        print('-'*30)

        try:
            opcao = int(input('Digite sua opcao: '))
            if opcao == 1:
                cadastrar_aluno()
            elif opcao == 2:
                mostrar_alunos()
            elif opcao == 3:
                buscar_aluno()
            elif opcao == 4:
                print('Saindo...')
                break
            else:
                print('Opcao invalida!')
        except ValueError:
            print('Opcao invalida!')


if __name__ == '__main__':
    main()



