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

# def stream_data(request):
#     def stream_data_generator():
#         queryset = TestModel.objects.all()
#         data = []
#         for obj in queryset:
#             id = obj.id
#             number = str(obj.number)
#             data.append({'id': id, 'number': number})
#             # json_data = json.dumps(data)
#             # # print('ok ==>', obj.number)
#             # yield json_data
#         json_data = json.dumps(data)
#         yield json_data
#         # data = list(TestModel.objects.values())
#         # data = JsonResponse(data, safe=False)
#         # yield data

#     response = StreamingHttpResponse(stream_data_generator(), content_type='text/event-stream')
#     # response = StreamingHttpResponse(stream_data_generator(), content_type="application/json")
#     return response


# text/event-stream
# def stream_data(request):
#     def stream_data_generator():
#         queryset = TestModel.objects.all()
#         for obj in queryset:
#             yield json.dumps({'id': obj.id, 'number': str(obj.number)})

#     response = StreamingHttpResponse(stream_data_generator(), content_type="text/event-stream")
#     response['Cache-Control'] = 'no-cache'
#     return response

# json===============
def stream_data(request):
    def stream_data_generator():
        queryset = TestModel.objects.all()
        for obj in queryset:
            yield json.dumps({'id': obj.id, 'number': str(obj.number)})

    response = StreamingHttpResponse(stream_data_generator(), content_type='application/json')
    response['Cache-Control'] = 'no-cache'
    return response

def my_view(request):
    def generate_data():
        for i in range(100000):
            print('data==========> ', i)
            # time.sleep(10)
            yield f"Chunk {i}\n"  # Replace with your data generation logic

    response = StreamingHttpResponse(generate_data(), content_type="text/plain")
    return response

def astreaming(_):
    async def stream():
        for i in range(10):
            await asyncio.sleep(5)
            yield f"Chunk: {i}\n".encode()

    return StreamingHttpResponse(stream())

# def get_data_dynamically(request):
#       def get_object():
#         queryset = TestModel.objects.all()
#         for item in queryset.iterator():
#              yield json.dumps({'number':item.number})
#         return StreamingHttpResponse(get_object(),content_type='application/json')

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
threading.Thread(target=run_scheduler).start()
# ================== end schedular ================