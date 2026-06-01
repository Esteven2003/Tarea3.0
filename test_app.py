import pytest
from app import TodoList

@pytest.fixture
def todo():
    """Fixture que crea una lista con tareas precargadas."""
    t = TodoList()
    t.add_task("Tarea 1")
    t.add_task("Tarea 2")
    return t

def test_add_task(todo):
    assert len(todo.list_tasks()) == 2
    todo.add_task("Tarea 3")
    assert len(todo.list_tasks()) == 3

def test_add_empty_task():
    t = TodoList()
    with pytest.raises(ValueError):
        t.add_task("   ")

def test_complete_task(todo):
    todo.complete_task(0)
    assert todo.list_tasks()[0]["done"] is True
    assert todo.list_tasks()[1]["done"] is False

def test_complete_invalid_index(todo):
    with pytest.raises(IndexError):
        todo.complete_task(5)

def test_delete_task(todo):
    deleted = todo.delete_task(1)
    assert deleted["task"] == "Tarea 2"
    assert len(todo.list_tasks()) == 1

def test_delete_invalid_index(todo):
    with pytest.raises(IndexError):
        todo.delete_task(10)

def test_get_pending(todo):
    todo.complete_task(0)
    pendientes = todo.get_pending()
    assert len(pendientes) == 1
    assert pendientes[0]["task"] == "Tarea 2"