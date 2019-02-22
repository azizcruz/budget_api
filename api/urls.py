from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register("projects", views.ProjectView)
router.register("categories", views.CategoryView)
router.register("expenses", views.ExpenseView)

urlpatterns = [
    path("", include(router.urls)),

    # these urls are for getting token and also refresh it.
    # path("token/", TokenObtainPairView.as_view()),
    # path("token/refresh", TokenRefreshView.as_view())
]