from pydantic import BaseModel

class RequestModel(BaseModel):
    customer_id: str