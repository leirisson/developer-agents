from codigo import chain
from fastapi import FastAPI
from langserve import add_routes


app = FastAPI(
    title="Langchain Agent", 
    version="1.0", 
    description="Agente de tradução de texto, traduza o texto para o idioma desejado"
    )

# /tanslate
add_routes(app, chain, path="/translate", methods=["POST"])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
