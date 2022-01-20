from GerarChavePublica import gerarChavePublica
from Encriptar import encriptar
from Desencriptar import desencriptar

## Inicialmente, vamos dar as três opções requeridas no projeto para o usuário:

print("Digite o número correspondete a ação que deseja fazer:")
print("1 - Gerar Chave Pública")
print("2 - Encriptar")
print("3 - Desencriptar")

escolhaInicial = int(input())


## Caso escolha a opção 1:

if escolhaInicial == 1:

    gerarChavePublica(escolhaInicial)


if escolhaInicial == 2:

    encriptar(escolhaInicial)

if escolhaInicial == 3:

    desencriptar(escolhaInicial)
