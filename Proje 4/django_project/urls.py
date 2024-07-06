"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
import anasayfa.views
import ogrenci.views
import ogretmen.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', anasayfa.views.anasayfafen, name="home"),
    path('anasayfa/', anasayfa.views.anasayfaf),
    path('', anasayfa.views.anasayfaf),
    path('ogrenci/', ogrenci.views.ogrencif,name="ogrenciler"),
    # path('ogretmen/<int:x>',ogretmen.views.ogretmenf)
    path('ogretmen/',ogretmen.views.ogretmenf),
    path('ogretmen/ekle', ogretmen.views.ekle),
    path('ogretmenler/', ogretmen.views.listele,name="ogretmenlistele"),
    # path('ogretmen/sil/<int:id>', ogrenci.views.sil,name="ogretmensil"),
    path('ogretmen/detay/<int:id>', ogretmen.views.ogretmendetay,name="ogretmendetay"),
    
    path('ogrenci/ekle', ogrenci.views.ekle),
    path('ogrenciler', ogrenci.views.listele,name="ogrenciliste"),
    path('ogrenciler/sil/<int:id>', ogrenci.views.sil,name="ogrencisil"),
    path('ogretmenler/sil/<int:id>', ogretmen.views.sil, name='CRUD_sil'),
    path('ogretmenler/guncelle/<int:id>', ogretmen.views.guncelle, name='CRUD'),

    path('ogrenciler/detay/<int:id>', ogrenci.views.detay,name="ogrencidetay"),

]
