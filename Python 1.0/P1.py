num = 1
soma = 0
while num != -1:
  num = int(input('Escreva um número: '))
  soma += num
  if num == -1:
    print(f'O total foi {soma + 1}')
    break