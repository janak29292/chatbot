from rest_framework import serializers

from chatapp.models import Intent, State, Option, Query, Response


class IntentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Intent
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ('id', 'name')


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):

    class Meta:
        model = Query
        fields = ('response',)


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Response
        fields = '__all__'
        depth = 1
