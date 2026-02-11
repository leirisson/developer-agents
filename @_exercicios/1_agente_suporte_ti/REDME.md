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
