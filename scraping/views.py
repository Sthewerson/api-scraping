from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SiteInfo
from .serializers import SiteInfoSerializer
import requests
from bs4 import BeautifulSoup  

@api_view(['POST'])
def salve_info(request):
    url = request.data.get('url')

   
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
       
        site_info = SiteInfo(url=url)
        site_info.save()

        return Response({'message': 'Informações salvas com sucesso!'})
    
    except Exception as e:
        return Response({'error': f'Erro ao realizar scraping: {str(e)}'}, status=500)

@api_view(['POST'])
def get_info(request):
    url = request.data.get('url')

    try:
        site_info = SiteInfo.objects.get(url=url)
        serializer = SiteInfoSerializer(site_info)
        return Response(serializer.data)
    
    except SiteInfo.DoesNotExist:
        return Response({'error': 'Informações não encontradas.'}, status=404)
