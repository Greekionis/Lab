from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class MainView(View):

    def get(self, request):
        return render(request, 'modist/index.html')

    def get_contact(self, request):
        return render(request, 'modist/contact.html')


