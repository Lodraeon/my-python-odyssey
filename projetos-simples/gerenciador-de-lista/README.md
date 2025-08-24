# Projeto 4: Gerenciador de Lista de Compras (CRUD Básico)

Uma aplicação de terminal para gerenciar uma lista de itens. O projeto simula as operações básicas de um CRUD (Create, Read, Update, Delete), focando em C (Inserir), R (Listar) e D (Apagar).

## Funcionalidades

-   **Adicionar Itens:** Permite que o usuário insira novos itens na lista.
-   **Listar Itens:** Exibe todos os itens da lista com seus respectivos índices.
-   **Apagar Itens:** Permite que o usuário apague um item específico fornecendo seu número (índice).
-   **Validação de Entrada:**
    -   O menu principal só aceita as opções válidas.
    -   A inserção de itens aceita apenas letras e espaços.
    -   A remoção de itens valida se o índice é um número e se ele existe na lista.
-   **Tratamento de Erros Específico:** O programa não quebra com entradas inválidas e fornece feedback claro para o usuário, diferenciando um erro de digitação (`ValueError`) de um índice inexistente (`IndexError`).
-   **Interface Limpa:** Usa `os.system('cls')` para limpar a tela a cada ação, melhorando a experiência do usuário.

## 💻 Como Usar

1.  Clone o repositório.
2.  Navegue até a pasta `projetos-simples/gerenciador-de-lista/`.
3.  Execute o script no seu terminal:
    ```bash
    python lista_app.py
    ```

## Conceitos Aplicados

-   **Estruturas de Dados:** Manipulação da estrutura de dados `list` com os métodos `.append()` e `del`.
-   **Tratamento de Exceções Avançado:** Uso de múltiplos blocos `except` (`ValueError`, `IndexError`) para lidar com diferentes tipos de erro de forma específica.
-   **Funções Nativas:** Uso de `enumerate()` para iteração com índice e valor.
-   **Interação com o Sistema Operacional:** Uso do módulo `os` para limpar a tela do console.
-   **Lógica de Validação Complexa:** Implementação de uma lógica para validar strings que podem conter espaços, mas não números ou outros símbolos.