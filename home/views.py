from django.shortcuts import render
import random
import schedule
import threading
import time
import json
from django.http import StreamingHttpResponse
from .models import TestModel
# Create your views here.

def home(request):
    template_name = 'home/home.html'
    data = TestModel.objects.all()
    context = {
        'data': data,
    }
    return render(request, template_name, context)

def get_data_dynamically(request):
      def get_object():
        queryset = TestModel.objects.all()
        for item in queryset.iterator():
             yield json.dumps({'number':item.number})
      return StreamingHttpResponse(get_object(),content_type='application/json')

def save_test_model():
    num = random.random()
    TestModel.objects.create(number=num)
    print('Auto saved on model=================> ',num)



# ================ start schedular ================ 
def run_scheduler():
	while True:
		schedule.run_pending()
		time.sleep(1)

schedule.every(1).minutes.do(save_test_model)
threading.Thread(target=run_scheduler).start()
# ================== end schedular ================