from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Variavel de anbiente não encontrada, verifique o .env")

# instancia um modelo de linguagem
modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key,
    max_completion_tokens=100
)

# templete de prompt
prompt = ChatPromptTemplate.from_messages(
   [
        ("system", "Escreva um splogan curto e criativo para {produto}, use emojis."),
        ("human", "{produto}"),
   ]
)

# parser de saida
parser = StrOutputParser()

# cadeia de execução
# a cadeia é composta por 3 partes:
# 1. o prompt
# 2. o modelo de linguagem
# 3. o parser de saida
chain = prompt | modelo | parser


# realizando a invocação da cadeia
# a invocação é feita passando um dicionário com as variáveis do prompt
prompt_user = input("Digite o produto: ")
resultado = chain.invoke({"produto": prompt_user})
print(f"Slogan para o produto:  {prompt_user}:")
print(resultado)

