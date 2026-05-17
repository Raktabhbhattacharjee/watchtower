from pydantic import BaseModel

class InvestigationPlan(BaseModel):
    steps:list[str]
    reasoning:str