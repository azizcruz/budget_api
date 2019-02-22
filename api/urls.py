from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register("projects", views.ProjectView)
router.register("categories", views.CategoryView)
router.register("expenses", views.ExpenseView)

urlpatterns = [
    path("", include(router.urls))
]