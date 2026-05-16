from weather_service import obter_clima

def test_obter_clima_integracao_sucesso():
    """Valida se a função consegue se comunicar com a API e retornar dados válidos."""
    resultado = obter_clima("London")
    
    assert isinstance(resultado, str)
    assert len(resultado) > 0
    assert "Cidade não informada" not in resultado

def test_obter_clima_cidade_vazia():
    """Valida o comportamento da integração quando nenhuma cidade é passada."""
    resultado = obter_clima("")
    assert resultado == "Cidade não informada."