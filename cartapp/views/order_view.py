from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from cartapp.models.order import Order
from cartapp.serializers.order_serializer import OrderSerializer


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    # list, single order
    def get(self, request, pk=None):
        if pk is not None:
            order = Order.objects.get(id=pk)
            serializer = OrderSerializer(order)
        else:
            orders = Order.objects.filter(customer_id=request.user.id)
            serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data)

    # create
    def post(self, request):
        serializer = OrderSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()

        return Response('Order placed successfully')

    # update
    def put(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderSerializer(instance=order, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    # delete
    def delete(self, request, pk):
        order = Order.objects.get(id=pk)
        order.delete()

        return Response('Delete Successfully')
