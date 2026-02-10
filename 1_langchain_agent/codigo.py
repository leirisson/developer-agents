from dotenv import load_dotenv
import os
import getpass
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate




load_dotenv()
CHAVE_API = os.getenv("OPENAI_API_KEY")
if not CHAVE_API:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Entre you OpenAI API key: ")
    

mensagens = [
    SystemMessage("Traduza o texto a seguir para inglês"),
    HumanMessage("hojé é o dia do jogo do Flamengo")
]

modelo = ChatOpenAI(model="gpt-5-nano")
parser = StrOutputParser()


# texto = chain.invoke(mensagens)
# print(texto)

# criar os templates de mensagens
template_mensagem = ChatPromptTemplate.from_messages([
    ("system", "Traduza o texto a seguir para {idioma}"),
    ("user", "{input}")
])

template_mensagem.invoke({"idioma": "inglês", "input": "meu nome é Leirisson e estou aprendendo a usar Langchain"})
# output: "My name is Leirisson and I am learning to use Langchain"

chain =  template_mensagem | modelo | parser  # criando uma chain - cadeia de execução

# texto = chain.invoke({"idioma": "inglês", "input": "meu nome é Leirisson e estou aprendendo a usar Langchain"})
# print(texto)

