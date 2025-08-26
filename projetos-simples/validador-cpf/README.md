# Projeto 5: Validador de CPF em Python

Uma aplicação de terminal completa para validar números de CPF com base no algoritmo oficial da Receita Federal. Este projeto implementa todas as etapas de verificação, incluindo a limpeza da entrada, a checagem de formatos inválidos e o cálculo dos dois dígitos verificadores.

## Funcionalidades

-   **Menu Interativo**: O programa roda em um loop contínuo, permitindo validar múltiplos CPFs ou sair.
-   **Limpeza de Entrada**: Aceita CPFs com ou sem formatação (pontos `.` e traços `-`), limpando a string para análise.
-   **Validação de Formato**:
    -   Verifica se a entrada contém apenas números, rejeitando letras ou outros símbolos.
    -   Verifica se o CPF tem 11 dígitos.
    -   Implementa a regra de negócio que invalida CPFs com todos os dígitos repetidos (ex: `111.111.111-11`).
-   **Cálculo dos Dígitos Verificadores**:
    -   Calcula o primeiro dígito verificador com base nos 9 primeiros dígitos do CPF.
    -   Calcula o segundo dígito verificador com base nos 9 primeiros dígitos mais o primeiro dígito calculado.
-   **Veredito Final**: Compara o CPF gerado pelo algoritmo com o CPF inserido pelo usuário para determinar se ele é **VÁLIDO** ou **INVÁLIDO**.

## Como Usar

1.  Clone o repositório.
2.  Navegue até a pasta `projetos-simples/validador-cpf/`.
3.  Execute o script no seu terminal:
    ```bash
    python nome_do_seu_arquivo.py
    ```
4.  Siga as instruções para validar um CPF ou sair do programa.

## Conceitos Aplicados

Este projeto foi um desafio significativo que me permitiu aplicar e aprofundar os seguintes conceitos:

-   **Implementação de Algoritmos**: Tradução de um algoritmo matemático complexo e com múltiplas etapas para um código Python funcional.
-   **Manipulação Avançada de Strings**: Uso de fatiamento (slicing) para extrair partes do CPF (`cpf[:9]`), concatenação para construir novos CPFs e laços `for` para limpar e analisar a entrada.
-   **Lógica de Validação em Múltiplas Camadas**: Criação de um funil de validações que garante a integridade dos dados antes de realizar o cálculo principal.
-   **Técnica Inteligente de Verificação**: Uso da multiplicação de strings (`caracter_repetido = cpf_tratado[0] * len(cpf_tratado)`) como uma forma criativa e eficiente de detectar CPFs com dígitos repetidos.
-   **Controle de Fluxo com `continue`**: Para reiniciar o loop principal eficientemente após detectar uma entrada inválida.