from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Process the data here
            # fname = data.get('fname')
            all_data = data.get('data')
            # start_time = data.get('start_time')
            # energy_consumption = data.get('energy_consumption')
            # battery_percentage = data.get('battery_percentage')

            print(f'data received: {all_data}')

            return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
