# O processamento das notas recebidas serão realizados nesse documento, para ser importado para main.py, por modularização

# Função para receber as notas e nomes dos alunos, e criar uma lista com tuplas

def cadastrar_alunos():
    alunos = []

    while True:
        nome = input("""
Informe o nome do aluno para registrar suas notas
(Ao terminar de registrar os alunos, digite 'sair') : """)

        if nome.lower() == "sair":
            break 

        while True:
            confirmacao = input(f"O nome '{nome}' está correto? (s/n): ").lower()

            if confirmacao in ["s", "n"]:
                break
            print("Digite apenas 's' ou 'n'")

        if confirmacao == "n":
            print("Digite o nome novamente.")
            continue

        notas = []

        while True:
            nota = input(f"""Registre uma nota para {nome}:
(Ao finalizar as notas deste aluno, digite 'fim') : """)

            if nota.lower() == "fim":
                if len(notas) == 0:
                    print("Registre pelo menos uma nota para o aluno.")
                    continue
                break

            try:
                nota = float(nota)

                if nota == 0:
                    while True:
                        confirmacao = input("""ATENÇÃO: Nota zero inserida! Deseja prosseguir? (s/n): 
Digite s para 'Sim', ou n para 'Não': """).lower()
                        if confirmacao in ["s", "n"]:
                            break
                        print("Digite s para 'Sim', ou n para 'Não':")

                    if confirmacao == "n":
                        continue

                if 0 <= nota <= 10:
                    notas.append(nota)
                else:
                    print("Nota deve ser entre 0 e 10.")

            except ValueError:
                print("Valor inválido! Digite apenas números para as notas.")

        alunos.append((nome, notas))

    return alunos

# Fim da função cadastrar_alunos()

# Função para calcular a média das notas de cada aluno

def calcular_media(notas):
    return sum(notas) / len(notas)

# Fim da função calcular_media()

# Funcao para mostrar os resultados

def mostrar_resultados(alunos):
    print("\nResultado dos alunos:\n")

    for nome, notas in alunos:
        media = calcular_media(notas)
        status = "Aprovado" if media >= 7 else "Recuperação"
        quantidade = len(notas)

        print(f"Aluno: {nome}")
        print(f"Notas: {notas}")
        print(f"Quantidade de atividades: {quantidade}")
        print(f"Média: {media:.2f}")
        print(f"Status: {status}")
        print("▪︎" * 50)

# fim da função mostrar_resultados()

# Função para encontrar a maior média de aluno

def encontrar_maior_media(alunos):
    maior_media = 0
    melhores_alunos = []

    for nome, notas in alunos:
        media = calcular_media(notas)

        if media > maior_media:
            maior_media = media
            melhores_alunos = [(nome, media)]

        elif media == maior_media:
            melhores_alunos.append((nome, media))

    return maior_media, melhores_alunos

# Fim da função encontrar_maior_media()