import base64

from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MoneyImageModel
from .inference import image_process_model
from django.core.files.base import ContentFile


class ImageProcessView(APIView):
    def get(self, request, *args, **kwargs):
        print('hello')
        return Response({"data": ''})

    def post(self, request, *args, **kwargs):

        image64 = request.data['image']
        format, imgstr = image64.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        image_model = MoneyImageModel()
        image_model.image_file.save(data.name, data, save=True)
        print(image_model.image_file)
        result_amount = image_process_model(image_model.image_file)
        res = {"sum": result_amount}

        return JsonResponse(res)


def base64_file(data, name=None):
    _format, _img_str = data.split(';base64,')
    _name, ext = _format.split('/')
    if not name:
        name = _name.split(":")[-1]
    print('no error')
    return ContentFile(base64.b64decode(_img_str), name='{}.{}'.format(name, ext))

