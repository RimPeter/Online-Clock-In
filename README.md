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
    pip install django-crispy-forms crispy-bootstrap4

    #Add 'crispy_forms' to INSTALLED_APPS           in settings.py
    #Add CRISPY_TEMPLATE_PACK = 'bootstrap4'        in settings.py
    #Add {% load crispy_forms_tags %} to register.html under {% extends "webapp/base.html" %} 
    #Add {% csrf_token %} {{ form|crispy }}         in register.html inside <body>

    pip install django-crispy-forms crispy-bootstrap4
    #Add:
            INSTALLED_APPS = [
            ...
            'crispy_forms',
            'crispy_bootstrap4',
            ]

    #Add:
            CRISPY_TEMPLATE_PACK = 'bootstrap4'

#CREATE LOGIN#
#webapp/views.py:
    from django.contrib.auth.models import auth
    from django.contrib.auth import authenticate

    #Create code:
    def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                #return redirect('home')
    context = {'form': form}
    return render(request, 'webapp/my_login.html', context= context)

    #Add html content to your my_login.html
    
    #webapp/url.py:
        path('my-login/', views.my_login, name='my-login'),

#Add logout user in webapp/views.py:
    from django.shortcuts import redirect
    
    def user_logout(request):
        auth.logout(request)
        return redirect('my-login')

#Add dashboard in webapp/views.py:

    #for decorator:
    from django.contrib.auth.decorators import login_required

    @login_required(login_url='my-login')
    def dashboard(request):
        return render(request, 'webapp/dashboard.html')

    #-un-comment out:
    return redirect('dashboard')    at def(home) in views

    #Add 'dashboard' at def my_login():
    if user is not None:
        auth.login(request, user)
        return redirect('dashboard')

    #dashboard.html:
    {% extends "webapp/base.html" %}
    {% block content %}
    <h1>
        Welcome to the Dashboard! {{user}}
    </h1>
    {% endblock %}

    #Add at urls.py:
    path('dashboard/', views.dashboard, name='dashboard'),

    #Add 'dashboard' in navbar.html:
    <a class="nav-link" href="{% url 'dashboard' %}">Dashboard &nbsp; <i class="fa fa-home" aria-hidden="true"></i> </a>

    #Add in urls.py:
    path('user-logout/', views.user_logout, name='user-logout')

    #Add 'user-logout' in navbar.html:
    <a class="nav-link" href="{% url 'user-logout' %}">Sign out &nbsp; <i class="fa fa-sign-out" aria-hidden="true"></i> </a>


#Add model.py:
    from django.db import models

    class Record(models.Model):
        creation_date = models.DateTimeField(auto_now_add=True)
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        email = models.EmailField()
        phone = models.CharField(max_length=20)
        address = models.CharField(max_length=200)
        city = models.CharField(max_length=100)
        province = models.CharField(max_length=100)
        country = models.CharField(max_length=100)
        
        def __str__(self):
            return self.first_name + ' ' + self.last_name

    #run migration:
    python manage.py makemigrations
    python manage.py migrate

#webapp/admin.py:
    from .models import Record

    admin.site.register(Record)

    #in views.py:
    from .models import Record

    @login_required(login_url='my-login')
    def dashboard(request): 
        my_records = Record.objects.all()
        context = {'records': my_records}
        return render(request, 'webapp/dashboard.html', context= context)

    #dashboard.py:
    {% extends "webapp/base.html" %}
    {% block content %}
    <h1>
        Welcome to the Dashboard! {{user}}
    </h1>
    {% for record in records %}
        <p>{{record.id}}</p>
        <p>{{record.first_name}}</p>
        <p>{{record.last_name}}</p>
    {% endfor %}
    {% endblock %}

#CREATE RECORD
#views.py:
    @login_required(login_url='my-login')
    def create_record(request):
        pass

#forms.py:
    from .models import Record

        # - Create Record Form

        class CreateRecordForm(forms.ModelForm):
            
            class Meta:
                model = Record
                fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']

        # - Update Record Form

        class UpdateRecordForm(forms.ModelForm):
                
            class Meta:
                model = Record
                fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country'] 

        #Add to forms.py:
        from .forms import CreateRecordForm, UpdateRecordForm


#Create a record in views.py:
@login_required(login_url='my-login')
def create_record(request):
    form = CreateRecordForm()
    
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context= context)

#add to create_record.html:
    {% extends "webapp/base.html" %}
    {% load crispy_form_tags %}
    {% block content %}
        <h5> Create a new record </h5>
        <hr>
        <form method="POST" action="{% url 'create-record' %}">
            {% csrf_token %}
    {% endblock %}

#update record:
    #in views.py:
        @login_required(login_url='my-login')
        def update_record(request, pk):

            record = Record.objects.get(id=pk)

            form = UpdateRecordForm(instance=record)

            if request.method == 'POST':

                form = UpdateRecordForm(request.POST, instance=record)

                if form.is_valid():

                    form.save()

                    messages.success(request, "Your record was updated!")

                    return redirect("dashboard")
                
            context = {'form':form}

            return render(request, 'webapp/update-record.html', context=context)

#Create content for view-record.html:
    #in views.py:
        @login_required(login_url='my-login')
        def singular_record(request, pk):

            all_records = Record.objects.get(id=pk)

            context = {'record':all_records}

            return render(request, 'webapp/view-record.html', context=context)

    #ctreate dinamic url:
        path('record/int:pk>/', views.singular_record, name='record'),

    #Add to dashboard.html:
        href="{% url 'record' record.id%}" 


#MESSAGES:
    #in views.py:
    from django.contrib import messages

    #for delete_record:
    messages.success(request, "Your record was deleted!")

    #for user_logout:
    messages.success(request, "Logout success!")

    #for create_record:
    messages.success(request, "Your record was created!")

    #for update_record:
    messages.success(request, "Your record was updated!")

    #base.html:
    {% for message in messages%}
      
          {% if message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS %}
            <p class="alert alert-success float-center text-center">

              <i class='fa fa-check'aria-hidde='true'></i> &nbsp; {{message}}

            </p>
          {% endif %}

    #message time out in app.js:
        // Message/Notification timer

    var message_timeout = document.getElementById("message-timer");

    setTimeout(function () {
    message_timeout.style.display = "none";
    }, 5000);

    #Add id for base.html:
    {% if message.level == DEFAULT_MESSAGE_LEVELS.SUCCESS %}
            <p id='message-timer' class="alert alert-success float-center text-center">