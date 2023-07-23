# simple_python_flask
## Criando um simples projeto Python com Flask em quatro etapas
### ETAPA - 1 (Criação do projeto no Git e importação)

Crie sua conta no [Git Hub](https://github.com/) se ainda não possuir uma.
Crie um projeto público no Git Hub com o nome que desejar, mas `simpleFlask` seria apropriado para o que se pretende demonstrar.
Lembre-se acresecentar ao projeto durante sua criação o `README.md` e o `.git ignore` sugeridos. 

Dentro de um terminal qualquer digite o comando abaixo, para importar o projeto do repositório remoto do Git.
Estou usando o Ubuntu 22.04 no WSL2.
```
$ git clone https://github.com/lucioweb/simple_python_flask.git
```

Abrindo a pasta do projeto com o `VSCode`.
```
$ code .
```

### ETAPA - 2 (Criando e ativando o ambiente virtual)
Essa etapa utiliza o tutorial do próprio Flask disponível em [Flask - Installation](https://flask.palletsprojects.com/en/2.3.x/installation/#dependencies)

Criando o `.venv` na pasta do projeto `simpleflask`✔️
```
$ python3 -m venv .venv
```

Antes de trabalhar em seu projeto, ative o ambiente correspondente.
Ativando o `.venv` (Conforme https://flask.palletsprojects.com/en/2.3.x/installation/). 
Lembre-se, esse comando e o anterior devem ser dados dentro da pasta do projeto.
```
$ . .venv/bin/activate
```

Dentro do ambiente ativado, use o seguinte comando para listar as libs presentes no ambiente virtual::
```
(.venv) luciolemos@dev:~/my_python_projects/simpleFlask$ pip list
Package    Version
---------- -------
pip        22.0.2
setuptools 59.6.0
```

### ETAPA - 3 (Criando o arquivo de requisitos `requirements.txt`)
Em vez de instalar pacotes individualmente, pip permite que você declare todas as dependências em um Arquivo de Requisitos.
Por exemplo: você pode criar um arquivo `requirements.txt` na raiz do projeto, contendo todas as bibliotecas que deseja instalar e instalá-las com esssa linha de comando: `python3 -m pip install -r requirements.txt`.
É uma boa prática salvar os pacotes necessários para sua aplicação em um arquivo requirements.txt. 
Assim se houver necessidade de migrar o projeto ou de instalá-lo em outro ambiente, bastará rodar o comando `pip install -r requirements.txt` e todos os componentes serão instalados. Você pode criar esse arquivo com o seguinte comando:
```
$ pip freeze > requirements.txt
```

Verifique com `pip list` as libs instaladas junto com o flask:
```
Package      Version
------------ -------
blinker      1.6.2
click        8.1.6
Flask        2.3.2
itsdangerous 2.1.2
Jinja2       3.1.2
MarkupSafe   2.1.3
pip          22.0.2
setuptools   59.6.0
Werkzeug     2.3.6
```

### ETAPA - 4 (O projeto propriamente)
Crie um arquivo com o nome que desejar, mas `hello.py` seria apropriado para o que se pretende mostrar em seguida.
Via linha de comando no terminal integrado do VS Code o comando seria:
```
$ echo>hello.py
```

Dentro do arquivo `hello.py` criado, digite ou cole, se ainda não tem habilidade suficiente com o Flask, as seguintes linhas de código:
```
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

Como a lib do Flask está instalada em nosso projeto, vamos subir a aplicação com o seguinte comando:
```
$ flask --app hello run
```

Ou no modo de depuração com o seguinte comando:
```
$ flask --app hello run --debug
```

Veremos no terminal o seguinte retorno, indicando que a aplicação foi carregada com sucesso:
```
 * Serving Flask app 'hello'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [21/Jul/2023 07:30:16] "GET / HTTP/1.1" 200 -
```

Pronto! Está criando seu Projeto Python com Flask, rodando na porta 5000, porta de escuta padrão utilizada pelo Python, emitindo uma mensagem de boas vindas.

Basta digitar no seu navegador favorito o seguinte URL: http://127.0.0.1:5000

### ETAPAS COMPLEMENTARES
Para realizar o upgrade das libs instaladas no projeto, instale:
```
$ pip install upgrade-requirements
```
... e execute:
```
$ upgrade-requirements
```

