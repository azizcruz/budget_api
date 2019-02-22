from rest_framework import serializers
from .models import Project, Category, Expense
from django.utils.text import slugify


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.CharField(max_length=120, read_only=True)
    budget_left = serializers.IntegerField(read_only=True)
    class Meta:
        model = Project
        fields = ["id", "url", "name", "slug", "budget", "budget_left"]

    # def create(self, validated_data):
    #     validated_data["slug"] = slugify(validated_data["name"])
    #     project = Project.objects.create(**validated_data)
    #     return project

    # def partial_update(self, request, pk=None):
    #     pass
    
        

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "url", "category_name"]

class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Expense
        fields = ["id", "url", "title", "amount","project", "category"]