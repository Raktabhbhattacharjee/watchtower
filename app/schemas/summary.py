from pydantic import BaseModel


class IncidentSummary(BaseModel):
    root_cause:str
    recomended_action:str
    confidence:str
    
