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
