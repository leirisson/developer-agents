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


class Destino(BaseModel):
    cidade: str = Field(description="Nome da cidade sugerida")
    motivo: str = Field(description="Motivo pelo qual a cidade foi sugerida")

class Restaurante(BaseModel):
    cidade:str =   Field(description="Nome da cidade sugerida")
    restaurantes: str = Field(description="Restaurantes recomendados na cidade")

parseador_destino = JsonOutputParser(pydantic_object=Destino)
parseador_restaurante = JsonOutputParser(pydantic_object=Restaurante)



prompt_cidade = PromptTemplate(
    template = """
    Sugira uma cidade dado o meu interesse {interesse},
    seguindo o formato de saída: {formato_de_saida}
    """,
    input_variables=["interesse"],
    partial_variables={"formato_de_saida": parseador_destino.get_format_instructions()}
)

prompt_restaurante = PromptTemplate(
    template = """
    Sugira restaurantes dado a cidade {cidade},
    seguindo o formato de saída: {formato_de_saida}
    """,
    partial_variables={"formato_de_saida": parseador_restaurante.get_format_instructions()}
)

prompt_passeio = PromptTemplate(
    template = """
    Sugira atividades e locais culturais dado a cidade {cidade}
    """
)


modelo_agent = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key,
    max_completion_tokens=100
)


"""
montando as cadeias de execução
"""
cadeia_destino = prompt_cidade | modelo_agent | parseador_destino
cadeia_restaurante = prompt_restaurante | modelo_agent | parseador_restaurante
cadeia_passeio = prompt_passeio | modelo_agent | StrOutputParser()

"""
montando a cadeia principal, onde:
1. o modelo sugere uma cidade dado o interesse do usuário
2. o modelo sugere restaurantes na cidade sugerida
3. o modelo sugere atividades e locais culturais na cidade sugerida
"""
cadeia_principal = (cadeia_destino   | cadeia_restaurante | cadeia_passeio)

"""
executando a cadeia principal
1. o usuário fornece seu interesse
2. o modelo sugere uma cidade dado o interesse do usuário
3. o modelo sugere restaurantes na cidade sugerida
4. o modelo sugere atividades e locais culturais na cidade sugerida
"""
interesse = input("Qual é o seu interesse? ")
resposta = cadeia_principal.invoke({"interesse": interesse})
print(resposta)