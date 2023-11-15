import pytest
from flask import url_for
from models import db, WeatherData, get_brasil_datetime
from routes import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    # Setup
    with app.app_context():
        db.create_all()

    yield client

    # Teardown
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_conexao_com_db(client):
    with app.app_context():
        assert db.engine.execute('SELECT 1').scalar() == 1

def test_conteudo_da_tabela(client):
    with app.app_context():
        exemplo = WeatherData(city='Teste', temperature=25.5, humidity=80)
        db.session.add(exemplo)
        db.session.commit()
        tabela = WeatherData.query.all()
        assert len(tabela) > 0

def test_resposta_html(client):
    resposta = client.get('/weather_data')
    assert resposta.status_code == 200
    assert 'text/html' in resposta.content_type
    assert 'Dados Climáticos' in resposta.data

def test_rotas_existentes(client):
    with app.app_context():
        assert url_for('index') == '/'
        assert url_for('display_weather_data') == '/weather_data'

def test_etl_route(client):
    resposta = client.get('/')
    assert resposta.status_code == 200
    assert 'Consulta Climática' in resposta.data
