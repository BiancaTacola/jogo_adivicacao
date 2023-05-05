print("*----------------------------------*")
print("Bem vindo ao jogo de adivinhação!")
print("*----------------------------------*")

#Este é o numero secreto que o usuário deve adivinhar
numero_secreto= 33

#Aqui indicamos str para que seja possivel comparar valores numéricos
chute_str = input("Por favor digite um número:")
print("Você digitou", chute_str)

chute = int(chute_str)

# = Atribuindo o valor a variavel
# == for igual ao valor da variavel

acertou = numero_secreto == chute
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if (acertou):
    print("Você acertou!")  # 4 espaços é obrigatório no python para mostrar que estamos dentro da função
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto")
    elif(menor):
        print("Você errou! O seu chute foi maior que o número secreto")

print("*----------------------------------*")
print("Fim do jogo!")