class TodoList:
    """Gestor simple de tareas pendientes."""

    def __init__(self):
        self.tasks = []  

    def add_task(self, task: str) -> dict:
        """Agrega una nueva tarea y la retorna."""
        if not task.strip():
            raise ValueError("La tarea no puede estar vacía")
        new_task = {"task": task.strip(), "done": False}
        self.tasks.append(new_task)
        return new_task

    def complete_task(self, index: int) -> dict:
        """Marca una tarea como completada por su índice."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            return self.tasks[index]
        raise IndexError("Índice fuera de rango")

    def delete_task(self, index: int) -> dict:
        """Elimina una tarea por su índice y la retorna."""
        if 0 <= index < len(self.tasks):
            return self.tasks.pop(index)
        raise IndexError("Índice fuera de rango")

    def list_tasks(self) -> list:
        """Devuelve todas las tareas."""
        return self.tasks

    def get_pending(self) -> list:
        """Devuelve solo las tareas pendientes."""
        return [t for t in self.tasks if not t["done"]]


if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Aprender CI/CD con GitHub Actions")
    todo.add_task("Crear Dockerfile")
    todo.add_task("Escribir pruebas unitarias")
    todo.complete_task(0)  

    print("=== Lista de tareas ===")
    for i, t in enumerate(todo.list_tasks()):
        status = "✓" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")

    print("\n=== Tareas pendientes ===")
    for t in todo.get_pending():
        print(f"- {t['task']}")