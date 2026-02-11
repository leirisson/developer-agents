from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

NUMERO_DIAS = 5
NUMERO_CRIANCAS = 4
ATIVIDADE = "esportes"

prompt = f"Crie um roteiro de viagens {NUMERO_DIAS} dias, para uma família com {NUMERO_CRIANCAS} crianças, que gosta de {ATIVIDADE}."

client = OpenAI(api_key=api_key)

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente que cria roteiros de viagens."},
        {"role": "user", "content": prompt}],
    max_tokens=100
)

print(resposta.choices[0].message.content.strip())



