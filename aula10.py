#Função para importar randomicamente números inteiros
from random import randint

Q = []

#Aqui é para dizer que o código vai por 20x adicionar no final da lista um número entre 1 e 100
for numero in range (20):
    Q.append (randint(1,100))

#Variável de controle
maior = -1
menor = 101
for item_da_lista in Q:
    if maior < item_da_lista:
        maior = item_da_lista

    if menor > item_da_lista:
        menor = item_da_lista

print('Lista de números')
print(Q)
print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

print(max(Q))
print(min(Q))