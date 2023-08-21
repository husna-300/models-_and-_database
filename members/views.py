from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def alifmobi(request):
  template = loader.get_template('alifmobi.html')
  return HttpResponse(template.render())

def visa(request):
  template = loader.get_template('visa.html')
  return HttpResponse(template.render())

def salom(request):
  template = loader.get_template('salom.html')
  return HttpResponse(template.render())

def carfinancing(request):
  template = loader.get_template('carfinancing.html')
  return HttpResponse(template.render())

def alifshop(request):
  template = loader.get_template('alifshop.html')
  return HttpResponse(template.render())

def transfers(request):
  template = loader.get_template('transfers.html')
  return HttpResponse(template.render())

def deposits(request):
  template = loader.get_template('deposits.html')
  return HttpResponse(template.render())

def alifonline(request):
  template = loader.get_template('alifonline.html')
  return HttpResponse(template.render())