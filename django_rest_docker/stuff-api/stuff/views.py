from rest_framework import generics
from .serializer import StuffSerializer
from .models import Stuff
from .permissions import IsOwnerOrReadOnly

class StuffList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

class StuffDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer