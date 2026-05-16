from pydantic import BaseModel

class IncidentAnalysis(BaseModel):
    issue_type:str
    severity:str
    needs_logs:bool
    need_metrics:bool
    summary:str


    