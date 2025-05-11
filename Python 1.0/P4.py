def soma_dos_numeros():
  num1 = float(input("Escolha o primeiro número: "))
  num2 = float(input("Escolha o segundo número: "))

  if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    soma = num1 + num2
    print(f"A soma dos números é: {soma}")
  else:
    print("Os números não atendem à condição para soma.")
soma_dos_numeros() 