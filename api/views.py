from django.shortcuts import redirect
from rest_framework import viewsets
from .serializers import ProjectSerializer, CategorySerializer, ExpenseSerializer
from .models import Project, Category, Expense
from rest_framework.response import Response
# Create your views here.
class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # Overriding list method to modify the budget left.
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        # Handling the budget left.
        for project in queryset:
            project.budget_left = project.calculate_budget_left()

        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Overriding retrieve method to modify the budget left
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.budget_left = instance.calculate_budget_left()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ExpenseView(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


# Handle base route of the website.
_API_ROUTE = "/api/"
def redirect_to_api(request):
    return redirect(_API_ROUTE)