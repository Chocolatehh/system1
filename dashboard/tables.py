import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse

from .models import Category, WenWu


class CategoryTable(tables.Table):
    actions = tables.Column(empty_values=(), verbose_name="操作", orderable=False)

    class Meta:
        model = Category
        fields = ('title', 'created_at')
        attrs = {'class': 'table'}
        template_name = "dashboard/bs51_tables.html"

    # 自定义操作链接
    def render_actions(self, value, record):
        return format_html(
            '''
            <a class="btn btn-sm btn-secondary" href="%s">编辑</a>
            <a class="btn btn-sm btn-warning" href="%s">删除</a>
            ''' % (
                reverse("dashboard:category_update", args=[record.pk]),
                reverse("dashboard:category_delete", args=[record.pk])
            )
        )


class WenWuTable(tables.Table):
    actions = tables.Column(empty_values=(), verbose_name="操作", orderable=False)

    class Meta:
        model = WenWu
        fields = ('title', 'category', 'created_at')
        attrs = {'class': 'table'}
        template_name = "dashboard/bs51_tables.html"

    # 自定义操作链接
    def render_actions(self, value, record):
        return format_html(
            '''
            <a class="btn btn-sm btn-secondary" href="%s">编辑</a>
            <a class="btn btn-sm btn-warning" href="%s">删除</a>
            ''' % (
                reverse("dashboard:wenwu_update", args=[record.pk]),
                reverse("dashboard:wenwu_delete", args=[record.pk])
            )
        )
