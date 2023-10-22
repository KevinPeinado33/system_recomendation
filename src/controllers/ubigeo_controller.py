from fastapi import APIRouter, Query, status

from src.models.ubigeo_model import get_departments, get_provinces, get_district

router = APIRouter()

class UbigeoController:
    
    @router.get('/departments', status_code=status.HTTP_200_OK)
    def get_departments():    
        return { 'data': get_departments() }
    
    @router.get('/provinces', status_code=status.HTTP_200_OK)
    def get_departments(
        department: str = Query(..., description='id del departamento.')
    ):    
        return { 'data': get_provinces(department) }
    
    @router.get('/districts', status_code=status.HTTP_200_OK)
    def get_departments(
        department: str = Query(..., description='id del departamento.'),
        province: str = Query(..., description='id de la provincia.')
    ):    
        return { 'data': get_district(department, province) }
    
