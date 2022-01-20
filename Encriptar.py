def encriptar(escolhaInicial):

    mensagem = input("Digite o texto que você quer encriptar: ")
    cp = int(input("Digite a sua chave pública: ")
    mensagemEncriptada = [ord(x) - 95 for x in mensagem]

    novaMsgmEncrip = str(mensagemEncriptada)
    
    arquivo = open("arquivo.txt", "a")
    arquivo.writelines(novaMsgmEncrip + '\n')
    
    print("Sua mensagem encriptada é:", novaMsgmEncrip)
