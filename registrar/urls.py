from django.urls import include, path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')
router.register(r'mentors', views.MentorViewSet, basename='mentor')

students_router = routers.NestedSimpleRouter(router, r'students', lookup='student')
students_router.register(r'attachments', views.AttachmentViewSet, basename='attachment')
mentors_router = routers.NestedSimpleRouter(router, r'mentors', lookup='mentor')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(students_router.urls)),
    path('', include(mentors_router.urls))
]