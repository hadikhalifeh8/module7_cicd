from fastapi import FastAPI, HTTPException
from app.utils.exceptions import InvalidInputError
from app.utils.logger import get_logger
from app.routes.crud_routs import router as crud_router
from app.routes.ml_routes import router as ml_router
from app.routes.sentimnet_routes import router as sentiment_router

logger = get_logger(__name__)
logger.info("Starting the model training and prediction process.")


app = FastAPI(title = "Iris Flower Prediction API",)
app.include_router(crud_router)
app.include_router(ml_router)
app.include_router(sentiment_router)

@app.get("/")
def root():
    return {"message": "Welcome to the Iris Flower Prediction API"}


@app.get("/health_check")
def root():
    return {"message": "good to go to the doctor"}


print("hello world")


@app.post("/name")
def get_name(name: str):
        if not name.isalpha():
            logger.error("Invalid input: Name must contain only alphabetic characters.")
            raise InvalidInputError("Invalid input: Name must contain only alphabetic characters.")
        return {"message": f"Hello, {name}!"}
            

