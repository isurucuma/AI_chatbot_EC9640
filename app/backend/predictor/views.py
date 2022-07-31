from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

from .apps import PredictorConfig

@csrf_exempt
def predictChat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data['message']
        # return JsonResponse({'message': 'Hello, World!'}, safe=False)
        predictedMessage = PredictorConfig.NNpredict(message)
        print(predictedMessage)
        return JsonResponse({'message':predictedMessage}, safe=False)

# Create your views here.
