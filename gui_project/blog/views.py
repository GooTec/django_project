from django.shortcuts import render
from .models import DailyLog

# Create your views here.
def index(request):
    dailyLogs = DailyLog.objects.all()
    return render(request, 'blog/index.html', {'dailyLogs' : dailyLogs})
