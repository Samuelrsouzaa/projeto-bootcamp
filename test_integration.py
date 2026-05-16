import pytest
import requests
from weather_service import obter_clima

def test_obter_clima_integracao_sucesso():
    
    resultado = obter_clima("London")
    
    
    assert isinstance(resultado, str)
    assert len(resultado) > 0
    assert "Cidade não informada" not in resultado

def test_obter_clima_cidade_vazia():
    
    resultado = obter_clima("")
    assert resultado == "Cidade não informada."