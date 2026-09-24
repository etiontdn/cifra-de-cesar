# Cifra de César

Este projeto implementa a Cifra de César em Python. Ele permite criptografar e descriptografar textos usando uma chave numérica.

## Como usar

1. Abra o terminal na pasta do projeto.
2. Execute o script:

```bash
python cifra.py
```

3. Quando o programa pedir:
   - digite a chave `k` (um número inteiro maior ou igual a 1);
   - escolha a operação:
     - `e` para encriptar;
     - `d` para descriptografar;
   - informe o texto.

### Exemplo

```text
Digite a chave k (1 a N): 3
Digite 'e' para encriptar ou 'd' para decriptar: e
Digite o texto a ser encriptado: ola mundo
Texto encriptado: rod pxrgr
```

## Observação

Este projeto foi desenvolvido com ajuda do autocomplete do Copilot, que facilitou a escrita, organização e revisão do código.

## Funcionalidades

- Criptografia de letras maiúsculas e minúsculas;
- Preserva caracteres que não são letras;
- Suporte para descriptografia usando a mesma chave.

## Criptoanálise

Além da cifra e da decifração, o projeto também inclui uma análise automática para tentar descobrir a chave mais provável de uma mensagem cifrada pela Cifra de César.

### Como funciona

O programa:

1. testa todas as chaves possíveis de 1 a 25;
2. descriptografa o texto com cada chave;
3. calcula a frequência das letras do texto resultante;
4. compara essa distribuição com a frequência esperada do português;
5. ordena as chaves pelo resultado mais próximo do idioma;
6. mostra os top 3 candidatos.

### Método usado

A comparação é feita com base em uma tabela de frequência das letras do português e uma medida chamada Chi-quadrado ($\chi^2$). Quanto menor o valor obtido, mais próximo o texto está da distribuição natural do idioma.

Em outras palavras, a chave que produz um texto com frequência de letras mais parecida com o português tende a ser a mais provável.

### Como executar a análise

```bash
python criptoanalise.py
```

Depois, insira o texto cifrado e o programa exibirá os 3 melhores candidatos de chave.

### Exemplo de saída

```text
Digite o texto cifrado para analisar: xlii xli xli

--- TOP 3 CANDIDATOS A CHAVE K ---

1º Lugar -> Chave K = 3 (Chi²: 12.40)
   Texto decriptado: ...

2º Lugar -> Chave K = 2 (Chi²: 15.90)
   Texto decriptado: ...

3º Lugar -> Chave K = 4 (Chi²: 18.10)
   Texto decriptado: ...
```

O programa retorna as 3 chaves mais prováveis, ajudando a identificar a que provavelmente foi usada para cifrar o texto.
