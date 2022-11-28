from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


@api_view(http_method_names=['GET', 'POST'])
def list_restaurants(request):
    if request.method == 'GET':
        restaurants = RestaurantSerializer(Restaurant.objects.all(), many=True)
        return Response(status=200, data=restaurants.data)
    elif request.method == 'POST' and request.content_type == 'application/json':
        seriliazer = RestaurantSerializer(data=request.data)
        if seriliazer.is_valid():
            seriliazer.save()
            return Response(status=201)
        else:
            return Response(status=400, data=seriliazer.errors)
    else:
        return Response(status=400)

# class RestaurantViewSet(mixins.CreateModelMixin,
#                         mixins.ListModelMixin,
#                         GenericViewSet):
#
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer
