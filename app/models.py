from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    text: str
    style: str = "formal"  # Options: "formal", "informal", "technical"

class SummarizationResponse(BaseModel):
    task_id: str
    status: str
    result: str
