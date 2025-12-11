# 📝 Lista de Tarefas - CRUD com Python, MySQL e Tkinter

## ℹ️ Sobre o sistema
Este é um sistema de **Lista de Tarefas** desenvolvido em Python, com banco de dados MySQL e interface gráfica com Tkinter.  
Ele permite gerenciar tarefas de forma simples e visual, com operações de **criar, ler, atualizar e deletar (CRUD)**, além da funcionalidade de **marcar tarefas como concluídas**.

---

## ✨ Funcionalidades
- Adicionar novas tarefas com título e descrição.
- Listar todas as tarefas cadastradas com status.
- Atualizar título, descrição e status da tarefa.
- Deletar tarefas selecionadas.
- Marcar tarefas como concluídas com um clique.
- Interface visual intuitiva com cores e Treeview para melhor visualização.

---

## 💻 Requisitos para rodar o sistema
- Python 3.x instalado.
- MySQL Server instalado e em execução.
- Bibliotecas Python:
  - mysql-connector-python
  - tkinter (já incluso no Python)
  
### ⚙️ Instalação das dependências
```bash
pip install mysql-connector-python
```

## 🧱 Estrutura do banco de dados

Banco de dados: lista_tarefas
Tabela: tarefas
| Campo     | Tipo         | Descrição                             |
| --------- | ------------ | ------------------------------------- |
| id        | INT          | Identificador único (PK)              |
| titulo    | VARCHAR(255) | Título da tarefa                      |
| descricao | TEXT         | Descrição da tarefa                   |
| status    | VARCHAR(20)  | Status da tarefa (pendente/concluída) |

### 🛠 Tecnologias usadas
- Python 3.x
- Tkinter (Interface gráfica)
- MySQL (Banco de dados relacional)
- mysql-connector-python (Conector Python <-> MySQL)

## 📂 Estrutura do projeto
```bash
lista_tarefas/
│
├── app.py          # Código principal do CRUD e interface Tkinter
└── README.md       # Documentação do projeto
```

## 🚀 Como usar

1. Abra o terminal e execute o Python:
```bash
python app.py
```
2. A interface gráfica será aberta.

3. Use os campos e botões para adicionar, atualizar, deletar e marcar tarefas como concluídas.

4. Todas as alterações são salvas no banco de dados MySQL.

## 👤 Desenvolvido por Gabriel Tenório.
