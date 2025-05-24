class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, plan, status):
        self.tasks[task_id] = {"status": status, "plan": plan}

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_plan(self, task_id):
        return self.tasks.get(task_id, {}).get("plan")

    def complete_task(self, task_id, result):
        self.tasks[task_id]["status"] = "completed"
        self.tasks[task_id].update(result)

    def fail_task(self, task_id, reason):
        self.tasks[task_id] = {"status": "rejected", "reason": reason}