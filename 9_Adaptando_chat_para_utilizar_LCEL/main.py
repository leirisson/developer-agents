import os
from dotenv import load_dotenv 
from langchain_openai import ChatOpenAI 
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.chat_history import InMemoryChatMessageHistory 
from langchain_core.runnables.history import RunnableWithMessageHistory 



load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Variavel de anbiente não encontrada, verifique o .env")

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.5,
    api_key=api_key,
    max_completion_tokens=100
)

prompt_sugestao = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um guia de viagens especializado em destinos brasileiros. Apresente-se como Mr. Passeios divertidos"),
        ("placeholder", "{historico}"),
        ("human", "{query}")
    ]
)




cadeia = prompt_sugestao | modelo | StrOutputParser()


# criando um memoria temporaria
memoria = {}
id_sescao = "aula_langchain_alura"


# simulando o pattern singletom e gerencaindo as memorias por sessao
# importante para garantir que cada sessao tenha sua propria memoria
def historico_por_sessao(id_sessao: str): 
    if id_sessao not in memoria:
        memoria[id_sessao] = InMemoryChatMessageHistory()
    return memoria[id_sessao]
        
        
# simulando as perguntas do usuario
lista_de_perguntas = [
    "Quero visitar um lugar no brasil, famoso por natureza, rios lindos e cultura maravilhosa. Pode sugerir ?",
    "Qual a melhor epoca para ir ?"
]

# simulando a execução da cadeia com memoria
cadeia_com_memeoria = RunnableWithMessageHistory(
    runnable=cadeia,
    get_session_history=historico_por_sessao,
    input_messages_key="query",
    history_messages_key="historico",    
)

# iterando sobre as perguntas do usuario
# e exibindo a resposta do AI
for uma_pergunta in lista_de_perguntas:
    resposta = cadeia_com_memeoria.invoke(
        {"query": uma_pergunta},
        config={"session_id": id_sescao}
        )

    print(f"usuario: {uma_pergunta}")
    print(f"AI: {resposta} \n")
    
