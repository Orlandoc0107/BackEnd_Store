from rest_framework import viewsets, status
from store.models import Store
from store.serializers import StoreSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        store = Store.objects.all()
        serializer = StoreSerializer(store, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            store = serializer.save()
            return Response(StoreSerializer(store).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        store = self.get_store(pk)
        if store is None:
            return Response({"error": f"La tienda con pk={pk} no existe"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        store = self.get_store(pk)
        if store is None:
            return Response({"error": f"La tienda con {pk} no existe"}, status=status.HTTP_404_NOT_FOUND)

        store.delete()
        return Response({"message": f"La tienda con {pk} ha sido eliminada"}, status=status.HTTP_204_NO_CONTENT)

    def get_store(self, pk):
        return get_object_or_404(Store, pk=pk)
