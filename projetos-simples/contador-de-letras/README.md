# Projeto 2: Contador de Letras em Python

Um script que analisa uma string fornecida e encontra a letra que aparece com mais frequência, além de contar suas ocorrências.

## Funcionalidades

-   Percorre uma string caractere por caractere.
-   Conta o número de aparições de cada letra na string inteira.
-   Mantém um registro da letra com a maior contagem encontrada até o momento.
-   Ignora espaços em branco na contagem.

## Como Usar

1.  Clone o repositório.
2.  Navegue até a pasta `contador_letras/`.
3.  Execute o script no seu terminal:
    ```bash
    python contador_letras.py
    ```
4.  O resultado será impresso diretamente no terminal. Para analisar uma frase diferente, basta editar a variável `frase` dentro do arquivo.

## Conceitos Aplicados

-   **Loops `while`**: Para iterar sobre a string usando um contador de índice.
-   **Manipulação de Strings**: Acesso a caracteres por índice (`frase[i]`) e uso do método `.count()`.
-   **Lógica de Algoritmo**: Implementação de uma lógica de "competição" para encontrar o valor máximo, utilizando variáveis para armazenar o "recorde" e o "recordista" atual.
-   **Controle de Fluxo**: Uso da declaração `continue` para pular iterações indesejadas (neste caso, os espaços).
