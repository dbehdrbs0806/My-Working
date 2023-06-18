from django.http import HttpResponse

def locker_main(request):
    return HttpResponse("locker 페이지입니다.")
