# Automatizar a documentação de projetos em Python

Aviso:

    Este é um roteiro para instalação do projeto em uma máquina Windows para atender as minhas necessidades, portanto nao há qualquer garantia ou suporte para este roteiro.

## Objetivo

Gerar, a partir dos _docstrings_ do código Python, uma documentação bonita,
moderna, atualizada e automática, ou seja, escreva sua documentação uma única
vez nos _docstrings_ do código Python e tenha a documentação atualizada.

Manter a documentação gerada automaticamente significa menos esforço porque
você está vinculando informações entre seu código e as páginas de documentação,
guiando por meio de exemplos e conectar os pontos entre as _docstrings_.

## O que é necessário?

* [PyCharm](https://www.jetbrains.com/pycharm/) para desenvolvimento do projeto
* Um repositório para o projeto no [GitHub](https://github.com/).

## O que será instalado?

* [Poetry](https://python-poetry.org/) é uma ferramenta para gerenciar
  dependências e empacotar projetos Python.
* [Material for MkDocs](https://mkdocstrings.github.io/) é um tema para MkDocs,
  um gerador de sites estáticos voltado para a construção de documentação de
  projetos. Ele usa o design do _Material_ para criar uma interface de usuário
  bonita e responsiva.
* [mkdocstrings for Python](https://mkdocstrings.github.io/python/) é um plugin
  para MkDocs que gera documentação da API a partir dos _docstrings_ do Python.
  Ele usa o [Griffe](https://mkdocstrings.github.io/griffe/) para coletar a
  documentação do código-fonte do Python.
* [PyTest](https://docs.pytest.org/) é um framework para escrever e executar
  testes unitários em Python. Ele oferece uma sintaxe simples e poderosa, além
  de
  vários recursos úteis, como fixtures, parametrização e plugins.
* [Pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) é um plugin para
  PyTest que mede a cobertura de código dos testes. Ele usa o Coverage.py para
  coletar e reportar os dados de cobertura.
* [Blue](https://blue.readthedocs.io/en/latest/) é um formatador de código
  automático para Python. Ele reformata o código-fonte do Python seguindo um
  estilo consistente com a [PEP 8](https://pep8.org/).
* [ISort](https://pycqa.github.io/isort/) é uma ferramenta para ordenar as
  importações do Python de forma padronizada e automática.
* [TaskiPy](https://github.com/taskipy/taskipy) é uma ferramenta para executar
  tarefas definidas em um
  arquivo [pyproject.toml](https://realpython.com/python-toml/). Ele permite
  que você use o
  Poetry para gerenciar suas tarefas, como executar testes, construir pacotes
  ou implantar projeto.

### Ambiente virtual

O Poetry será usado para configurar o ambiente virtual e também o
gerenciamento dos pacotes a serem instalados no projeto.

### Instalação do Poetry

Abra o PowerShell e execute o seguinte comando:

```commandline
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Adicione o Poetry à variável PATH com o seguinte comando trocando o
<nome_usuario> pelo nome do usuário da máquina.

```commandline
$Env:Path += ";C:\Users\<nome_usuario>\AppData\Roaming\Python\Scripts"; setx PATH "$Env:Path"
```

### Criar um projeto

Ainda no PowerShell navegue até o diretório de projetos e execute o comando
abaixo.

```commandline
poetry new --src nome-projeto
```

Se você entrar no diretório do projeto deve ver algo assim:

```
nome-projeto
├── pyproject.toml
├── README.md
├── src
│   └── nome_projeto
│       └── __init__.py
└── tests
    └── __init__.py
```

### Configurando o PyCharm

1. Feche todos os projetos da IDE e a customize. Clique em _All settings_.
   ![Tela de boas-vindas do PyCharm com a indicacao de clicar no link All setting do menu Customize](assets\pycharm01.png "Customizar o PyCharm")
2. No interpretador do Python clique em _Add interpreter_.
   ![Seta indicando para clicar en Add interpreter](assets\pycharm02.png "Tela do interpretador do Python")
3. Selecione _Poetry Environment_ e busque o executável do Poetry.
   C:\Users\nome_usuario\AppData\Roaming\Python\Scripts\
   ![Seta indica onde deve se clicado](assets\pycharm03.png "Tela para adicionar o poetry.exe")
4. Altere o formato da _docstrings_ para Google selecionando  _Python
   Integrated Tools_.
   ![Seta indicando a seleção do Google na formacao dos docstrings](assets\pycharm04.png "Tela para alterar o formato da docstrings para Google")
5. Abra o projeto no PyCharm.
6. Gere o [.gitignore](https://www.toptal.com/developers/gitignore) para
   PyCharm e Python.
7. Commit inicial para estrutura do projeto.

### Adicionar os pacotes

Dentro do PyCharm abra o PowerShell e execute os comandos abaixo.

```commandline
poetry add --group docs mkdocs-material
```

```commandline
poetry add --group docs mkdocstrings[python]
```

```commandline
poetry add --group dev pytest
```

```commandline
poetry add --group dev pytest-cov
```

```commandline
poetry add --group dev blue
```

```commandline
poetry add --group dev taskipy
```

## Criar documentação do projeto

Adiciona um diretório, na raiz do projeto, nomeado `docs`

```commandline
mkdocs new .
```

Commit para instalação dos pacotes

### Personalizar o tema modificando o arquivo mkdocs.yml

```yaml
site_name: Nome Projeto
repo_url: https://github.com/<usuario_github>/nome_projeto
repo_name: <usuario_github>/nome_projeto
edit_uri: edit/main/docs/

theme:
  name: material
  language: pt-BR
  logo: assets/logo.png
  favicon: assets/logo.png
  font:
    text: Roboto
    code: Roboto Mono
  features:
    - content.code.annotation
    - content.code.copy
    - content.tabs.link
    - header.autohide
    - navigation.footer
    - navigation.tabs
    - navigation.top
    - navigation.sections
    - search.highlight
    - search.suggest
    - toc.integrate
  icon:
    admonition:
      note: fontawesome/solid/note-sticky
      abstract: fontawesome/solid/book
      info: fontawesome/solid/circle-info
      tip: fontawesome/solid/bullhorn
      success: fontawesome/solid/check
      question: fontawesome/solid/circle-question
      warning: fontawesome/solid/triangle-exclamation
      failure: fontawesome/solid/bomb
      danger: fontawesome/solid/skull
      bug: fontawesome/solid/robot
      example: fontawesome/solid/flask
      quote: fontawesome/solid/quote-left
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle:
        icon: material/toggle-switch-off-outline
        name: Mudar para o modo escuro
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/toggle-switch
        name: Mudar para o modo claro

extra:
  generator: true
  social:
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/<nome_usuario>
    - icon: fontawesome/brands/github
      link: https://github.com/<nome_usuario>

watch:
  - src/nome_projeto

plugins:
  - search:
      lang: pt
  - mkdocstrings:
      handlers:
        python:
          paths: [ src/nome_projeto ]
          options:
            separate_signature: true
            show_signature_annotations: true

```

### Colocando identificadores para os arquivos exemplos

Crie um diretório `api`, no diretório `docs`, e dentro crie um arquivo `.md` com o mesmo nome do 
arquivo a ser manipulado pelo mkdocstrings.

Dentro do arquivo `.md`, no diretório api, coloque o identificador, 
após três dois pontos seguidos, com o mesmo nome do arquivo Python. 
(::: nome_arquivo)

```markdown
heranca_poo.md

::: heranca_poo
```

Exemplo:

    nome-projeto
    ├── pyproject.toml
    ├── README.md
    ├── docs
    │   └── api
    │       └── heranca_poo.md
    ├── src
    │   └── nome_projeto
    │       ├── __init__.py
    │       └── heranca_poo.py
    └── tests
        └── __init__.py

Commit para personalização do Material for MkDocs

## Configurando o arquivo pyproject.toml

```toml
[tool.poetry]
name = "nome-projeto"
version = "0.1.0"
description = ""
authors = ["Nome <nome@host.com>"]
readme = "README.md"
packages = [{ include = "nome_projeto", from = "src" }]

[tool.poetry.dependencies]
python = "^3.11"

[tool.poetry.group.docs.dependencies]
mkdocs-material = "^9.1.12"
mkdocstrings = { extras = ["python"], version = "^0.21.2" }

[tool.poetry.group.dev.dependencies]
pytest = "^7.3.1"
pytest-cov = "^4.0.0"
blue = "^0.9.1"
isort = "^5.12.0"
taskipy = "^1.10.4"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
pythonpath = "."
addopts = "--doctest-modules"

[tool.isort]
profile = "black"
line_length = 79

[tool.taskipy.tasks]
lint = "blue --check --diff . && isort --check --diff ."
docs = "mkdocs serve"
pre_test = "task lint"
test = "pytest -s -x --cov=src -vv"
post_test = "coverage html"

```

Commit para configuração do Pytest, lint e taskiPy

## Rodar o servidor do MkDocs

```commandline
mkdocs serve
```

Depois do servidor iniciar clique no linque `http://127.0.0.1:8000/` e veja o 
resultado.
