from django.urls import path
from .views import signin, signup, index, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('singin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout')
]
