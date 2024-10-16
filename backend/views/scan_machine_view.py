import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from backend.models import Machine

from backend.service import get_machine_available_info as gmai


@csrf_exempt
def scan_machine(request, id):
    if request.method == 'POST':
        try:
            if not id:
                return JsonResponse({'error': 'don\'t has id in request'}, status=400)

            machine_info = Machine.objects.get(id=id)
            if not machine_info:
                return JsonResponse({'error': 'don\'t has this data in DB'}, status=400)
            ip_address = machine_info.ip_address
            user_name = machine_info.user_name
            password = machine_info.password
            cpu_usage_info = gmai.get_cpu_usage_rate(ip_address, user_name, password)
            mem_usage_info = gmai.get_mem_usage_rate(ip_address, user_name, password)
            pattern = r"[-+]?\d*\.\d+|\d+"
            cpu_usage_rate = re.findall(pattern, cpu_usage_info)
            mem_usage_rate = re.findall(pattern, mem_usage_info)
            data = {
                "ip_address": ip_address,
                "cpu_usage_rate": cpu_usage_rate[1],
                "mem_usage_rate": mem_usage_rate[1]
            }
            return JsonResponse({'data': data}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
