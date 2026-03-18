linhat = ("༟" * 120)
titulo1 = ("GESTÃO DE NOTAS E DESEMPENHO DE ALUNOS")
present = ("""Esta aplicação tem como objetivo auxiliar a equipe de coordenação e docentes na gestão de notas e desempenho acadêmico.
Com esta aplicação, os professores podem cadastrar alunos, atribuir notas e acompanhar o resultado do aluno.""")

print(linhat)
print(titulo1)
print(linhat)
print(present)
print(linhat)

# Importação da função de cadastro de alunos: def cadastrar_alunos() do arquivo processamento.py

print("Vamos começar cadastrando os alunos e suas notas")

from processamento import cadastrar_alunos

alunos = cadastrar_alunos()
print(alunos)
print(linhat)

# Importação da função de cálculo de média: def calcular_media() do arquivo processamento.py

print("Agora vamos calcular a média das notas de cada aluno")

from processamento import calcular_media

for nome, notas in alunos:
    media = calcular_media(notas)
    print(f"A média de {nome} é: {media:.2f}")
