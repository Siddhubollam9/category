from django.urls import path
from .views import main_page, add_category, show_categories,edit_category, delete_category

urlpatterns = [
    path('', main_page, name='main_page'),
    path('add_category/', add_category, name='add_category'),
    path('show_categories/', show_categories, name='show_categories'),
]
urlpatterns += [
    path('edit_category/<int:category_id>/', edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
]
