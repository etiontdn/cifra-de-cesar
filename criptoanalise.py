from cifra import decrypt

# Tabela de frequência das letras na língua portuguesa (%)
FREQ_PT = {
    'a': 14.63, 'b': 1.04,  'c': 3.88,  'd': 4.99,  'e': 12.57, 'f': 1.02,
    'g': 1.30,  'h': 0.78,  'i': 6.18,  'j': 0.39,  'k': 0.02,  'l': 2.78,
    'm': 4.74,  'n': 4.44,  'o': 9.73,  'p': 2.52,  'q': 1.20,  'r': 6.53,
    's': 6.81,  't': 4.34,  'u': 4.63,  'v': 1.58,  'w': 0.01,  'x': 0.21,
    'y': 0.01,  'z': 0.47
}

def calcular_chi_quadrado(texto: str) -> float:
    """Mede a similaridade do texto testado com o idioma Português."""
    letras = [c.lower() for c in texto if c.isalpha()]
    total_letras = len(letras)

    if total_letras == 0:
        return float('inf')

    chi2 = 0.0
    for letra, freq_esperada_pct in FREQ_PT.items():
        esperado = (freq_esperada_pct / 100.0) * total_letras
        observado = letras.count(letra)
        chi2 += ((observado - esperado) ** 2) / esperado

    return chi2

def break_cesar_top_n(cipher_text: str, top_n: int = 3):
    """
    Testa todas as chaves de 1 a 25 e retorna as N melhores opções
    ordenadas pelo menor valor de Chi-Quadrado.
    """
    candidatos = []

    for candidate_k in range(1, 26):
        decrypted_candidate = decrypt(cipher_text, candidate_k)
        score = calcular_chi_quadrado(decrypted_candidate)
        candidatos.append((score, candidate_k, decrypted_candidate))

    # Ordena pelo menor score de Chi-Quadrado (quanto menor, mais próximo do Português)
    candidatos.sort(key=lambda x: x[0])

    # Retorna apenas os N primeiros
    return candidatos[:top_n]


if __name__ == "__main__":
    texto_cifrado = input("Digite o texto cifrado para analisar: ")
    
    if not texto_cifrado.strip():
        print("Texto inválido!")
        exit()

    top_candidatos = break_cesar_top_n(texto_cifrado, top_n=3)

    print("\n--- TOP 3 CANDIDATOS A CHAVE K ---")
    for i, (score, k, texto) in enumerate(top_candidatos, start=1):
        print(f"\n{i}º Lugar -> Chave K = {k} (Chi²: {score:.2f})")
        print(f"   Texto decriptado: {texto}")