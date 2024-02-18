from django.urls import path
from .views import ImageProcessView

urlpatterns = [
    path('v1/image_process/', ImageProcessView.as_view(), name='process_image'),
]
