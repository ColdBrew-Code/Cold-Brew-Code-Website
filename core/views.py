from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("Hello, world!")


def not_found(request, exception):
    return HttpResponseNotFound("Page not found.")
