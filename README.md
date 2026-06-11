# GoNext Lite 🚀

O **GoNext Lite** é um gerenciador de tarefas via Interface de Linha de Comando (CLI) desenvolvido em Python, projetado para auxiliar estudantes de tecnologia na organização de suas rotinas de estudos.

> **Deploy:** Para executar esta aplicação CLI, basta clonar este repositório público, configurar o banco de dados e rodar o script no seu terminal.

## ✨ Entrega Final (Trabalho em Equipe e Banco de Dados)
- **Integração com Banco de Dados em Nuvem:** Os dados (tarefas) deixaram de ser salvos na memória e agora são persistidos e sincronizados em um banco de dados PostgreSQL na nuvem utilizando **Supabase**.
- **Code Review e Colaboração:** Projeto desenvolvido em equipe utilizando a cultura de Pull Requests e Code Review.
- **Integração Contínua (CI):** Testes automatizados rodando no GitHub Actions.

## 👥 Equipe
- Samuel [Seu Sobrenome] - Matrícula: [Sua Matrícula]
- [Nome da sua Dupla] - Matrícula: [Matrícula dela]

## 🛠️ Nova Stack (Banco de Dados)
- **Supabase** (PostgreSQL) para armazenamento dos dados.
- Biblioteca `supabase` e `python-dotenv` em Python.

## 🚀 Como Executar Localmente

1. **Clonar o Repositório:**
   ```bash
   git clone https://github.com/Samuelrsouzaa/projeto-bootcamp.git
   cd projeto-bootcamp
   ```

2. **Instalar Dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar o Banco de Dados:**
   - Crie um arquivo `.env` na raiz do projeto (como o exemplo abaixo):
   ```env
   SUPABASE_URL=https://gmtzzlsddgtcubjkbczl.supabase.co
   SUPABASE_KEY=sua_chave_aqui
   ```
   - No painel do Supabase, crie a tabela rodando o seguinte SQL:
   ```sql
   CREATE TABLE tarefas (
     id SERIAL PRIMARY KEY,
     titulo TEXT NOT NULL,
     concluida BOOLEAN DEFAULT FALSE,
     criado_em TIMESTAMP WITH TIME ZONE DEFAULT NOW()
   );
   ```

4. **Rodar a Aplicação:**
   ```bash
   python task_manager.py
   ```