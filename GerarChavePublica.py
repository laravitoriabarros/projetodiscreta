import math


e = 0

def gerarChavePublica(escolhaInicial):

    print("Digite dois números primos:")
    p = int(input("Primeiro número:"))
    q = int(input("Segundo número:"))

    ## Agora, vamos declarar duas funções para verificar se os números dados são primos ou não:
    
    def verificacaoPrimoP(p):

        multiplos = 0
       
        ## Aqui vamos utilizar uma estrutura de repetição para verificar se os números dados são primos:
        ## Se não são primos, precisaremos pedi-los de novo!
    
        for contador in range(2, p):
        
            if (p % contador == 0):
        
                multiplos += 1


        if multiplos != 0:
            
            print("O primeiro número digitado não é primo, por favor escolha outro:")
            p = int(input())

            return verificacaoPrimoP(p)


    def verificacaoPrimoQ(q):   
       
        multiplos2 = 0
    
        for cont in range(2,q):
        
                if (q % cont == 0):
        
                    multiplos2 += 1


        if multiplos2 != 0:
            
            print("O segundo número digitado não é primo, por favor escolha outro:")
            q = int(input())

            return verificacaoPrimoQ(q)


    ## Aqui chamamos as funções para que elas possam funcionar:
                
    verificacaoPrimoP(p)
    verificacaoPrimoQ(q)
    
    ## Agora temos que receber o número "e":
            
    print("Agora escolha um número relativamente primo à (p − 1) * (q − 1):")

    global e
    e += int(input())

    N = (p - 1) * (q - 1)

    aux_e = e
    aux_N = N
    if (e > N):
        aux_e = N
        aux_N = e 
    
    ## Agora vamos verificar se o número "e" e o valor da variável "N" são primos entre si:

    ## Aqui criamos uma função para descobrir o MDC de "e" e "N":
    
    def mdc(a, q, d, r):
        if (r == 0):
            return d
        else:
            a = d
            d = r
            q = math.floor(a/d)
            r = a % d 
            return mdc(a, q, d, r)


    mdc2 = mdc(aux_N, math.floor(aux_N/aux_e), aux_e, aux_N%aux_e)    


       ## Se não é 1, temos que pedir outro valor.

        
       ## Caso o valor da função seja 1, significa que os números são coprimos!
   

    while (mdc2 != 1):

        print("O número escolhido não é coprimo à expressão (p - 1) * (q - 1). Por favor, tente novamente!")
        e = int(input("Digite outro valor: "))
        aux_e = e
        ## Aqui chamamos a função mdc para que o novo valor seja computado
        mdc2 = mdc(aux_N, math.floor(aux_N/aux_e), aux_e, aux_N%aux_e)


        


    ## Este comando cria um arquivo e permite que adicionemos algo nele:
        
    arquivo = open("arquivo.txt", "w")


    ## Aqui transformamos as variaveis em string para que possam ser escritas juntas:

    v1 = str(e)
    v2 = str(N)
            
    ## Aqui eu criei a variável "Chave Pública" que vai ser composta pelos números "e" e "N":
            
    chavePublica = v1 + v2
            

    ## Aqui nós escrevemos o valor da chavePublica no arquivo:
            
    arquivo.writelines(chavePublica)

    ## Por fim, avisamos ao usuário qual é sua Chave Pública:

    print("A sua chave pública é: ", chavePublica)

      
