# Create your views here.
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView

from chatapp.models import Intent, State, Query, Response
from rest_framework.response import Response as APIResponse

from chatapp.serializers import IntentSerializer, StateSerializer, QuerySerializer, ResponseSerializer


class IntentList(ListAPIView):
    serializer_class = IntentSerializer
    queryset = Intent.objects.all()


class StateList(ListAPIView):
    serializer_class = StateSerializer

    def get_queryset(self):
        return State.objects.filter(intents__id=self.kwargs.get('intent_id'))


class QueryDetail(RetrieveAPIView):
    serializer_class = QuerySerializer
    queryset = Query.objects.all()

    @swagger_auto_schema(manual_parameters=[
            openapi.Parameter(name='query_id', in_=openapi.IN_QUERY,
                              type=openapi.TYPE_INTEGER,
                              description='Query Id'),
            openapi.Parameter(name='option_id', in_=openapi.IN_QUERY,
                              type=openapi.TYPE_INTEGER,
                              description='Option_id'),
    ])
    def get(self, request, *args, **kwargs):
        intent_id = self.kwargs.get('intent_id')
        state_id = self.kwargs.get('state_id')
        query_id = request.GET.get('query_id')
        option_id = request.GET.get('option_id')
        try:
            instance = self.queryset.get(
                intent__id=intent_id,
                state__id=state_id,
                query__id=query_id,
                option__id=option_id
            )
        except Query.DoesNotExist:
            raise NotFound(detail="No response Found", code=404)
        serializer = self.get_serializer(instance)
        return APIResponse(serializer.data)


class ResponseDetail(RetrieveAPIView):
    serializer_class = ResponseSerializer
    queryset = Response.objects.all()
