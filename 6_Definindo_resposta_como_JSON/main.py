from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser  # formato de saida vai ser uma string
from pydantic import Field, BaseModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.globals import set_debug
import os 


# Ativando o modo debug
set_debug(True)

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()


api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY não foi encontrada no arquivo .env")


"""
criando uma classe Destino para representar a saída do modelo
com os atributos cidade e motivo
para que o modelo possa retornar uma saída em JSON
"""
class Destino(BaseModel):
    cidade: str = Field(description="Nome da cidade sugerida")
    motivo: str = Field(description="Motivo pelo qual a cidade foi sugerida")

"""
criando parser para o modelo
para que o modelo possa retornar uma saída em JSON
"""
parseador = JsonOutputParser(pydantic_object=Destino)



# Criando o modelo de prompt para o agente
prompt_modelo = PromptTemplate(
    template = """
    Sugira uma cidade dado o meu interesse {interesse},
    seguindo o formato de saída: {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador.get_format_instructions()}
)

# invocar o modelo
modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key,
    max_completion_tokens=100
)

# Criando a cadeia de execução (chain)
cadeia = prompt_modelo | modelo | parseador

# receber a entrada do usuário
interesse = input("Qual é o seu interesse? ")

# invocar a cadeia de execução
resposta = cadeia.invoke(
    {"interesse": interesse}
    )

print(resposta)
