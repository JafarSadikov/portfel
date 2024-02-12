from django.urls import path


from .views import register_clients

urlpatterns = [
    path('', register_clients, name='register_clients'),
]