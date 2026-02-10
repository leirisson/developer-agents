"""
Cliente para o agente de tradução de texto
simula a interação com o servidor, enviando mensagens e recebendo respostas 
como se fosse uma aplicação cliente.
"""

from langserve import RemoteRunnable

chain_remote = RemoteRunnable("http://localhost:8000/translate")

# enviar uma mensagem para o servidor
resposta = chain_remote.invoke({"idioma": "inglês", "input": "meu nome é Leirisson e estou aprendendo a usar Langchain"})
print(resposta)


# para usar no postman, deve-se enviar um POST para http://localhost:8000/translate
# com o seguinte corpo:
# {
#     "idioma": "inglês",
#     "input": "meu nome é Leirisson e estou aprendendo a usar Langchain"
# }