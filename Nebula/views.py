from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def admin(request):
    return render(request, 'admin.py')

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def stylesheets(request):
    return render(request, 'indexpage.css')
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Query MongoDB for user record
       # user = User.objects.filter(username=username).first()

        if user:
            # Compare passwords
            if user.check_password(password):
                # Authenticate user
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    # Redirect to dashboard or another page
                    return redirect('dashboard')
        # Handle invalid credentials
        return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

