from django.shortcuts import render
import random
import schedule
import threading
import time
import json
import asyncio
from django.http import StreamingHttpResponse, JsonResponse
from .models import TestModel
# Create your views here.

def home(request):
    template_name = 'home/home.html'
    data = TestModel.objects.all()
    context = {
        'data': data,
    }
    return render(request, template_name, context)

# json===============
def stream_data(request):
    def stream_data_generator():
        queryset = TestModel.objects.all()
        for obj in queryset:
            json_data = json.dumps({'id': obj.id, 'number': str(obj.number)})
            print('json data =====>', json_data)
            yield json_data

    response = StreamingHttpResponse(stream_data_generator(), content_type='application/json')
    response['Cache-Control'] = 'no-cache'
    return response


# text/event-stream
# def stream_data(request):
#     def stream_data_generator():
#         queryset = TestModel.objects.all()
#         for obj in queryset:
#             yield json.dumps({'id': obj.id, 'number': str(obj.number)})

#     response = StreamingHttpResponse(stream_data_generator(), content_type="text/event-stream")
#     response['Cache-Control'] = 'no-cache'
#     return response

def save_test_model():
    num = random.random()
    TestModel.objects.create(number=num)
    print('Auto saved on model=================> ',num)

# ================ start schedular ================ 
def run_scheduler():
	while True:
		schedule.run_pending()
		time.sleep(1)

# schedule.every(1).minutes.do(save_test_model)
schedule.every(10).seconds.do(save_test_model)
threading.Thread(target=run_scheduler).start()
# ================== end schedular ================