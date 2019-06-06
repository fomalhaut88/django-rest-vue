from rest_framework import serializers

from . import models


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {'read_only': False, 'required': True},
            'name': {'required': False},
        }


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = ('id', 'first_name', 'last_name', 'age', 'full_name', 'secret', 'country')
        read_only_fields = ('full_name',)
        extra_kwargs = {
            'secret': {'write_only': True},
        }

    country = CountrySerializer(required=False, allow_null=True)

    def update(self, instance, validated_data):
        if 'country' in validated_data:
            country = validated_data['country']
            instance.country_id = country['id'] if country is not None else None
            del validated_data['country']
        return super().update(instance, validated_data)
