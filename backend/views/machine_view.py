from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from backend.models import Machine


@csrf_exempt
def get_list(request):
    if request.method == 'GET':
        try:
            machineList = [];
            machines = Machine.objects.all()
            for machine in machines:
                data = {
                    "id": machine.id,
                    "ip_address": machine.ip_address,
                    "user_name": machine.user_name,
                    "password": machine.password
                }
                machineList.append(data)
            return JsonResponse({"data": machineList})
        except Exception:
            return JsonResponse({'error': 'Exception JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)

@csrf_exempt
def serv_add(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ip_address = data.get('ip_address')
            user_name = data.get('user_name')
            pwd = data.get('pwd')

            if not ip_address or not user_name or not pwd:
                return JsonResponse({'error': 'ipAddress,userName and password are required'}, status=400)

            machine_info = Machine(ip_address=ip_address, user_name=user_name, password=pwd)
            machine_info.save()

            return JsonResponse({'message': 'machine info saved successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

@csrf_exempt
def active_machine(request, id):
    if request.method == 'POST':
        try:
            if not id:
                return JsonResponse({'error': 'id are required'}, status=400)
            machine_info = Machine.objects.get(id=id)
            machine_info.active_statu = True
            machine_info.save()
            return JsonResponse({'message': 'machine statu saved successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
