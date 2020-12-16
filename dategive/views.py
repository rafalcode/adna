from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import datetime, time

def dgive_show(request):
    cur_date = datetime.datetime.now().strftime("For EBI01717 today is: %d %b %Y / Time now is %H:%M")
    data = {"date": cur_date}
    return JsonResponse(data)
