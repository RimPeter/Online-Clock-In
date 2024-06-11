#install virtual environment
pip install virtualenv
python -m venv myenv
myenv\Scripts\activate


myenv\Script\deactivate or deactivate

#install Django in your virtual environment

pip install django
pip list #to see all packages

#create project
django-admin startproject #project name#


#Copy path of the virtual environment folder, so we don't get errors at additional installations with VScode
ctrl+shift+p
Enter Interpreter Path

#run server
python3 manage.py runserver

#Create 1st app
django-admin startapp #app name#
    ##Add to INSTALLED_APPS

python manage.py migrate 

#Create urls.py in 'webapp'
-add 'include' to import in clockin\urls.py
-add path('', include('webapp.urls')),
-add to webapp\urls.py:
    from django.urls import path
    from . import views
    urlpatterns = [
    path('', views.home, name=''),
    ]
-add to webapp\views.py:
    from django.http import HttpResponse
    def home(request):
        return HttpResponse('Hello, Django!')

#Create 'static' folder in clockin
    -css and js folders in it
#Add to settings.py:
    STATICFILES_DIRS = [
    BASE_DIR / "static",
    ]

#Create 'templates' folder in webapp:
    -'webapp' folder in it
        -'index.html' in it

#Change webapp\views.py:
    def home(request):
    #return HttpResponse('Hello, Django!')
    return render(request, 'webapp/index.html')

#Create 'base.html' in templates:
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Clock-In</title>
        <link rel="stylesheet" type="text/css" href="https://bootswatch.com/5/morph/bootstrap.min.css">
    </head>
    <body>
    </body>
    </html>

#Create style.css in css folder:
#Add in base.html:
    <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}"> 

#Create add.js  
#Add in base.html:
    <script src="{% static 'js/app.js' %}"></script>
    -from bootstrap popper to use dropdowns (https://getbootstrap.com/docs/5.3/getting-started/introduction/):
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    -from jquery:
        <script src="https://code.jquery.com/jquery-3.3.1.min.js" crossorigin="anonymous"></script>
    -new update, source: "https://getbootstrap.com/docs/4.4/getting-started/introduction/"

#Create 'register.html', 'dashboard.html', 'create-record.html', 'view-record.html', 'update-record.html' and 'my-login' in webapp:

#Create forms.py:
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth.models import User
    from django import forms
    from django.contrib.auth.forms import AuthenticationForm
    from django.forms.widgets import PasswordInput, TextInput

    # - Create User Form

    class CreateUserForm(UserCreationForm):
    
        class Meta:
            model = User
            fields = ['username', 'password1', 'password2']
            
    # - Login User Form

    class LoginForm(AuthenticationForm):
        username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
        password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))

#install crispyforms:
    pip install django-crispy-forms==1.14.0
    #Add 'crispy_forms' to INSTALLED_APPS in settings.py
    #Add CRISPY_TEMPLATE_PACK = 'bootstrap4' in settings.py
    #Add {% load crispy_forms_tags %} to register.html under {% extends "webapp/base.html" %} 
    