from django.shortcuts import render
import random
import schedule
import threading
import time
from .models import TestModel
# Create your views here.

def home(request):
    template_name = 'home/home.html'
    return render(request, template_name)

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