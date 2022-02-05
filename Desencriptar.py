def desencriptar(escolhaInicial):

    # Pede o texto para o usuário

    mensagem = input("Digite o texto que você quer desencriptar: ")

    # Decodifica a mensagem
    def decodify(char):
        decodified = list()
        i = 0
        while (i < len(char)):
            digit = int(str(char[i])+str(char[i+1]))
            if (digit == 28):
                decodified.append(' ')
            else:
                decodified.append(chr(digit+63))
            i += 2
        

        return decodified
    

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
        mensagemDesencriptada = ''.join(decodify(mensagem))

        arquivo = open("mensagem_desencriptada.txt", "w")
        arquivo.writelines(mensagemDesencriptada)
    
        print("Sua mensagem desencriptada é:", mensagemDesencriptada)
    else:
        print("Chave negada")

