from rest_framework import serializers
from .models import Disease, RawImage, Report, RawImageMobile, ReportMobile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class RawImageSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = RawImage
        exclude = ['user']
        # fields = '__all__'
        lookup_field = 'id'     


class ChoiceField(serializers.ChoiceField):

    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        # To support inserts with the value
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)


class DiseaseSerializer(serializers.ModelSerializer):
    name = ChoiceField(
        choices = Disease.DISEASE_CHOICES
    )
    severity = ChoiceField(
        choices = Disease.SEVERITY_CHOICES
    )
    class Meta:
        model = Disease
        fields = '__all__'
        depth = 1

    def get_name(self, obj):
        return obj.get_name_display()

class ReportSerializer(serializers.ModelSerializer):
    raw_image = RawImageSerializer(many=False)
    disease = DiseaseSerializer(many=False)

    class Meta:
        model = Report
        exclude = ['user']
        depth = 2
        lookup_field = 'id'

    


class RawImageMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawImageMobile
        fields = '__all__'
        lookup_field = 'id'

class ReportMobileSerializer(serializers.ModelSerializer):
    raw_image = RawImageMobileSerializer(many=False)
    disease = DiseaseSerializer(many=False)

    class Meta:
        model = ReportMobile
        fields = '__all__'
        depth = 2
        lookup_field = 'id'