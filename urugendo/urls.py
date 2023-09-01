from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

router = routers.DefaultRouter()

router.register("ingenzi", IngenziViewset)
router.register("urugendo", UrugendoViewset)
router.register("itike", ItikeViewset)
router.register("users", UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', CustomTokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
