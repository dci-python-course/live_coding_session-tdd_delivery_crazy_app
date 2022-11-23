from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


@api_view(http_method_names=['GET', 'POST'])
def list_restaurants(request):
    if request.method == 'GET':
        restaurants = RestaurantSerializer(data=Restaurant.objects.all(), many=True)
        if restaurants.is_valid():
            return Response(status=200, data=restaurants.data)
        return Response(status=200, data=list())

    elif request.method == 'POST':
        seriliazer = RestaurantSerializer(data=request.POST)
        if seriliazer.is_valid():
            seriliazer.save()
        return Response(status=201)
