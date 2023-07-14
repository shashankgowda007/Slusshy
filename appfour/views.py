from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import M
from .serializer import Data


# Create your views here.
@api_view(["GET", "POST", "PUT"])
def main(request):
    c = {"abc": "def"}
    if request.method == "GET":
        print(request.GET.get("search"))
        print("Get method")
        return Response(c)
    elif request.method == "POST":
        data = request.data

        print(">>>>>>>>>")
        print(data)
        print("<<<<<<<<<<<<<<<<<<<<")
        print("POST method")
        return Response(data["name"])
    elif request.method == "PUT":
        print("PUT method")
        return Response(c)


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def main2(request):
    if request.method == "GET":
        obj = M.objects.all()
        serial = Data(obj, many=True)
        return Response(serial.data)

    elif request.method == "POST":
        data = request.data
        ser = Data(data=data)
        if ser.is_valid():
            ser.save()

            return Response(ser.data)
        else:
            return Response(ser.errors)

    elif request.method == "PUT":
        data = request.data
        ser = Data(data=data)
        if ser.is_valid():
            ser.save()

            return Response(ser.data)
        else:
            return Response(ser.errors)

    elif request.method == "PATCH":
        data = request.data
        obj = M.objects.get(id=data["id"])
        ser = Data(obj, data=data, partial=True)

        if ser.is_valid():
            ser.save()

            return Response(ser.data)
        else:
            return Response(ser.errors)
    else:
        data = request.data
        obj = M.objects.get(id=data["id"])
        obj.delete()
        return Response({"message": "Deleted"})
