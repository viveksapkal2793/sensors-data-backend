from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SensorData
from django.utils import timezone
from datetime import datetime

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            all_data = data.get('data')

            # print(f'data received: {all_data}')

            for row in all_data[1:]:  # Skip header row
                naive_datetime = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f')
                aware_datetime = timezone.make_aware(naive_datetime, timezone.get_current_timezone())
                SensorData.objects.create(
                    date=aware_datetime,
                    acc_x=row['Accvalue'][0],
                    acc_y=row['Accvalue'][1],
                    acc_z=row['Accvalue'][2],
                    gyro_x=row['Gyrovalue'][0],
                    gyro_y=row['Gyrovalue'][1],
                    gyro_z=row['Gyrovalue'][2],
                    latitude=row['lat'],
                    longitude=row['long'],
                    activity_name=row['activity_name'],
                    behaviour_name=row['behaviour_name'],
                    custom_event=row['custom_event']
                )

            return JsonResponse({'status': 'success', 'message': 'Data received successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
