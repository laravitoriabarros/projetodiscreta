def desencriptar(escolhaInicial):

    # Criando uma lista com alguns caracteres da tabela ASCII (alfabeto + alguns símbolos) para poder fazer 
    # a decodificação 

    alphabet = list()
    for i in range(32, 127):
        alphabet.append(chr(i))

    # Pede o texto para o usuário

    mensagem = input("Digite o texto que você quer desencriptar: ")

    # Decodifica a mensagem
    def decodify(char, chave):
        index = 0
        decodified = list()
        # Vai letra por letra da mensagem e vê se ela existe na lista que criamos anteriormente
        for i in range(0, len(char)):
            for k in range(0, len(alphabet)):
                # Caso não exista, insere o caractere como ele está 
                if (char[i] not in alphabet):
                    decodified.append(char[i])
                    break
                else:
                    # Caso exista, insere o caractere transposto x caracteres para a trás
                    if (char[i] == alphabet[k]):
                        index = k
                        index = (index - chave) % 75
                        decodified.append(alphabet[index])
                    
        return decodified;
    

    arquivo = open("arquivo.txt", "r")
    cp = False
    for line in arquivo:
        cp = line

    p = int(input("Por favor insira p: "))
    q = int(input("Por favor insira q: "))
    e = input("Por favor insira e: ")

    N = (p - 1) * (q - 1)

    chave = (str(e)) + (str(N))


    if (chave == cp):
        mensagemDesencriptada = ''.join(decodify(mensagem, int(chave)))

        arquivo = open("mensagem_desencriptada.txt", "w")
        arquivo.writelines(mensagemDesencriptada)
    
        print("Sua mensagem desencriptada é:", mensagemDesencriptada)
    else:
        print("Chave negada")

