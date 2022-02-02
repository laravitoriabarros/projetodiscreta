def encriptar(escolhaInicial):

    # Criando uma lista com alguns caracteres da tabela ASCII (alfabeto + alguns símbolos)
    
    alphabet = list()
    for i in range(65, 91):
        alphabet.append(chr(i))
    alphabet.append(' ')

    
    # Pede o texto para o usuário
    
    mensagem = input("Digite o texto que você quer encriptar: ")
    mensagem = mensagem.upper()
    chave = int(input("Digite a chave pública: "))

    # Codifica a mensagem
    def codify(char):
        index = 0
        codified = list()

        # Vai letra por letra da mensagem e vê se ela existe na lista que criamos anteriormente
        
        for i in range(0, len(char)):
            for k in range(0, len(alphabet)):
                
                # Caso não exista, insere o caractere como ele está 
                
                if (char[i] not in alphabet):
                    codified.append(char[i])
                    break
                    
                else:
                    
                    # Caso exista, insere o caractere transposto x caracteres para a frente 
                    
                    if (char[i] == alphabet[k]):
                        index = k
                        index = (index + 2) % 29
                        codified.append(index)
                        
        return codified;
    
    msg_to_numbers = codify(mensagem)
    mensagemEncriptada = list()
    for i in msg_to_numbers:
        mensagemEncriptada.append(str(i))
    
    mensagemEncriptada = ''.join(mensagemEncriptada)

    arquivo = open("mensagem_encriptada.txt", "w")
    arquivo.writelines(mensagemEncriptada)
        
    print("Sua mensagem encriptada é:", mensagemEncriptada)
    
