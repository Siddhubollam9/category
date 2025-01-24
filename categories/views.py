from django.shortcuts import render, redirect
from .models import Category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Category
from django.shortcuts import get_object_or_404

def main_page(request):
    return render(request, 'main.html')

def add_category(request):
    if request.method == 'POST':
        # Main category name
        name = request.POST['name']
        
        # Parent category (if any)
        parent_id = request.POST.get('parent')
        parent = Category.objects.get(id=parent_id) if parent_id else None

        # Create the main category
        main_category = Category.objects.create(name=name, parent=parent)

        # Subcategories (comma-separated)
        subcategories = request.POST.get('subcategories')
        if subcategories:
            subcategories_list = [s.strip() for s in subcategories.split(',')]
            for subcategory_name in subcategories_list:
                Category.objects.create(name=subcategory_name, parent=main_category)

        return render(request, 'add_category_success.html', {'main_category': main_category})

    return render(request, 'add_category.html', {'categories': Category.objects.all()})

def show_categories(request):
    categories = Category.objects.filter(parent=None)  # Fetch only root categories
    return render(request, 'show_categories.html', {'categories': categories})

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        if new_name:
            category.name = new_name
            category.save()
            return redirect('show_categories')
    return render(request, 'edit_category.html', {'category': category})
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('show_categories')
