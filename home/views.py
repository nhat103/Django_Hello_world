from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
TEMPLATES_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)


def index(request):
    # return HttpResponse("Hello word. You're at home")
    # return HttpResponse("<html><head></head><body>.....")
    today = datetime.datetime.now().date()
    # return render(request, "index.html")
    return render(request, "index.html", {"today": today})
