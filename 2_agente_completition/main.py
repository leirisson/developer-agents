from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 4
atividade = "esportes"

prompt = f"Crie um roteiro de viagens {numero_dias} dias, para uma família com {numero_criancas} crianças, que gosta de {atividade}."

client = OpenAI(api_key=api_key)

resposta = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente que cria roteiros de viagens."},
        {"role": "user", "content": prompt}],
    max_tokens=150
)

print(resposta.choices[0].message.content.strip())