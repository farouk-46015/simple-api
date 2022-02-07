from django.db.models import Count
from rest_framework import viewsets , response ,status 

from core.models import Car , Rate
from .serializer import CarListSerializer, CarSerializer , RateSerializer , PopularSerializer
from .utils import check_car_exist

# Create your views here.


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return CarSerializer
        else:
            return CarListSerializer

    def create(self, request, *args, **kwargs):
        make = str(request.data['make']).upper()
        model = str(request.data['model']).upper()
        
        if check_car_exist(make, model):
            return super().create(request, *args, **kwargs) 
        else:
            return response.Response({'detail': '%s with %s does not exist' % (make,model)} , status=status.HTTP_302_FOUND)

    def update(self, request, *args, **kwargs):
        make = str(request.data['make']).upper()
        model = str(request.data['model']).upper()

        if check_car_exist(make, model):
            return super().update(request, *args, **kwargs)
        else:
            return response.Response({'detail': '%s with %s does not exist' % (make,model)} , status=status.HTTP_302_FOUND)
    
    def partial_update(self, request, *args, **kwargs):
        make = str(request.data['make']).upper()
        model = str(request.data['model']).upper()

        if check_car_exist(make, model):
            return super().partial_update(request, *args, **kwargs)
        else:
            return response.Response({'detail': '%s with %s does not exist' % (make,model)} , status=status.HTTP_302_FOUND)
        

class RateViewSet(viewsets.ModelViewSet):
    serializer_class = RateSerializer
    queryset = Rate.objects.all()


class PopularViewSet(viewsets.ViewSet):

    def list(self,request):
        qs = Car.objects.annotate(rates_number=Count('rates')).order_by('-rates_number')
        serializer = PopularSerializer(qs , many=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


