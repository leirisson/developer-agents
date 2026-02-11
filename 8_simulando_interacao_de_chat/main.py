import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY não foi encontrada no arquivo .env")

modelo_agent = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key,
    max_completion_tokens=100
)

# criar um exemplo de 2 perguntas
lista_de_perguntas = [
    "quero visitar uma cidade nova",
    "quero conhecer lugares culturais"
]

for uma_pergunta in lista_de_perguntas:
    resposta = modelo_agent.invoke(uma_pergunta)
    print("AI: " + resposta.content + "\n")
