from fastapi import APIRouter, HTTPException

from app.services.ml_services import predict, train_model
from app.utils.exceptions import InvalidInputError
from app.utils.logger import get_logger

from app.schemas.ml_schema import PredictRequestSchema, PredictionSchema


logger = get_logger(__name__)

router = APIRouter(prefix="/ml", tags=["ml"])

@router.post("/train")
def train_model_route():
    """
        Train the machine learning model on the Iris dataset.
    """
    try:
        train_model()
    except Exception as e:
        logger.error(f"An error occurred while training the model: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while training the model.")    
    except FileNotFoundError as e:
        logger.error(f"File not found error: {e}")
        raise HTTPException(status_code=404, detail="File not found error.")     
    return {"message": "Model trained successfully."}


@router.post("/predict", response_model= PredictionSchema)
def predict_route(request: PredictRequestSchema):
    try:
        prediction = predict([request.input_data]) # [[5.1, 3.5, 1.4, 0.2]]
    except InvalidInputError as e:
        logger.error(f"Invalid input error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"An error occurred during prediction: {e}")
        raise HTTPException(status_code=500, detail="An error occurred during prediction.")
    return {"prediction": prediction[0]}
        
