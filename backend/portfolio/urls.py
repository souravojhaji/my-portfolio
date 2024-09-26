from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, SkillViewSet, ProjectViewSet, ContactInfoViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'contact-info', ContactInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
