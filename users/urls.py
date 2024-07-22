from .views import CreateUserAPIView ,authenticate_user
from django.urls import include, re_path 

urlpatterns = [
   re_path(r'^create/$', CreateUserAPIView.as_view()),
   re_path(r'^login/$', authenticate_user),

]