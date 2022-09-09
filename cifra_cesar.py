frase = input("Insira a frase criptografada: ")
frase = frase.upper()
chave = int(input("Insira a chave: "))
frase_decriptada = ""

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", 
            "I", "J", "K", "L", "M", "N", "O", "P", 
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

alfabeto_cesar = []

for letra in alfabeto[chave:len(alfabeto)+1]:
    alfabeto_cesar.append(letra)

for letra in alfabeto[0:chave]:
    alfabeto_cesar.append(letra)

for caractere in frase:
    if caractere in alfabeto_cesar:
        posicao = alfabeto_cesar.index(caractere)
        caractere = alfabeto[posicao]
        frase_decriptada = frase_decriptada + caractere
        frase_decriptada = frase_decriptada.capitalize()
            
    if caractere == ' ':
        caractere = ' '
        frase_decriptada = frase_decriptada + caractere

print(frase_decriptada)
