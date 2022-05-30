nprovas = int(input('Informe o numero de notas da disciplina: '))
cod = int(input('Informe o codigo do aluno: '))
aprovados = int
reprovados = int
cont = int
media = int
nota = int
soma = int

aprovados = 0
reprovados = 0

while cod != 0:
  soma = 0
  media = 0 
  for cont in nprovas :
    print('informe a nota: ')
    soma = soma + nota
  media = soma / nprovas
  if media >= 7:
      aprovados = aprovados + 1
  else:
      reprovados = reprovados + 1 
  input('Informe o codigo do aluno')
print('o numero de aprovados é: ', aprovados)
print('o numero de reprovados é: ', reprovados)
