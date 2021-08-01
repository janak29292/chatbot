from django.urls import path

from chatapp.views import IntentList, StateList, QueryDetail, ResponseDetail

urlpatterns = [
    path('intents/', IntentList.as_view()),
    path('states/<int:intent_id>/', StateList.as_view()),
    path('query/<int:intent_id>/<int:state_id>/', QueryDetail.as_view()),
    path('response/<int:pk>/', ResponseDetail.as_view()),
]
