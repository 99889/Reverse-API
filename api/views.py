from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def reverse_string(request):
    if request.method == 'POST':
        print(request.POST)
        input_string = request.POST.get('string')
        print('try',input_string)
        if input_string:
            output_string = input_string[::-1]
            return JsonResponse({'result': output_string})
        else:
            return JsonResponse({'error': 'Invalid request method'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
