import pytest

@pytest.fixture
def lista_tarefas_teste():
    """Cria uma lista de tarefas limpa para simular o sistema."""
    return []

def test_adicionar_tarefa_sucesso(lista_tarefas_teste):
    """Valida se uma tarefa é adicionada corretamente com título."""
    titulo = "Estudar para o Bootcamp"
    
    if titulo.strip():
        lista_tarefas_teste.append({"titulo": titulo, "concluida": False})
    
    assert len(lista_tarefas_teste) == 1
    assert lista_tarefas_teste[0]["titulo"] == "Estudar para o Bootcamp"
    assert lista_tarefas_teste[0]["concluida"] is False

def test_concluir_tarefa_sucesso(lista_tarefas_teste):
    """Valida se o status da tarefa muda para concluída."""
    lista_tarefas_teste.append({"titulo": "Fazer Deploy", "concluida": False})
    
    lista_tarefas_teste[0]["concluida"] = True
    
    assert lista_tarefas_teste[0]["concluida"] is True