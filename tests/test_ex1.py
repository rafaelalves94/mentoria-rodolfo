from app.ex1 import Array_numeros

def test_soma_valores(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: list('123'))
    resultado = Array_numeros.soma_valores('123')

    assert resultado == 6

def test_maior_valor(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: list('123'))
    resultado = Array_numeros.maior_valor('123')

    assert resultado == '3'

def test_lista_invertida(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: list('123'))
    resultado = Array_numeros.lista_invertida('123')

    assert resultado == ['3','2','1']
    