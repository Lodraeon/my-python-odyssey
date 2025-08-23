# Projeto 3: Jogo de Adivinhar a Palavra em Python

Um jogo de adivinhação de palavras interativo que roda no terminal, desenvolvido para praticar e consolidar conceitos fundamentais de Python.

## Funcionalidades

-   O jogador deve adivinhar uma palavra secreta, inserindo uma letra por vez.
-   As letras corretas são reveladas na palavra oculta (ex: `*****` -> `*y***`).
-   Validação de entrada: Garante que o jogador insira apenas uma única letra por tentativa.
-   Contador de tentativas que acompanha o desempenho do jogador.
-   Lógica de vitória que encerra o jogo quando a palavra é completada.
-   Suporte para frases com espaços, que são revelados automaticamente no início do jogo para melhorar a experiência.

## 💻 Como Usar

1.  Clone o repositório ou baixe o arquivo `.py`.
2.  Navegue até a pasta do projeto.
3.  Execute o script no seu terminal:
    ```bash
    python jogo_adivinha_palavra.py
    ```
4.  Para alterar a palavra secreta, edite a variável `palavra_secreta` no início do código.

## 🧠 Conceitos Aplicados

Este projeto foi uma excelente oportunidade para aprofundar meu conhecimento em:

-   **Lógica de Jogo**: Estruturação de um programa com um loop principal (`while True`), condições de vitória (`break`) e feedback contínuo para o jogador.
-   **Manipulação Avançada de Strings**:
    -   Compreensão da **imutabilidade** das strings.
    -   **Reconstrução** de strings dentro de um loop para atualizar o estado do jogo.
    -   Uso de métodos como `.isalpha()`, `.lower()`, `len()` e o operador `in` para validações complexas.
-   **Tratamento de Exceções**: Embora a validação principal seja com `if/else`, a estrutura de outros projetos solidificou o conhecimento para criar código defensivo.
-   **Design de Experiência do Usuário (UX)**: Tomada de decisões para tornar o jogo mais amigável, como a conversão automática para minúsculas e a revelação de espaços.