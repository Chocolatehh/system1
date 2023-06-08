from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from dashboard.models import Category, WenWu

from Inpainting.models import User


def inject_content(request):
    return {
        'ticket': request.COOKIES.get('ticket'),
        'user': User.objects.filter(email=request.COOKIES.get('email')).first()
    }


def index_view(request):
    content = {
        'category': Category.objects.all(),
        'items': WenWu.objects.all()[:9],
        **inject_content(request)
    }
    return render(request, 'home/index.html', content)


def category_view(request, pk):
    paginator = Paginator(WenWu.objects.filter(category_id=pk).all(), 9)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)  # 如果传入page参数不是整数，默认第一页
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'home/category.html', {
        'category': Category.objects.all(),
        'page': page_obj,
        'pk': pk,
        **inject_content(request)
    })


def wenwu_view(request, pk):
    obj = get_object_or_404(WenWu, id=pk)
    return render(request, 'home/wenwu.html', {
        'obj': obj,
        'category': Category.objects.all(),
        **inject_content(request)
    })


def search_view(request):
    paginator = Paginator(WenWu.objects.filter(title__contains=request.GET.get('q') or True).all(), 9)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)  # 如果传入page参数不是整数，默认第一页
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return render(request, 'home/search.html', {
        'category': Category.objects.all(),
        'page': page_obj,
        **inject_content(request)
    })