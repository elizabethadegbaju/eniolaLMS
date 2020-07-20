import django_filters
from django import forms

from .models import Book, Category, Checkout


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title',
                                      lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__name',
                                       lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = ['title', 'category', 'author', ]


class CheckoutFilter(django_filters.FilterSet):
    student_f_name = django_filters.CharFilter(field_name="user__first_name",
                                               lookup_expr='icontains',
                                               label='User\'s First Name')
    student_l_name = django_filters.CharFilter(field_name="user__last_name",
                                               lookup_expr='icontains',
                                               label='User\'s Last Name')

    class Meta:
        model = Checkout
        fields = ['user', 'reserved', 'collected', 'overdue', 'closed']
