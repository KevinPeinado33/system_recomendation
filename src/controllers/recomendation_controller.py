from fastapi import APIRouter, status
from src.models.content_based_recomendation import ContentBasedRecomendation

router                      = APIRouter()
content_based_recomendation = ContentBasedRecomendation()

class RecomendationController:

    @router.get('/articles', status_code=status.HTTP_200_OK)
    def get_articles():

        articles_recommended = content_based_recomendation.select_articles()

        return { 'data': articles_recommended }
    

    @router.get('/articles_recommended', status_code=status.HTTP_200_OK)
    def get_recomendation():
        
        recomendation = content_based_recomendation.recomendation(title='Laptop chipiada Asus rog')

        return { 'data': recomendation }
