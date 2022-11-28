from django.shortcuts import render
#from django.http import HttpResponse
import random 


def home(request):
   return render (request, 'generator/home.html')


def about(request):
   return render (request, 'generator/about.html')

def password(request):
   characters = list('abcdefghijklmnopqrstuvwxyz')
   generated_password = ''

   length = int (request.GET.get('length'))

   if request.GET.get ('uppercase'):
      characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

   if request.GET.get('special'):
      characters.extend(list('_-!$%/*@+-'))

   if request.GET.get('numbers'):
      characters.extend(list('0123456789'))

   for char in range (length):
      generated_password += random.choice(characters)
   return render (request, 'generator/password.html',{'password':generated_password} )