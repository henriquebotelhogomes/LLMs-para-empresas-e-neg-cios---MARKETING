# 🤖 AI Marketing Assistant

### LLM-powered Content Generation System for Marketing

Aplicação desenvolvida para demonstrar integração prática com Large
Language Models (LLMs) na geração estratégica de conteúdo para marketing
digital.

O sistema utiliza **LangChain + Groq (Llama 3.1)** para construir um
agente capaz de gerar textos personalizados com base em plataforma, tom
e tamanho desejado.

Projeto desenvolvido como parte de portfólio técnico voltado para
desenvolvimento de aplicações com IA generativa.

------------------------------------------------------------------------

## 🎯 Objetivo

Demonstrar:

-   Integração estruturada com API de LLM
-   Engenharia de Prompt orientada a contexto
-   Separação modular de responsabilidades
-   Organização de código preparada para evolução
-   Aplicação prática de IA voltada a problemas reais

------------------------------------------------------------------------

## 🏗️ Arquitetura do Projeto

ai-marketing-assistant/

├── app.py \# Interface web (Streamlit)\
├── requirements.txt\
├── .env.example\
│\
├── config/\
│ └── settings.py \# Gerenciamento de variáveis de ambiente\
│\
└── core/\
├── agent.py \# Orquestração do agente\
├── llm.py \# Integração com Groq (LLM)\
└── prompts.py \# Engenharia de prompt

------------------------------------------------------------------------

## ⚙️ Stack Tecnológica

-   Python 3.10+
-   Streamlit
-   LangChain
-   Groq API (Llama 3.1)
-   python-dotenv

------------------------------------------------------------------------

## 🧠 Conceitos de IA Aplicados

-   LLM Integration
-   Prompt Engineering
-   Context Structuring
-   Modular Design
-   Separation of Concerns
-   API-based Model Consumption

------------------------------------------------------------------------

## 🔄 Fluxo de Funcionamento

1.  Usuário informa:
    -   Tema
    -   Plataforma (Instagram, LinkedIn, Blog, etc.)
    -   Tom (Informativo, Inspirador, Urgente, etc.)
    -   Tamanho do conteúdo
2.  O sistema:
    -   Constrói dinamicamente um prompt estruturado
    -   Envia requisição para o modelo via Groq API
    -   Recebe resposta do LLM
    -   Retorna o conteúdo formatado na interface

------------------------------------------------------------------------

## 🔐 Configuração do Ambiente

### 1. Clone o repositório

git clone https://github.com/seu-usuario/ai-marketing-assistant.git\
cd ai-marketing-assistant

### 2. Crie um ambiente virtual

python -m venv venv

Windows:\
venv`\Scripts`{=tex}`\activate  `{=tex}

Mac/Linux:\
source venv/bin/activate

### 3. Instale as dependências

pip install -r requirements.txt

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

GROQ_API_KEY=sua_chave_aqui

------------------------------------------------------------------------

## ▶️ Executando a Aplicação

streamlit run app.py

Acesse no navegador:\
http://localhost:8501

------------------------------------------------------------------------

## 📌 Decisões Técnicas

-   Separação entre interface e lógica de negócio
-   Encapsulamento da integração com LLM
-   Prompt isolado em módulo próprio
-   Uso de variáveis de ambiente para segurança
-   Estrutura preparada para evolução futura (API-first)

------------------------------------------------------------------------

## 🚀 Possíveis Evoluções

-   Conversão para API com FastAPI
-   Implementação de Memory
-   Implementação de RAG (Retrieval-Augmented Generation)
-   Persistência de histórico
-   Deploy em ambiente cloud
-   Transformação em SaaS

------------------------------------------------------------------------

## 📚 Aprendizados Técnicos

-   Construção de agentes baseados em LLM
-   Estruturação de prompts dinâmicos
-   Integração com provedores externos de modelos
-   Organização de projetos Python escaláveis
-   Aplicação prática de IA generativa em contexto de negócio

------------------------------------------------------------------------

## 👩‍💻 Autora

Henrique Botelho Gomes\
Profissional em transição estratégica para Desenvolvimento de IA / LLM\
Foco em aplicações práticas de IA para negócios

------------------------------------------------------------------------

## 📄 Status

MVP funcional --- versão inicial para portfólio técnico.
