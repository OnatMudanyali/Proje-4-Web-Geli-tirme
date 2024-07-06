from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def ogrencif(request):
  template = loader.get_template('ogrenciler.html')
  return HttpResponse(template.render())


from ogrenci.models import Talebe
from django import forms
from django.shortcuts import redirect

class OgrenciForm(forms.ModelForm):
  class Meta:
      model = Talebe
      fields = ['TC', 'AdiSoyadi','Aciklama']  

def ekle(request):
  if request.method == 'POST':
      xx = OgrenciForm(request.POST)
      if xx.is_valid():
          # Form verileri işleme
          xx.save()  # Veritabanına kaydetme
          return redirect('ogrenciliste')  #url name
  else:
      xx = OgrenciForm()
  return render(request, 'ogrenciekle.html', {'form': xx})


def listele(request):
  ogrenciliste = Talebe.objects.all()
  template = loader.get_template('ogrencilistele.html')
  context ={
      'ogrenciliste' : ogrenciliste,
  }
  return HttpResponse(template.render(context, request))
    # Bu fonksiyonu app içindeki views.py içine ekle.
def detay(request, id):
      item = Talebe.objects.get(id=id)
      template = loader.get_template('detay.html')
      context = {
        'item': item,
      }
      return HttpResponse(template.render(context, request))
def sil(request, id):
      item = Talebe.objects.get(id=id)
      # item = Ogrenci.objects.all()[4]
      item.delete()
      return redirect('ogrenciliste')


# def ogrenci(request):
#   template = loader.get_template('index1.html')
#   return HttpResponse(template.render()) 