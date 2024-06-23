from forca import palavra # palavra sorteada

letras_usuario = [] # palpite do usuário
chances = 5
ganhou = False

while True:
    # jogo
    print("Bem vindo ao jogo da forca!!")
    
    # exibir espaço vazio e traços
    for letra in palavra:
        if letra.lower() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"voce tem {chances} chances")
    
    # input
    tentativa = input("Escolha uma letra para adivinhar a palavra: ")
    letras_usuario.append(tentativa.lower())
    
    # se errar
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    
    # verifica o erro
    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_usuario:
            ganhou = False
            
    # perdeu
    if chances == 0 or ganhou:
        break 
    
    
if ganhou:
    print(f"Parabéns, você ganhou. A palavra era {palavra}")
else:
    print(f"Voce perdeu! A palavra era {palavra}")

