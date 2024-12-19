def get_task_status(storage, task_id):
    task = storage.get(task_id)
    return {"task_id": task_id, "status": task["status"], "result": task.get("result")}
