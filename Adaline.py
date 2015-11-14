#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Adaline network implementation
# The network learns if certain animal has two or four feet.
# fourfeet = 1, twofeet = -1
# dog = [-1,-1,1,1] | answer = 1
# cat = [1,1,1,1] | answer = 1
# horse = [1,1,-1,1] | answer = 1
# man = [-1,-1,-1,1] | answer = -1

# (sinapses)
w = [0,0,0,0]
# input
x = [[-1,-1,1,1],
     [1,1,1,1],
     [1,1,-1,1],
     [-1,-1,-1,1]]
# expected answers
t = [1,1,1,-1]
# bias (ajuste fino)
b = 0
# output
y = 0
# numero maximo de interacoes
max_int = 1000
# taxa de aprendizado
taxa_aprendizado = 0.0025
#soma
soma = 0

# nome do animal
animal = ""
# resposta = acerto ou falha
resposta = ""

# dicionario de dados
d = {'-1,-1,1,1' : 'cao', 
     '1,1,1,1' : 'gato', 
     '1,1,-1,1' : 'cavalo',
     '-1,-1,-1,1' : 'homem' }

print("Treinando")

# funcao para converter listas em strings
def listToString(list):
    s = str(list).strip('[]')
    s = s.replace(' ', '')
    return s

# inicio do algoritmo
for k in range(1,max_int):
    acertos = 0    
    print("INTERACAO "+str(k)+"-------------------------")
    for i in range(0,len(x)):
        soma = 0
        
        # pega o nome do animal no dicionário
        if d.has_key(listToString(x[i])):
            animal = d[listToString(x[i])]  
        else:
            animal = ""
            
        # para calcular a saida do adaline, cada entrada de x eh multiplicada
        # pelo seu peso w correspondente
        for j in range(0,len(x[i])):
            soma += x[i][j] * w[j]

        # a saida eh igual a soma anterior
        y_in = soma
        #print("y_in = ",str(y_in))        
                  

        # funcao de ativação
        if y_in >= 0:
            y = 1       
        else:
            y = -1
            
        # atualiza os pesos
        for j in range (0,len(w)):                
           # regra delta
           w[j] = w[j] + taxa_aprendizado * (t[i] - y_in) * x[i][j]        
        
        if y == t[i]:
            acertos+=1
            resposta = "acerto"
        else:
            resposta = "erro"
        
        #imprime a resposta
        if y == 1:
            print(animal+" = quadrupede = "+resposta)
        elif y == 0:
            print(animal+" = padrao nao identificado = "+resposta)
        elif y == -1:
            print(animal+" = bipede = "+resposta)
            
    if acertos == len(x):
        print("Funcionalidade aprendida com "+str(k)+" interacoes")
        break
    print("")
print("Finished")