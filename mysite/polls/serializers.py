from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Choice


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class QuestionSerializers(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question_text', 'pub_date')


class ChoiceSerializers(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes')
