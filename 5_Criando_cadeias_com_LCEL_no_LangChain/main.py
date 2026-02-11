
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser # formato de saida vai ser uma string
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY não foi encontrada no arquivo .env")



modelo_cidade = PromptTemplate(
    template = """
    Sugira uma cidade dado o meu interesse {interesse}
    """,
    input_variables=["interesse"]
)


modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key
)

cadeia = modelo_cidade | modelo | StrOutputParser()

resposta = cadeia.invoke(
    {"interesse": "praias"}
    )

print(resposta.strip())


