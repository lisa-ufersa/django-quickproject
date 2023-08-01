from rest_framework.serializers import ModelSerializer

from users.models import UserProfileExample

class UserProfileExampleSerializer(ModelSerializer):

    class Meta:
        model = UserProfileExample
        fields = ['id', 'username', 'email', 'address', 'phone_number', 'birth_date', 'user']