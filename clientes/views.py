from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Cliente, Contrato, Ficha, Plano
from .serializers import ClienteSerializer, FichaSerializer, PlanoSerializer, ContratoSerializer

class ClienteListViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ContratoListViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class PlanoListViewSet(viewsets.ModelViewSet):
    queryset = Plano.objects.all()
    serializer_class = PlanoSerializer

class FichaListViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

