import pytest
from task_manager import TaskManager

def test_add():
    tm = TaskManager()
    tm.add_task("Teste")
    assert len(tm.list_tasks()) == 1

def test_empty_error():
    tm = TaskManager()
    with pytest.raises(ValueError):
        tm.add_task("")