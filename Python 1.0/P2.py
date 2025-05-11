def numero_vogal(tentativa):
  vogais = 'aeiouAEIOUáàâãóòôèéêíìúù'
  cont = 0
  for letra in tentativa:
    if letra in vogais:
      cont +=1
  return cont

x = (input('digite uma palavra: '))
r = numero_vogal(x)
print(f'a palavra {x} tem {r} vogais')