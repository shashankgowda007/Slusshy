from django.shortcuts import render, redirect
from .models import Rate, Signup, Passenger, Rider, MapVal, FileField, Image
from rest_framework.decorators import api_view
from .Serializer import Items, Items1, IS, IS1, IS2, ImageForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
import os
from django.http import HttpResponse

# Create your views here.


@api_view(["GET", "POST", "PUT", "PATCH", "DELETE"])
def main2(request):
    if request.method == "GET":
        obj = Rate.objects.all()
        serial = Items(obj, many=True)
        return Response(serial.data)

    elif request.method == "POST":
        data = request.data
        ser = Items(data=data)
        if ser.is_valid():
            ser.save()

            return Response(ser.data)
        else:
            return Response(ser.errors)

    elif request.method == "PUT":
        data = request.data
        ser = Items(data=data)
        if ser.is_valid():
            ser.save()

            return Response(ser.data)
        else:
            return Response(ser.errors)

    elif request.method == "PATCH":
        data = request.data
        obj = Rate.objects.get(id=data["id"])
        ser = Items(obj, data=data, partial=True)

        if ser.is_valid():
            ser.save()

            return Response(ser.data)
        else:
            return Response(ser.errors)
    else:
        data = request.data
        obj = Rate.objects.get(id=data["id"])
        obj.delete()
        return Response({"message": "Deleted"})


class Rider_api(generics.ListCreateAPIView):
    queryset = Rider.objects.all()
    serializer_class = IS


class Passenger_api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = IS1


class Map_api(generics.ListCreateAPIView):
    queryset = MapVal.objects.all()
    serializer_class = IS2


d = {}


def rate(request):
    return render(request, "ratings.html")


@api_view(["GET"])
def getData(request):
    obj3 = Rate.objects.all()
    item = Items(obj3, many=True)
    return Response(item.data)


@api_view(["GET"])
def getData1(request):
    obj4 = Signup.objects.all()
    item1 = Items1(obj4, many=True)
    return Response(item1.data)


def input(request):
    if request.method == "POST":
        rate = request.POST["rateing"]
        feedback = request.POST["feedback"]
        name = request.POST["name"]
        obj = Rate(rateing=float(rate), feedback=str(feedback), name=str(name))
        obj.save()
        obj2 = Rate.objects.all()
        total_rating = 0
        count = 0
        for i in obj2:
            total_rating += float(i.rateing)
            count += 1
        average = total_rating / count
        db = Rate.objects.all()
        d = {}
        for i in db:
            d[i.name] = float(i.rateing)
        a = []
        m = d.values()

        max1 = max(m)

        for i in d.keys():
            if d[i] == max1:
                if i == name:
                    obj1 = Rate(bestrider=max1)
                    obj1.save()
                a.append(i)
    return render(
        request,
        "out.html",
        {
            "rate": str(rate),
            "feedback": str(feedback),
            "TR": obj2,
            "AR": "{:.2f}".format(average),
            "d": a,
        },
    )


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username not in d.keys():
            d[username] = password
        else:
            username = "isExist"
            password = None
        obj = Signup(username=username, password=password)
        obj.save()
        # obj1=Signup.objects.all()
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        user = request.POST["username"]
        pswd = request.POST["password"]
        msg = "not yet"
        if user in d.keys():
            if pswd == d[user]:
                msg = "ur login successfully"
        else:
            msg = "login id id invalid"

    return render(request, "login.html", {"msg": str(msg)})


def displaydb(request):
    obj1 = Signup.objects.all()
    return render(request, "displaydatabase.html", {"obj": obj1})


d = []
p = []
obj3 = Passenger.objects.all()
for i in obj3:
    d.append(i.Srn)
obj4 = Rider.objects.all()
for i in obj4:
    p.append(i.Srn)

mapping_dict = {}


def create_mapping_dict():
    a_objects = Rider.objects.all()
    b_objects = Passenger.objects.all()

    for i, obj in enumerate(a_objects):
        if i < len(b_objects):
            mapping_dict[obj.Srn] = b_objects[i].Srn
        else:
            default_text = "No driver found"
            mapping_dict[obj.Srn] = default_text
            new_b_obj = Passenger(Srn=default_text)
            new_b_obj.save()
    # obj1 = MAP(MapVal=mapping_dict)
    # obj1.save()
    return mapping_dict


s = ""


def driver(request):
    if request.method == "POST":
        srn1 = request.POST["srn1"]
        s = srn1
        srn2 = request.POST["srn2"]

        if len(str(srn1)) == 0:
            if str(srn2) not in p:
                if srn2 not in d:
                    # obj = Passenger(Srn=srn2)

                    # obj.save()
                    try:
                        existing_data = Passenger.objects.get(Srn=srn2)
                    except Passenger.DoesNotExist:
                        new_data1 = Passenger(Srn=srn2)
                        new_data1.save()
        else:
            if str(srn1) not in d:
                if srn1 not in p:
                    # obj1 = Rider(Srn=srn1)

                    # obj1.save()
                    try:
                        existing_data = Rider.objects.get(Srn=srn1)
                    except Rider.DoesNotExist:
                        new_data = Rider(Srn=srn1)
                        new_data.save()
                    # ----------------------------

        ob = create_mapping_dict()
        k = mapping_dict.items()
        for i in k:
            okk = MapVal(Mapp=i)
            okk.save()

    return render(request, "driver.html", {"map": mapping_dict.items()})


# def passenger(request):
#     if request.method == "POST":

#     return render(request, "driver.html", {"srn2": p})


def file(request):
    if request.method == "POST" and request.FILES.get["file"]:
        f = request.FILES["file"]
        fs = FileSystemStorage()
        filename = fs.save(f.name, f)
        upload = fs.url(filename)
        # filename = default_storage.save(f.name, f)
        # FileField.objects.create(File=filename)
        return render(request, "File.html", {"success": True})
    return render(request, "File.html")


def fetch(request):
    dataobj = MapVal.objects.all()
    for i in dataobj:
        if i.Mapp[:9] == s:
            str11 = i.Mapp[9:]
    return render(request, "driver.html", {"objdata": str11})


def upload_image_(request):
    if request.method == "POST":
        for i in range(1, 11):  # Loop through numbers 1 to 10
            image_file = request.FILES.get(f"image{i}")
            if image_file:
                file_path = os.path.join("image", f"name{i}.jpg")
                default_storage.save(file_path, image_file)
        return HttpResponse(
            "success"
        )  # Replace 'success' with the URL or view name for the success page
    return render(request, "ratings.html")
