from django.http import JsonResponse
from .services import search_posts, delete_post
from .utils import load_data_from_csv
import json

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .serializers import PostSerializer

@swagger_auto_schema(
    method='get',
    operation_description="Поиск постов на основе запроса q.",
    responses={200: openapi.Response(description="Успешный ответ", schema=openapi.Schema(type="array", items=openapi.Schema(type="object")))}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def search_view(request):
    """
    Поиск постов на основе запроса q.
    """
    query = request.GET.get('q', '')
    posts = search_posts(query)
    # posts_list = list(posts.values())
    # return JsonResponse(posts_list, safe=False, json_dumps_params={'ensure_ascii': False})
    serializer = PostSerializer(posts, many=True)  # Используем сериализатор для сериализации QuerySet в JSON
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

    


@swagger_auto_schema(
    method='get',
    operation_description="Удаление поста по идентификатору.",
    responses={200: openapi.Response(description="Успешный ответ", schema=openapi.Schema(type="object"))}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def delete_view(request, document_id):
    """
    Удаление поста по идентификатору.
    """
    delete_post(document_id)
    return JsonResponse({'success': True})

@swagger_auto_schema(
    method='get',
    operation_description="Загрузка данных из CSV файла.",
    responses={200: openapi.Response(description="Успешный ответ", schema=openapi.Schema(type="object"))}
)
@api_view(['GET'])
@permission_classes([AllowAny])
def load_data_view(request):
    """
    Загрузка данных из CSV файла.
    """
    csv_file_path = '../posts.csv'

    try:
        load_data_from_csv(csv_file_path)
        return JsonResponse({'result': "Data loaded from CSV file successfully!"})
    except Exception as e:
        return JsonResponse({'error': str(e)})
