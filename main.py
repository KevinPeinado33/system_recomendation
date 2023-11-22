import nltk
from fastapi                 import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers.recomendation_controller import router as recomendation_router

nltk.download('punkt')
nltk.download('stopwords')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router( recomendation_router, prefix='/recomendation' )
