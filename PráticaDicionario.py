def validacao (pergunta):
  x = pergunta
  if x > 2 or x < 1:
    x = pergunta
  else:
    return x


def mediaIdades(pessoas):
  soma = 0
  for i in range(len(pessoas['AnoNascimento'])):
    idadeAtual = 2026 - (pessoas['AnoNascimento'][i] )
    soma += idadeAtual
  return soma

def mulheres30(pessoas):
    mulheres = []
    for i in range(len(pessoas['Nome'])):
      sexo = pessoas['Sexo'][i].lower()
      if sexo[0] == 'f' or  sexo[:] =='mulher'or sexo =='menina':
          idadeAtual = 2026 - (pessoas['AnoNascimento'][i])
          if idadeAtual < 30: 
            mulheres.append({
              'Nome':pessoas['Nome'][i],
              'AnoNascimento':pessoas['AnoNascimento'][i],
              'Sexo': pessoas['Sexo'][i]

              })

    return  mulheres


def  homensMedia(pessoas):
  homens = []
  qtdHomens = 0
  cadastros = 0

  for i in range(len(pessoas['Nome'])):
    sexo = pessoas['Sexo'][i].lower()
    if sexo[0] == 'h' or  sexo[:] =='menino'or sexo =='masculino':
      idadeAtual = 2026 - (pessoas['AnoNascimento'][i])
      qtdHomens += idadeAtual
      cadastros += 1

  if cadastros == 0:
      return []
  
  media = qtdHomens / cadastros

  for n in range(len(pessoas['Nome'])):
    sexo = pessoas['Sexo'][n].lower()
    if sexo[0] == 'h' or  sexo[:] =='menino'or sexo =='masculino':
      idadeAtual = 2026 - (pessoas['AnoNascimento'][n])
      if media < idadeAtual:
         homens.append({
          'Nome':pessoas['Nome'][n],
          'AnoNascimento':pessoas['AnoNascimento'][n],
          'Sexo': pessoas['Sexo'][n]
        })
         
  return homens


#Comando principal
pessoas = {'Nome':[], 'AnoNascimento':[], 'Sexo':[]}

#MENU

print('Escolha uma pessoa:')
print('1- Cadastrar nova pessoa')
print('2- Sair')

cadastros = 0

while True:

  try: 
    op = validacao(int(input('Opção:')))

    if op == 1:
      nome = input('Qual o seu nome?: ')
      anoNascimento = int(input('Qual o seu ano de nascimento?: '))
      sexo = input('Qual o seu sexo?: ')

      pessoas['Nome'].append(nome)
      pessoas['AnoNascimento'].append(anoNascimento)
      pessoas['Sexo'].append(sexo)

      cadastros += 1

      print('-' * 5)

    elif op == 2:
      print(pessoas)

      print(f'Total de cadastros: {cadastros}')
      if cadastros > 0:

        pes = int(cadastros)
        soma = mediaIdades(pessoas)
        print(f'Media da idade da(s) {cadastros} pessoas = {soma / pes}')
        print(f'Mulheres com menos de 30 anos: {mulheres30(pessoas)}')
        print(f'Homens com idade acima da média: {(homensMedia(pessoas)) }')
        
      else:
        print('Nenhum cadastro foi realizado')

      print('Encerrando...')
      break
    

  except:
    print("Erro ao digitar um número")
    print("Digite a opção novamente")
    continue
     

