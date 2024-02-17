from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def image_process(request):
    if request.method == 'GET':
        data = {'text': 'hello'}
        return JsonResponse(data)

    return HttpResponse('Empty')
