from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .apps import PredictorConfig

@csrf_exempt
def predictChat(request):
    if request.method == 'POST':
        data = request.POST.get('message')
        print(data)
        # return JsonResponse({'message': 'Hello, World!'}, safe=False)
        return JsonResponse({'message': PredictorConfig.NNpredict(data)}, safe=False)

# Create your views here.
