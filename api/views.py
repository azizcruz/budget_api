from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import ProjectSerializer, CategorySerializer, ExpenseSerializer
from .models import Project, Category, Expense
from .mixins import MixinModelViewSet

# Create your views here.

class ProjectView(MixinModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseView(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


# Fix base route of the website is not found.
_API_ROUTE = "/api/"
def redirect_to_api(request):
    return redirect(_API_ROUTE)