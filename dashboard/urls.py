from django.urls import path

from . import views
from .decorators import login_required


app_name = 'dashboard'

urlpatterns = [
    path('', login_required(views.WuWenListView.as_view()), name='wenwu_list'),
    path('create/', login_required(views.WenWuCreateView.as_view()), name='wenwu_create'),
    path('<int:pk>/', login_required(views.WenWuDetailView.as_view()), name='wenwu_detail'),
    path('<int:pk>/update/', login_required(views.WenWuUpdateView.as_view()), name='wenwu_update'),
    path('<int:pk>/delete/', login_required(views.WenWuDeleteView.as_view()), name='wenwu_delete'),

    path('category/', login_required(views.CategoryListView.as_view()), name='category_list'),
    path('category/create/', login_required(views.CategoryCreateView.as_view()), name='category_create'),
    path('category/<int:pk>/', login_required(views.CategoryDetailView.as_view()), name='category_detail'),
    path('category/<int:pk>/update/', login_required(views.CategoryUpdateView.as_view()), name='category_update'),
    path('category/<int:pk>/delete/', login_required(views.CategoryDeleteView.as_view()), name='category_delete')
]