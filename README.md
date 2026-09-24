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
