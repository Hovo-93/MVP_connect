from .models import User

from rest_framework.serializers import ModelSerializer


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone'
        )


class UserDetailSerializer(ModelSerializer):
    """
        Детальная информация
    """
    class Meta:
        model = User
        fields = '__all__'
