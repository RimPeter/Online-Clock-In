#install virtual environment
python -m venv myenv
myenv\Scripts\activate
pip install virtualenv

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

