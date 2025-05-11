alunos = {}
for i in range(5):
  nome = input(f"Digite o nome do aluno {i+1}: ")
  nota = float(input(f"Digite a nota do aluno {i+1}: "))
  alunos[nome] = nota

print("Dicionário de alunos e notas:")
alunos