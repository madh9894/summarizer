from fastapi import FastAPI, HTTPException, BackgroundTasks
from app.models import SummarizationRequest, SummarizationResponse
from app.summarizer import summarize_text
from app.tasks import process_summarization

app = FastAPI()

# Task storage for tracking summarization requests
task_storage = {}

@app.post("/summarize", response_model=SummarizationResponse)
async def submit_text_for_summarization(request: SummarizationRequest, background_tasks: BackgroundTasks):
    # Create a unique task_id
    task_id = str(len(task_storage) + 1)
    # Store task in pending state
    task_storage[task_id] = {"status": "pending", "result": None}
    
    # Perform summarization immediately
    try:
        summary = summarize_text(request.text, request.style)
        # Update status and result directly
        task_storage[task_id] = {"status": "completed", "result": summary}
    except Exception as e:
        # Handle errors if summarization fails
        task_storage[task_id] = {"status": "error", "result": str(e)}
    
    # Return the result immediately along with task_id
    return {"task_id": task_id, "status": "completed", "result": task_storage[task_id]["result"]}

@app.get("/summarize/status/{id}", response_model=SummarizationResponse)
async def get_summarization_status(id: str):
    if id not in task_storage:
        raise HTTPException(status_code=404, detail="Task ID not found")
    
    # Retrieve task status and result
    task = task_storage[id]
    return {"task_id": id, "status": task["status"], "result": task.get("result")}
