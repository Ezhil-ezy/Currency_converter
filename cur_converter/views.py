from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
import requests
import json
import string
# Create your views here.

def chrome(request):
  return render(request, "shop/index.html")

def add(request):
  return render(request, "shop/add.html")
'''
def addition(request):
  a = int(request.GET["a"])
  b = int(request.GET["b"])
  res = a + b
  return render(request, "shop/add.html", {'result':res})
'''

def addition(request):
  
  url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
  
  a = request.GET["a"]
  b = request.GET["b"]

  amount =request.GET["amount"]

  querystring = {
    "from":a,
    "to":b,
    "amount":amount
  }
  
  print(querystring)

  if b == "INR":
    symbol = '₹ '
  
  elif b == "USD":
    symbol = '$ '
  elif b == "EUR":
    symbol = '€ '
  elif b == "BRL":
    symbol = 'R$ '
  elif b == "CAD":
    symbol = 'ca $'
  elif b == "BAM":
    symbol = 'km'
  
  headers = {
    "X-RapidAPI-Key": "976628a52bmsh88a81f9521b3fa2p12121cjsn3fb9b5ec240c",
    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)
  data = json.loads(response.text)
  converted = data["result"]["convertedAmount"]
  formatted = "{:,.2f}".format(converted)
  result = formatted
  return render(request, 'shop/add.html', {'result':result})