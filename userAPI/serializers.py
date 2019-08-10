from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import UserProfile as User

from rest_framework.serializers import (
    CharField,
    EmailField,
    ModelSerializer,
    ValidationError,
    ImageField
)


# User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            # 'avatar'
        ]
        extra_kwargs = {'password':
                            {'write_only': True}
                        }
    def validate(self, data):
        email = data['email']
        user_qs = User.objects.filter(email=email)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        # avatar = validated_data['avatar']
        user_obj = User(
            username = username,
            email = email,
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=True, allow_blank=True)
    email = EmailField(label= 'Email Address', required=True, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'token'
        ]
        extra_kwargs = {'password':
                            {'write_only': True}
                        }
    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        username = data.get('username', None)
        password = data['password']
        if not email and not username:
            raise ValidationError('A username or email is required to login.')
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
        ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user_obj= user.first()
        else:
            raise ValidationError("This username/email is not registered.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again")

        data['token'] = "Some Random Token"
        return data
