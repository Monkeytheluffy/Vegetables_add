from django.shortcuts import render, get_object_or_404
from .models import Category, Vegetable
from django.shortcuts import redirect
from .forms import UserRegistrationForm, UserLoginForm
from .mongodb import get_db


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'vegetables/category_list.html', {'categories': categories})

def vegetable_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    vegetables = Vegetable.objects.filter(category=category)
    return render(request, 'vegetables/vegetable_list.html', {'category': category, 'vegetables': vegetables})

def vegetable_detail(request, vegetable_id):
    vegetable = get_object_or_404(Vegetable, id=vegetable_id)
    return render(request, 'vegetables/vegetable_detail.html', {'vegetable': vegetable})

# View to register a new user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            db = get_db()
            users_collection = db['users']

            # Save user to MongoDB
            users_collection.insert_one({
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password']  # Use hashing for passwords in production
            })

            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'vegetables/register.html', {'form': form})

# View to login a user
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            db = get_db()
            users_collection = db['users']
            user = users_collection.find_one({'username': username, 'password': password})

            if user:
                request.session['username'] = user['username']
                return redirect('category_list')
    else:
        form = UserLoginForm()

    return render(request, 'vegetables/login.html', {'form': form})

# View to logout a user
def logout_view(request):
    request.session.flush()  
    return redirect('login')

def home(request):
    categories = Category.objects.all()  
    vegetables = Vegetable.objects.all()  
    return render(request, 'vegetables/vegetable_detail.html', {'categories': categories, 'vegetables': vegetables})
