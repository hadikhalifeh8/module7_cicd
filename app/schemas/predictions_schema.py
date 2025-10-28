from pydantic import BaseModel

class Prediction(BaseModel):
    text: str
    sentiment: str
    
    class Config:
        from_attributes = True
        
class PredictionCreate(BaseModel):
    text: str
    
    class Config:
        from_attributes = True