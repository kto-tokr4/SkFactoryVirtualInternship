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

    def update(self, instance, validated_data):
        # coord_data = validated_data.pop('coords')
        # coords = instance.coords
        # print (coords, coord_data)
        # print (Coords.objects.filter(pk=instance.coords.id).update(**coord_data))



        instance.beauty_title = validated_data.get("beauty_title", instance.beauty_title)
        instance.title = validated_data.get("title", instance.title)
        instance.other_titles = validated_data.get("other_titles", instance.other_titles)
        instance.connect = validated_data.get("connect", instance.connect)
        instance.add_time = validated_data.get("add_time", instance.add_time)
        instance.winter = validated_data.get("winter", instance.winter)
        instance.summer = validated_data.get("summer", instance.summer)
        instance.autumn = validated_data.get("autumn", instance.autumn)
        instance.spring = validated_data.get("spring", instance.spring)

        coord_data = validated_data.pop('coords')
        Coords.objects.filter(pk=instance.coords.id).update(**coord_data)

        # instance.coords = Coords.objects.filter(pk=coords.id).update(**coord_data)
        # instance.coords = Coords.objects.filter(pk=instance.coords.id).update(**coord_data)

        instance.save()
        return instance




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
