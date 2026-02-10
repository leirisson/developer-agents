# Exercícios básicos de LangChain

Pré-requisitos
- Ter Python instalado e as dependências do projeto: `python -m pip install -r requirements.txt`
- Definir a variável de ambiente `OPENAI_API_KEY` (pode usar um arquivo `.env`)

Observação
- Todos os exemplos usam o modelo `gpt-5-nano` via `langchain-openai`.
- Para ver apenas o texto da resposta, use `.content` quando chamar o modelo diretamente ou `StrOutputParser` quando usar cadeias.

## Exercício 1 — Prompt + Modelo (resposta simples)
- Objetivo: criar um prompt simples e encadear com o modelo para obter texto.
- Tarefas:
  - Criar um `ChatPromptTemplate` com um placeholder.
  - Instanciar `ChatOpenAI(model="gpt-5-nano")`.
  - Converter a saída para `str` com `StrOutputParser`.
  - Invocar a cadeia com um valor de entrada.

Exemplo inicial

```python
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-5-nano")
prompt = ChatPromptTemplate.from_template(
    "Escreva um slogan curto e criativo para {produto}."
)
parser = StrOutputParser()
chain = prompt | model | parser

print(chain.invoke({"produto": "cafeteira inteligente"}))
```

Critérios de sucesso
- A saída deve ser um slogan curto e direto no terminal.
- Alterar o valor de `produto` muda a resposta do modelo.

## Exercício 2 — Mensagens (System + Human)
- Objetivo: usar mensagens estruturadas para orientar o comportamento do modelo.
- Tarefas:
  - Criar uma `SystemMessage` com instruções de tradução.
  - Enviar uma `HumanMessage` com texto em português.
  - Invocar o modelo com a lista de mensagens e imprimir somente o conteúdo.

Exemplo inicial

```python
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-5-nano")
mensagens = [
    SystemMessage(content="Você é um tradutor do português para inglês."),
    HumanMessage(content="Hoje é dia de jogo do Flamengo.")
]
resposta = model.invoke(mensagens)
print(resposta.content)
```

Critérios de sucesso
- O terminal deve exibir o texto traduzido para inglês.
- Modificar a instrução do sistema altera o estilo/tonalidade da resposta.

## Exercício 3 — Pipeline com Prompt + Modelo + Parser
- Objetivo: compor uma cadeia reutilizável usando `Runnable` (| pipeline).
- Tarefas:
  - Criar um `ChatPromptTemplate` que recebe `pergunta` e `contexto`.
  - Encadear com `ChatOpenAI` e `StrOutputParser`.
  - Invocar a cadeia com um dicionário de entrada.

Exemplo inicial

```python
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-5-nano")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Responda de forma direta e concisa."),
    ("human", "{pergunta}\nContexto:\n{contexto}")
])
parser = StrOutputParser()
chain = prompt | model | parser

print(chain.invoke({
    "pergunta": "Explique LangChain em uma frase.",
    "contexto": "Ferramenta para compor pipelines de LLM."
}))
```

Critérios de sucesso
- A saída deve ser uma resposta curta que considere a pergunta e o contexto.
- Trocar os valores de `pergunta` e `contexto` deve alterar a resposta adequadamente.

Ideias para explorar
- Use `chain.batch([...])` para processar várias entradas de uma vez.
- Experimente `chain.stream(input)` para receber tokens incrementais.
