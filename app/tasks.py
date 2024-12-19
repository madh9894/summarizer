from app.summarizer import summarize_text

async def process_summarization(text, style, task_id, storage):
    try:
        # Perform summarization
        summary = summarize_text(text, style)
        # Update task status to completed and store the result
        storage[task_id] = {"status": "completed", "result": summary}
    except Exception as e:
        # In case of error, set task status to error
        storage[task_id] = {"status": "error", "result": str(e)}
