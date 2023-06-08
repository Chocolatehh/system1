from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import WenWu, Category
from .forms import WenWuForm, CategoryForm
from .tables import CategoryTable, WenWuTable

from django_tables2 import SingleTableView, RequestConfig

from Inpainting.models import User


# 注入 Ticket User 上下文模板变量
class TicketAndUserContentData:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        ticket = self.request.COOKIES.get('ticket')
        email = self.request.COOKIES.get('email')
        user = User.objects.filter(email=email).first()

        if not ticket or not user or not User.objects.filter(ticket=ticket).exists():
            return HttpResponseRedirect('/login/')

        context['ticket'] = ticket
        context['user'] = user
        return context


class WuWenListView(TicketAndUserContentData, SingleTableView):
    table_class = WenWuTable
    queryset = WenWu.objects.all()

    # 添加分页
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = self.table_class(data=self.queryset)
        RequestConfig(self.request, paginate={"per_page": 10}).configure(t)
        context['table'] = t
        return context


class WenWuCreateView(TicketAndUserContentData, CreateView):
    model = WenWu
    form_class = WenWuForm
    success_url = reverse_lazy('dashboard:wenwu_list')


class WenWuUpdateView(TicketAndUserContentData, UpdateView):
    model = WenWu
    form_class = WenWuForm
    success_url = reverse_lazy('dashboard:wenwu_list')


class WenWuDetailView(TicketAndUserContentData, DetailView):
    model = WenWu


class WenWuDeleteView(TicketAndUserContentData, DeleteView):
    model = WenWu
    success_url = reverse_lazy('dashboard:wenwu_list')


class CategoryListView(TicketAndUserContentData, SingleTableView):
    table_class = CategoryTable
    queryset = Category.objects.all()

    # 添加分页
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        t = self.table_class(data=self.queryset)
        RequestConfig(self.request, paginate={"per_page": 10}).configure(t)
        context['table'] = t
        return context


class CategoryCreateView(TicketAndUserContentData, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('dashboard:category_list')


class CategoryUpdateView(TicketAndUserContentData, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('dashboard:category_list')


class CategoryDetailView(TicketAndUserContentData, DetailView):
    model = Category


class CategoryDeleteView(TicketAndUserContentData, DeleteView):
    model = Category
    success_url = reverse_lazy('dashboard:category_list')
