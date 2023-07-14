from django.shortcuts import render
from .models import AppThree, PostAPI
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .Serial3 import IS, IS1
from .models import AppThree
from rest_framework.views import APIView
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# .......................................................................................................


from django.http.response import Http404

# # from .models import Todo
# from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import generics


class YourModelListCreateAPIView(generics.ListCreateAPIView):
    queryset = AppThree.objects.all()
    serializer_class = IS


class YourModelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppThree.objects.all()
    serializer_class = IS


# class SWIFTRIDE(APIView):
#     # READ a single Todo
#     def get_object(self, pk):
#         try:
#             return AppThree.objects.get(pk=pk)
#         except AppThree.DoesNotExist:
#             raise Http404

#     def get(self, request, pk=None, format=None):
#         if pk:
#             data = self.get_object(pk)
#         else:
#             data = AppThree.objects.all()

#         serializer = IS(data, many=True)

#         return Response(serializer.data)

#     def post(self, request, format=None):
#         data = request.data
#         serializer = IS(data=data)

#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         response = Response()

#         response.data = {
#             "message": " Created Successfully",
#             "data": serializer.data,
#         }

#         return response

#     def put(self, request, pk=None, format=None):
# todo_to_update = AppThree.objects.get(pk=pk)
#         serializer = IS(instance=todo_to_update, data=request.data, partial=True)

#         serializer.is_valid(raise_exception=True)

#         serializer.save()

#         response = Response()

#         response.data = {
#             "message": "Todo Updated Successfully",
#             "data": serializer.data,
#         }

#         return response

#     def delete(self, request, pk, format=None):
#         todo_to_delete = AppThree.objects.get(pk=pk)

#         todo_to_delete.delete()

#         return Response({"message": "Todo Deleted Successfully"})


# .............................................................................................................
# @api_view(["GET"])
# def getData(request):
#     # obj = {"name": "Example demo Name", "age": 30}
#     obj = AppThree.objects.all()
#     serial = IS(obj, many=True)
#     return Response(serial.data)


# @api_view(["POST"])
# def postData(request, pk):
#     obj1 = PostAPI.objects.get(id=pk)
#     serial1 = IS1(obj1, many=False)
#     return Response(serial1.data)


# @api_view(["POST"])
# def postData1(request):
#     serial1 = IS1(data=request.data)
#     if serial1.is_valid():
#         serial1.save()

#     return Response(serial1.data)


# @api_view(["POST"])
# def update(request, pk):
#     obj1 = PostAPI.objects.get(id=pk)
#     serial1 = IS1(instance=obj1, data=request.data)
#     return Response(serial1.data)


# @api_view(["DELETE"])
# def delete(request, pk):
#     obj1 = PostAPI.objects.get(id=pk)
#     obj1.delete()
#     return Response("item successfully deleted!!!!!!!!!")


# Create your views here.
def fun(request):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, "fun.html", {"list1": a})


def data(request):
    d = {}
    if request.method == "POST":
        name = request.POST["name"]
        srn = request.POST["srn"]
        age = request.POST["age"]
        college = request.POST["college"]
        city = request.POST["city"]
        obj = AppThree(Name=name, SRN=srn, AGE=age, College=college, City=city)
        obj.save()
        if srn not in d:
            d[srn] = [name, age, college, city]
        # ----------------------------------------------------
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     'data_group',  # Group name that WebSocket consumers are listening to
        #     {'type': 'send_data', 'data': d}
        # )
        # ------------------------------------------------------
    return render(request, "AppThree.html", {"list": d})


def display(request):
    obj1 = AppThree.objects.all()
    return render(request, "AppThree.html", {"obj": obj1})


class UserAPIView(APIView):
    serial = IS

    def get_queryset(self):
        obj = AppThree.objects.all()
        return obj
