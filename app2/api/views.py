from app2.models import Data
from app2.api.serialization import DataSerializer
from rest_framework import viewsets


class DataViewsSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer



