from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from ogretmen.models import Teacher
from django import forms
from django.shortcuts import redirect

def ogretmenf(request):
  template = loader.get_template('ogretmenw.html')
  return HttpResponse(template.render())
def listele(request):
    ogretmenlistele = Teacher.objects.all()
    template = loader.get_template('ogretmenlistele.html')
    context ={
        'ogretmenlistele' : ogretmenlistele,
    }
    return HttpResponse(template.render(context, request))
def sil(request, id):
    item = Teacher.objects.get(id=id)
    # item = Ogrenci.objects.all()[4]
    item.delete()
    return redirect('ogretmenlistele')

      # Bu fonksiyonu app içindeki views.py içine ekle.
# def ogretmenf(request,x):
#   print("Ogretmen sayfasına istek geldi..")
#   toplam = x*2
#   print(toplam)
#   giden = "toplam {{toplam}}"
#   giden1 = giden.render()
#   return HttpResponse(giden1)class OgrenciForm(forms.ModelForm):
class Ogretmenform(forms.ModelForm):
  class Meta:
      model = Teacher
      fields = ['maas', 'brans','adsoyad','telefon']  

def ekle(request):
  if request.method == 'POST':
      xx = Ogretmenform(request.POST)
      if xx.is_valid():
          # Form verileri işleme
          xx.save()  # Veritabanına kaydetme
          return redirect('ogretmenlistele')  #url name
  else:
      xx = Ogretmenform()
  return render(request, 'ogretmenekle.html', {'form': xx})
# Bu fonksiyonu app içindeki views.py içine ekle.
def ogretmendetay(request, id):
  item = Teacher.objects.get(id=id)
  template = loader.get_template('ogretmendetay.html')
  context = {
    'item': item,
  }
  return HttpResponse(template.render(context, request))
def guncelle(request, id):
    # ogretmen = get_object_or_404(Teacher, id=id)
    ogretmen = Teacher.objects.get(id=id)
    if request.method == 'POST':
        form = Ogretmenform(request.POST, instance=ogretmen)
        if form.is_valid():
            # Form verileri işleme
            form.save()  # Veritab. kaydetme
            return redirect('ogretmenlistele') #url name
    else:
        form = Ogretmenform(instance=ogretmen)
    return render(request, 'ogretmenduzenle.html', {'form': form}) 