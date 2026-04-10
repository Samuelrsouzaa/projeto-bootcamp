class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        if not title or title.strip() == "":
            raise ValueError("O título não pode estar vazio.")
        self.tasks.append({"title": title, "completed": False})

    def list_tasks(self):
        return self.tasks

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True