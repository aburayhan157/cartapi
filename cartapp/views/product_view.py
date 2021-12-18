from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cartapp.models.product import Product
from cartapp.serializers.product_serializer import ProductSerializer


class ProductView(APIView):
    permission_classes = (IsAuthenticated,)

    # list, single product
    def get(self, request, pk=None):
        if pk is not None:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    # create
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    # update
    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    # delete
    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()

        return Response('Delete Successfully')
