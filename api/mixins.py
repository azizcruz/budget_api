from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class MixinModelViewSet(ModelViewSet):
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