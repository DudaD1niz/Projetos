def calculadora():
  num1 = int(input("Digite o primeiro número desejado: "))
  num2 = int(input("Digite o segundo número desejado: "))
  reg = str(input("Escolha a operação que deseja fazer (+ , -, *, /): "))

  if reg == '+':
    soma = num1 + num2
    print(f'O resultado da soma foi: {soma}')
  elif reg == '*':
    mult = num1 * num2
    print(f'O resultado da sua multiplicação foi: {mult}')
  elif reg == '-':
    men = num1 - num2
    print(f"O resultado da sua subtração foi de: {men}")
  elif reg == '/':
    if num1 or num2 == 0:
      print(f'A divisão por zero não pode ser feita!')
    else:
      div = num1/num2
      print(f'O resultado da divisão é {div}')

calculadora()
