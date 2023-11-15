# Clima Global Flask App

## Descrição

Este é um aplicativo web Flask projetado para coletar e exibir dados climáticos de cidades ao redor do mundo. Ele utiliza a API OpenWeather para buscar as condições climáticas atuais e armazená-las em um banco de dados SQLite para visualização e análise futuras.

## Funcionalidades

- Consulta dados climáticos de várias cidades globais.
- Armazena dados climáticos em um banco de dados SQLite.
- Fornece uma interface web para visualizar os dados coletados.

## Tecnologias Utilizadas

- Python 3
- Flask
- Flask-SQLAlchemy
- OpenWeather API
- HTML
- CSS

## Instalação e Configuração

Para configurar o projeto localmente, siga estes passos:

```bash
#Clone o repositório
git clone https://github.com/camilaanacleto/ETL_Flask.git
cd clima-global-flask

# Crie e ative um ambiente virtual
python -m venv venv
.\venv\Scripts\activate


# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
flask run

## Uso

Após iniciar o servidor, acesse `http://127.0.0.1:5000/` no navegador para ver a interface web. Para ver os dados climáticos armazenados, navegue até `http://127.0.0.1:5000/weather_data`.

## Executando os Testes

Para rodar os testes, execute o seguinte comando:

pytest

```

