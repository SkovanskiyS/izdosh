from django.urls import path
from .views import image_process

urlpatterns = [
    path('v1/image_process/', image_process, name='process_image'),

]