from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def get_rectangle_area(request, width, height):
    rectangle = width * height
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна "
                        f"{rectangle}")


def get_square_area(request, width):
    square = width * width
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна "
                        f" {square}")


def get_circle_area(request, radius):
    circle = 3.14 * radius * radius
    return HttpResponse(f"Площадь круга размером с радиусом {radius} равна {circle}")


def get_rectangle_area2(request, width, height):
    # redirect_name = reverse("rectangle-name", args=[width, height])
    # return HttpResponseRedirect(redirect_name)
    return render(request, 'geometry/rectangle.html')


def get_square_area2(request, width):
    # redirect_name2 = reverse("square-name", args=(width, ))
    # return HttpResponseRedirect(redirect_name2)
    return render(request, 'geometry/square.html')


def get_circle_area2(request, radius):
    # redirect_name3 = reverse("circle-name", args=(radius, ))
    # return HttpResponseRedirect(redirect_name3)
    return render(request, 'geometry/circle.html')
