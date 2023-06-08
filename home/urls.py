from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('search/', views.search_view, name='index_view'),
    path('category/<int:pk>', views.category_view, name='category_view'),
    path('wenwu/<int:pk>', views.wenwu_view, name='wenwu_view'),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
