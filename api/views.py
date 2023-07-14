from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from apptwo.models import Rate


@api_view(["GET"])
def getData(request):
    # obj = {"name": "Example demo Name", "age": 30}
    obj = Rate.objects.all()
    serial = ItemSerializer(obj, many=True)
    return Response(serial.data)
