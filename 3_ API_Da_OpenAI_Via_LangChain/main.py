from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY não foi encontrada no arquivo .env")
    

NUMERO_DIAS = 5
NUMERO_CRIANCAS = 4
ATIVIDADE = "praia"

prompt = f"Crie um roteiro de viagens para {NUMERO_DIAS} dias, para uma família com {NUMERO_CRIANCAS} crianças, que gosta de {ATIVIDADE}."

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

resposta = modelo.invoke(prompt)
print(resposta.content.strip())
