"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django_app import views as django_views
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hi/',views.greet),
    path('list/',django_views.patient_list),
    # path('html/',views.hello),
    path('Dr/',django_views.doctor_list),

    path('HOME/', django_views.list_patients,name="list_patients"),
    path('add/',django_views.add_patient,name="add_patient"),
    path('delete/<int:id>/',django_views.delete_patient, name="delete_patient"),


    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
    path('home/', accounts_views.home, name='home'),
    path('hi/',django_views.greet1),
    path('All/',django_views.project),
]







