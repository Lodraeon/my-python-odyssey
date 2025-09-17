# Projeto 6: Gerenciador de Notas de Alunos

Uma aplicação de terminal em Python para gerenciar uma lista de notas. O projeto foi desenvolvido para praticar a manipulação de listas, o design com funções e, principalmente, a criação de um software robusto com tratamento de erros em múltiplas camadas.

## Funcionalidades

-   **Menu Interativo Completo**: Permite ao usuário adicionar, remover, listar notas ou calcular a média.
-   **Adição de Notas**: Valida se a nota inserida é um número e se está no intervalo válido de 0 a 10.
-   **Remoção de Notas**: Permite remover uma nota pelo seu número na lista, com validação para entradas não numéricas e para índices que não existem na lista.
-   **Cálculo de Média e Status**: Calcula a média das notas inseridas e exibe o status do aluno ("Aprovado" ou "Reprovado").
-   **Design Defensivo**: O programa é à prova de falhas, prevendo e tratando praticamente qualquer tipo de entrada incorreta do usuário sem quebrar.

## Como Usar

1.  Clone o repositório.
2.  Navegue até a pasta `projetos-simples/gerenciador-de-notas/`.
3.  Execute o script no seu terminal:
    ```bash
    python nome_do_seu_arquivo.py
    ```

## Conceitos Aplicados

Este projeto foi essencial para aprofundar os seguintes conceitos de software:

-   **Design Orientado a Funções**: Separação de responsabilidades em funções "puras" (que não dependem de estado global) e procedimentos, tornando o código modular e legível.
-   **Programação Defensiva com "Guard Clauses"**: Implementação do padrão de validação `if valor is None: continue` para garantir que a lógica principal do programa só execute com dados seguros.
-   **Tratamento de Exceções Específico**: Uso de `try/except ValueError` para validação de tipo e lógica condicional para prevenir `IndexError` e `ZeroDivisionError`.
-   **Separação de Lógica e Apresentação**: A função de cálculo (`cal_media`) apenas retorna o dado, enquanto o loop principal é responsável por formatar e exibir o resultado para o usuário.
