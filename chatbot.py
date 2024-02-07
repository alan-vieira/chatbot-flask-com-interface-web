"""
Um aplicativo simples com Flask para um chatbot usando ChatterBot.
"""
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Inicialização do Flask
app = Flask(__name__)

# Criação de uma nova instância de chatbot chamada 'kitt'
chatbot = ChatBot('kitt')

# Criação de um novo treinador para o chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinamento do chatbot com saudações e conversas em português
trainer.train(
    "chatterbot.corpus.portuguese.greetings",
    "chatterbot.corpus.portuguese.conversations"
    )


@app.route("/")
def index():
    """
    Renderiza a página inicial.

    Retorna:
        HTML renderizado
    """
    return render_template("index.html")


@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    """
    Manipula as respostas do chatbot.

    Retorna:
        str: resposta do chatbot
    """
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return str(response)


if __name__ == "__main__":
    app.run()
