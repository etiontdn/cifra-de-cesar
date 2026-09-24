'''
Exercício com Cifra de Cesar.
Implementar um algoritmo da cifra de César, em qualquer linguagem.
O deslocamento (chave k) pode variar de 1 a N.
Pode contemplar somente a encriptação (a decriptação não é obrigatória)
'''

def encrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = k % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def decrypt(text, k):
    result = ""
    for char in text:
        if char.isalpha():
            shift = k % 26
            if char.islower():
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            result += char
    return result

# Input definindo a chave k
k = int(input("Digite a chave k (1 a N): "))
if k < 1:
    print("A chave k deve ser maior ou igual a 1.")
    exit()

# Input definindo se quer encriptar ou decriptar
operation = input("Digite 'e' para encriptar ou 'd' para decriptar: ")

while operation.lower() not in ['e', 'd']:
    print("Operação inválida. Digite 'e' para encriptar ou 'd' para decriptar.")
    operation = input("Digite 'e' para encriptar ou 'd' para decriptar: ")

if operation.lower() == 'e':
    text = input("Digite o texto a ser encriptado: ")
    encrypted_text = encrypt(text, k)
    print("Texto encriptado:", encrypted_text)
elif operation.lower() == 'd':
    text = input("Digite o texto a ser decriptado: ")
    decrypted_text = decrypt(text, k)
    print("Texto decriptado:", decrypted_text)