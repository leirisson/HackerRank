#apagenado um registro de um dicionario

Alunos = {"aluno1": "Raimundo", "aluno2": "francisco","aluno3": "zelha","aluno4": "brutos" }


# verificar se existe um valor no dicionarios usamos a chave 
if Alunos["aluno1"]:
    print(f'O aluno {Alunos["aluno1"]} existe !')

# verificar se existe um valor no dicionario chave:valor.value

#delentando
del Alunos["aluno3"]
#print(Alunos)

#mudando o valor usando a chave
Alunos["aluno1"] = 'guiru'
#print(Alunos)


#adcionar elemento
Alunos["adcioandoValor"] = 54
print(Alunos)

#criando um dionario dentro de uma lista
brasil = []
estado1 = {'uf':'Amazonas', 'sigla':'AM'}
estado2 = {'uf':'Coari', 'sigla':'CO'}

brasil.append(estado1)
brasil.append(estado2)

#usando o copy com dcionario

estado = dict()
brasa = list()

for c in range(0,2):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('sigla: '))
    brasil.append(estado.copy())
print(estado)