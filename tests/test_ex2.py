from app.ex2 import Loop_numeros

def test_soma_numeros(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 5)
    resultado = Loop_numeros.soma_numeros(5)
    assert resultado == 15
