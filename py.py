import random

def escolher_palavra():
    palavras = ["programacao", "python", "jogo", "terminal", "forca", "desenvolvimento"]
    return random.choice(palavras).upper()

def exibir_status(palavra, letras_acertadas):
    return " ".join([letra if letra in letras_acertadas else "_" for letra in palavra])

def jogar():
    print("Bem-vindo ao Jogo da Forca!")
    palavra = escolher_palavra()
    letras_acertadas = set()
    letras_erradas = set()
    tentativas = 6
    
    while tentativas > 0:
        print("\n" + exibir_status(palavra, letras_acertadas))
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas}")
        
        tentativa = input("Digite uma letra: ").upper()
        
        if tentativa in letras_acertadas or tentativa in letras_erradas:
            print("Você já tentou essa letra!")
        elif tentativa in palavra:
            letras_acertadas.add(tentativa)
            print("Boa! Você acertou uma letra!")
        else:
            letras_erradas.add(tentativa)
            tentativas -= 1
            print("Ops! Essa letra não está na palavra.")
        
        if set(palavra) == letras_acertadas:
            print(f"\nParabéns! Você acertou a palavra: {palavra}")
            break
    else:
        print(f"\nGame Over! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar()
