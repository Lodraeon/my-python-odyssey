# Projeto 1: Calculadora Simples em Python

Uma calculadora de linha de comando desenvolvida como parte da minha jornada de aprendizado em Python.

## Funcionalidades

-   Realiza as quatro operações matemáticas básicas: adição, subtração, multiplicação e divisão.
-   Possui um menu interativo para realizar múltiplos cálculos.
-   Validação de entrada do usuário para garantir que apenas números sejam inseridos.
-   Tratamento de erro específico para o caso de divisão por zero.
-   Formatação inteligente do resultado, removendo o `.0` de números inteiros.

## Como Usar

1.  Clone o repositório.
2.  Navegue até a pasta `calculadora/`.
3.  Execute o script no seu terminal:
    ```bash
    python calculadora.py
    ```
4.  Siga as instruções para inserir os números e o operador.

## Conceitos Aplicados

-   **Loops `while`**: Para o menu principal e para a validação insistente da entrada do usuário.
-   **Tratamento de Exceções `try/except ValueError`**: Para garantir que o programa não quebre com entradas não numéricas.
-   **Lógica Condicional `if/elif/else`**: Para selecionar a operação matemática correta e lidar com casos especiais, como a divisão por zero.
-   **Formatação de Strings**: Uso de f-strings com a formatação `:g` para uma exibição de resultados mais limpa.
