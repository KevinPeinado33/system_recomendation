from fastapi import APIRouter, status, Body
from src.models.content_based_recomendation import ContentBasedRecomendation

router                      = APIRouter()
content_based_recomendation = ContentBasedRecomendation()

class RecomendationController:

    @router.get('/articles', status_code=status.HTTP_200_OK)
    def get_articles():

        articles_recommended = content_based_recomendation.select_articles()

        return { 'data': articles_recommended }
    

    @router.post('/articles_recommended', status_code=status.HTTP_200_OK)
    def get_recomendation( article: dict = Body(...) ):

        title =  article['title']

        recomendation = content_based_recomendation.recomendation(title)

        return { 'data': recomendation }
