# CRUD_JONS_ELETRICA

Sistema de gerenciamento de serviços elétricos para empre Jons Elétrica com funcionalidades CRUD (Create, Read, Update, Delete) e geração de orçamentos.

## Funcionalidades

- **Listar Serviços**: Exibe todos os serviços cadastrados com seus respectivos preços.
- **Criar Serviços**: Adiciona novos serviços ao catálogo.
- **Ler Serviço por ID**: Busca e exibe um serviço específico pelo seu identificador único.
- **Atualizar Serviços**: Modifica o nome ou o preço de um serviço existente.
- **Deletar Serviços**: Remove um serviço do catálogo.
- **Orçamento**: Gera orçamentos personalizados com base nos serviços selecionados e suas quantidades.

## Requisitos

- Python 3.x instalado

## Como Executar

1. Clone o repositório ou baixe o arquivo `crud_jonseletrica.py`.
2. Abra o terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo foi salvo.
4. Execute o comando:
   ```bash
   python crud_jonseletrica.py
   ```
5. Siga as instruções do menu para gerenciar serviços ou criar orçamentos.

## Outra Forma

1. Abra o arquivo `crud_jonseletrica.py` em um compilador Python.
2. Execute o arquivo.
3. Siga as instruções do menu para gerenciar serviços ou criar orçamentos.

## Estrutura do Projeto

- `crud_jonseletrica.py`: Contém toda a lógica do sistema, incluindo funções CRUD, gerenciamento de arquivos JSON e interface de linha de comando.
- `servicos.json`: Arquivo JSON onde os dados dos serviços são armazenados persistentemente.