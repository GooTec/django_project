from django.shortcuts import render
from .models import DailyLog

# Create your views here.
def index(request):
    dailylogs = DailyLog.objects.all()
    return render(request, 'blog/index.html', {'dailyLogs': dailylogs})


def category(request, category_num):
    if category_num == 1:
        cate_name = 'food'
    elif category_num == 2:
        cate_name = 'music'
    else : 
        cate_name = 'programming'
    dailylogs = DailyLog.objects.get(category=cate_name)
    return render(request, 'blog/category.html', {'dailyLogs': dailylogs})


def detail(request, dailylog_id):
    try:
        dailylog = DailyLog.objects.get(pk=dailylog_id)
    except DailyLog.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'blog/single.html', {'dailylog': dailylog})

