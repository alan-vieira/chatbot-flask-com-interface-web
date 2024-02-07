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

### Ambiente virtualizado com Anaconda

Após ter instalado o pacote Anconda crie a ative o ambiente com os comandos:

- Crie o ambiente virtual com python 3.8
```bash
conda create -n chatbot_conda python=3.8
```

- Ative o ambiente virtual
```bash
conda activate chatbot_conda
```

- desative o ambiente virtual
```bash
conda deactivate
```

Certifique-se de ter essas dependências instaladas no seu ambiente de desenvolvimento. Você pode instalá-las executando:

## Configuração


1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/chatbot-flask-com-interface-web.git
cd chatbot-flask-com-interface-web
```

2. Instale as dependências usando o pip:

```bash
pip install -r requirements.txt
```

## Modificação no arquivo `compat.py` da biblioteca SQLAlchemy

Ao utilizar a biblioteca SQLAlchemy em conjunto com o sistema operacional Windows ou Jython, foi identificado um possível problema relacionado à função `time.clock` na linha 264 do arquivo `compat.py`.

### Problema Identificado

No código original:

  ```python
  if win32 or jython:
      time_func = time.clock
  else:
      time_func = time.time
  ```

A função time.clock é utilizada, porém, em algumas situações específicas, essa abordagem pode levar a problemas.

### Solução Aplicada

A seguinte modificação foi realizada para evitar possíveis complicações:

  ```python
  if win32 or jython:
    #time_func = time.clock
    pass
  else:
    time_func = time.time
  ```

Essa alteração evita o uso da função `time.clock` e opta por manter o código compatível em ambientes Windows e Jython.

Nota: Modificar diretamente o código de bibliotecas pode ter implicações. Recomenda-se monitorar as atualizações da biblioteca e verificar se o problema foi abordado nas versões mais recentes.

## Como Usar

Execute o aplicativo Flask:

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