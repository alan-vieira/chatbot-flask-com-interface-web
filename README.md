# Chatbot Flask com Interface Web

Este projeto consiste em um chatbot desenvolvido utilizando o framework Flask para o backend e uma interface web para interação. A aplicação utiliza a biblioteca ChatterBot para criar um assistente de conversação simples, capaz de responder a perguntas comuns dos usuários.

## Visão Geral

O objetivo deste projeto é fornecer uma plataforma de chat interativa que permita aos usuários obter respostas para suas perguntas de forma rápida e eficiente. O chatbot é treinado para lidar com uma variedade de consultas relacionadas a um determinado tópico ou domínio específico.

## Estrutura de Pastas

A estrutura de pastas do projeto é organizada da seguinte forma:

```bash
chatbot-flask-com-interface-web/
|-- static/
|   |-- style.css
|-- templates/
|   |-- index.html
|-- chatbot.py
|-- requirements.txt
```

- `static/style.css`: Este arquivo contém o estilo CSS para a interface do usuário do ChatBot.
- `templates/index.html`: Este arquivo contém a estrutura HTML da interface do usuário do ChatBot.
- `chatbot.py`: Este é o arquivo principal do projeto, onde o ChatBot é inicializado e a interação com o usuário é tratada.
- `requirements.txt`: Este arquivo lista as dependências do Python 

## Pré-requisitos

Antes de começar, você deve ter as seguintes dependências instaladas:

- Python 3.8
- Flask
- ChatterBot

Certifique-se de ter essas dependências instaladas no seu ambiente de desenvolvimento. Você pode instalá-las executando:

```python
pip install -r requirements.txt
```

## Configuração

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot-flask-com-interface-web.git
cd chatbot-flask-com-interface-web
```

2. Execute o aplicativo Flask:

```python
python chatbot.py
```

O aplicativo Flask será iniciado e estará pronto para interagir com você como um assistente de vendas.


## Documentação

### Flask App

`app = Flask(__name__)`

Inicializa uma instância do Flask.

### Rota Principal

`@app.route("/")`

Define a rota principal da aplicação Flask, que renderiza a página inicial do ChatBot.

### Rota para Obter Resposta do ChatBot
`@app.route("/get", methods=["GET", "POST"])`

Define a rota para obter a resposta do ChatBot com base na mensagem enviada pelo usuário.

### Função `index()`

```python
@app.route("/")
def index():
    """
    Renderiza a página inicial do ChatBot.
    """
    return render_template("index.html")
```

Esta função renderiza a página inicial do ChatBot.

### Função `chatbot_response()`

```python
@app.route("/get", methods=["GET", "POST"])
def chatbot_response():
    """
    Retorna a resposta do ChatBot com base na mensagem do usuário.
    """
    msg = request.form["msg"]
    response = chatbot.get_response(msg)
    return str(response)
```

Esta função retorna a resposta do ChatBot com base na mensagem enviada pelo usuário.

## Como Usar

Para usar o ChatBot, abra um navegador da web e vá para o endereço http://localhost:5000/. Você verá a interface do usuário do ChatBot, onde poderá enviar mensagens e receber respostas do assistente de vendas.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para detalhes.

## Autor

| [<img src="https://avatars.githubusercontent.com/alan-vieira" width=115><br><sub>Alan Vieira</sub>](https://github.com/alan-vieira) |
| :---: |

## Agradecimentos

Agradecemos pelo uso e interesse neste projeto! Esperamos que seja útil para seus propósitos.

Se precisar de mais alguma coisa ou tiver outras perguntas, fique à vontade para perguntar!