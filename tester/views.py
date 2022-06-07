from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .tasks import print_something
import requests
# Create your views here.


#cache data for 10 seconds
#cache uses redis/dragonfly
# @cache_page(10)
def say_hello(request):
    #start task that uses celery, flower and redis/dragonfly
    print_something.delay('Hello')
    key = 'httpbin_result'
    data = cache.get(key)
    if data is None:
        response = requests.get('https://httpbin.org/delay/5')
        data = response.json()
        cache.set(key,data,10)
    # or the following coupled with cache_page
    # response = requests.get('https://httpbin.org/delay/5')
    # data = response.json()
    return render(request, 'hello.html', {'name': data})
