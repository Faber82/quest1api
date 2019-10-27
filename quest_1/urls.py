"""quest_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.conf.urls import url, include
from api.resources import NoteResource

note_resource = NoteResource()
#path używa ścieżki bez regular expresion. Do sprawdzenia czy api pójdzie na path. Narazie zostawiam tak jak w tuorialu.
#r przed '^admin/' to skrót od "raw" - surowy. Oznacza traktowanie tego ciągu znaków dosłownie. używa się głównie
#ze względu na stosowanie \. 
urlpatterns = [
    url (r'^admin/', admin.site.urls),
    url (r'^api/', include(note_resource.urls))
]
#importujemy nasz zasób NoteResource tworzymy z niego instancję
#a następnie mówimy że chcemy żeby wszystkie url'e które zaczynają
#się od api/ były przekierowane do zasobu