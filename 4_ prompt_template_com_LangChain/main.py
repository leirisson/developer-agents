from cmd import PROMPT
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os 

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
# valida se a chave da API foi encontrada
if not API_KEY:
    raise ValueError("OPENAI_API_KEY não foi encontrada no arquivo .env")

NUMERO_DIAS = 5
NUMERO_CRIANCAS = 4
ATIVIDADE = "musica"


# CRIANDO UM MODELO DE PROMPT
MODELO_DE_PROMPT = PromptTemplate(
    template="""
    Crie um roteiro de viagens para {numero_dias} dias, 
    para uma família com {numero_criancas} crianças, 
    que gosta de {atividade}.
    """
)

# CRIANDO O PROMPT BASEADO NO MODELO DE PROMPT
prompt = MODELO_DE_PROMPT.format(
    numero_dias=NUMERO_DIAS,
    numero_criancas=NUMERO_CRIANCAS,
    atividade=ATIVIDADE
)

# INSTANCIANDO O MODELO
modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=API_KEY
)

# RESPOSTA DO MODELO
resposta = modelo.invoke(prompt)
print(resposta.content.strip())