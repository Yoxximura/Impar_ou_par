import random

print("Bem-vindo ao jogo de impar ou par!!!") #Boas-vindas aos jogadores

escolha = str(input("Escolha impar ou par:\n")).strip().lower() #Escolher com qual irá querer jogar

while escolha not in ["ímpar", "impar", "par"]: #Verificando se o jogador escreveu corretamente
    escolha = input("Digite apenas 'ímpar' ou 'par':\n ").strip().lower() #.strip retira todos os espaços e .lower deixa tudo em minuscúlo

if escolha == "par":
    print("O computador será impar")
    escolha_pc = "impar"
else:
    print("O computador será par")
    escolha_pc = "par"

while True:
    try:
        numero_jogador = int(input("Escolha qualquer número de 0 a 9 (somente os números):\n")) #Escolhendo o número do jogador
        if 0 <= numero_jogador <= 9: #Verificado se o número do jogador atende aos requisitos
            break # Sai do loop se o número estiver no intervalo certo
        else:
            print("Número fora do intervalo. Tente novamente.")
    except ValueError:
            print("Entrada inválida. Por favor, digite apenas números inteiros.")
print(f"Você escolheu o número:", numero_jogador)

numero_pc = random.randint(0, 9) #Faz o pc escolher um número aleatório
print(f"O computador escolheu o número:", numero_pc)

soma = numero_jogador + numero_pc #Faz a soma dos resultados
print(f"A soma dos número é:", soma) #Mostra a soma dos resultados

#O resultado é par quando for dividido por 2 e o resultado da o final 0
resultado = "par" if soma % 2 == 0 \
    else "impar"

print(f"Você escolheu:", escolha, "e o Computador escolheu:", escolha_pc)
if resultado == escolha:
    print(f"Você venceu!!! :)")
else:
    print(f"O computador venceu!!! :(")
