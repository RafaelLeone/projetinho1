# projetinho1
projeto 1 curso django roger
google keep
1 - lista de tarefas fixa
2 - deploy
3 - cadastro de tarefas
? - Ir colocando o que a gente aprendeu como o URLField.
? - usuario
---

##Começo.
1 cdworkspace/
2 mkdir projetinho1
3 cd projetinho1
4 viurtualenv .venv
5 source .venv/bin/activate
6 pip install django
7 django-admin startproject porjetinho1
8 cd projetinho1
9 ./manage.py startapp lembretes

##Parte 1
Dentro da IDE. VScode ou Pycharm

#projetinho1:
1 settings.py > Installed APPs = 'lembretes'
2 urls.py > path('', include('lembretes.urls'))

#lembretes:
-urls.py:
from django.urls import path
from . import views
urlpatterns = [
    path('', views.pagina_inicial)
]
-views.py:
from django.shortcuts import render
def pagina_inicial(request):
  return render(request, 'lembretes/pagina_inicial.html')
-Lembretes > Templates > Lembretes > Página Inicial HTML
Criar pagina_inicial.html

##Parte 2
#Lembretes
admin.py > from .models import lembretes
admin.site
no models fazer a class lembretes
NO TERMINAL
./manage.py makemigrations
./manage.pý migrate
./manage.py createsuperuser
pip freeze > requirements.txt
NA IDE
pagina_incial.html
{% for lembretes in lembretes #letra miniscula apps.py deixa a letra minuscula %}
{% end for %}










