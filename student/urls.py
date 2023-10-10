from django.urls import include, path

from rest_framework import routers

from student.views import PayViewSet, StudentViewSet, HomePageView

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)
router.register(r'pay', PayViewSet)

urlpatterns = [
     path("",HomePageView.as_view(), name="home"),
     path('',include(router.urls)),
]