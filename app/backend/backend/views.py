from django.http import JsonResponse

def api(request):
    
    return JsonResponse({'message': 'Hello, World!'}, safe=False)

