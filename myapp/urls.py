from django.urls import path
from . import views
from .views import SimplePostView,UserAPI,simple_page,student_api
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet1
from django.urls import path, include
from myapp.sc  import defaultview
from myapp.drfView  import drfview
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'students', StudentViewSet1)



urlpatterns = [
    path('hello/', views.hello),   # default route
    path('bye/', views.bye),   # default route
    path('echo/', views.echo),   # default route
    path('update/', views.update_echo),     # PUT
    path('delete/', views.delete_echo),     # DELETE
    path('cbv-post/', SimplePostView.as_view()), 
    path('drf-post/', UserAPI.as_view()),
    path('', include(router.urls)),
    path('simple-products/', simple_page),
    path("login/", defaultview.login_page),
    path("home/", defaultview.home),
    path('newstudents/', student_api),
    path("profile/", drfview.ProfileAPI.as_view()),
    path("api-token-auth/", obtain_auth_token),
    path("aboutus/", drfview.Aboutus.as_view()),
     path("jwt/login/", TokenObtainPairView.as_view()),
    path("jwt/refresh/", TokenRefreshView.as_view()),
    


]


