from rest_framework import serializers
from .models import User, Coords, PerevalAdded, PerevalAreas, Images


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'fam', 'otc', 'email', 'phone')


class PerevalAddedSerializer(serializers.ModelSerializer):
    coords = CoordsSerializer()
    user = UserSerializer()

    class Meta:
        model = PerevalAdded
        fields = ('date_added', 'beauty_title', 'title', 'other_titles', 'connect', 'add_time', 'winter',
                  'summer', 'autumn', 'spring', 'coords', 'user', 'status')

    def create(self, validated_data):
        coord_data = validated_data.pop('coords')
        user_data = validated_data.pop('user')
        coords = Coords.objects.create(**coord_data)
        user = User.objects.create(**user_data)
        pereval = PerevalAdded.objects.create(coords=coords, user=user, **validated_data)
        return pereval


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('date_added', 'title', 'data')

    def create(self, validated_data):
        image = Images(**validated_data)
        return image


class PerevalAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAreas
        fields = ('id_parent', 'title')
