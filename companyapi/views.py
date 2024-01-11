from django.http import HttpResponse
def home_page(request):
    # print("Home Page Requested")
    return HttpResponse("This is home page")