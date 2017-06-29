import decimal
from rest_framework import serializers as rest_serializers
from apps.company.models import Manufacturer, Company, Material


class CompanySerializer(rest_serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'id')


class MaterialSerializer(rest_serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = ('name', 'id')


class ManufacturerSerializer(rest_serializers.ModelSerializer):
    company = CompanySerializer()
    material = MaterialSerializer()

    class Meta:
        model = Manufacturer
        fields = ('company', 'material', 'unit_price',)

    def to_representation(self, instance):
        data = super(ManufacturerSerializer, self).to_representation(instance)
        volume = self.context['volume']
        data.update({'total_price': instance.unit_price * decimal.Decimal(volume)})
        return data


class QueryParamsSerializer(rest_serializers.Serializer):
    name = rest_serializers.CharField()
    volume = rest_serializers.FloatField()
