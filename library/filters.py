import django_filters
from django import forms
from django.db.models import Q

from .models import Book, Category, Message, Checkout


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
                                                        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = ['title', 'category', 'author', ]


class MessageFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter')

    class Meta:
        model = Message
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Message.objects.filter(
            Q(name__icontains=value) | Q(message__icontains=value) | Q(email__icontains=value) | Q(
                subject__icontains=value)
        )


class CheckoutFilter(django_filters.FilterSet):
    student_f_name = django_filters.CharFilter(field_name="user__first_name", lookup_expr='icontains',
                                               label='User\'s First Name')
    student_l_name = django_filters.CharFilter(field_name="user__last_name", lookup_expr='icontains',
                                               label='User\'s Last Name')

    class Meta:
        model = Checkout
        fields = ['user', 'reserved', 'collected', 'overdue', 'closed']
