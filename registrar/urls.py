from django.urls import include, path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.ProductViewSet, basename='student')


students_router = routers.NestedSimpleRouter(router, r'students', lookup='student')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(students_router.urls)),
]