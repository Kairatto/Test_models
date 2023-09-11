from rest_framework import serializers
from .models import Tour, Days, DaysImage


class DaysImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaysImage
        fields = ('image',)


class DaysSerializer(serializers.ModelSerializer):
    days_images = DaysImageSerializer(many=True)

    class Meta:
        model = Days
        fields = ('title_days', 'description_days', 'days_images')

    def create(self, validated_data):
        days_images_data = validated_data.pop('days_images')
        days = Days.objects.create(**validated_data)

        for image_data in days_images_data:
            DaysImage.objects.create(day=days, **image_data)

        return days


class TourSerializer(serializers.ModelSerializer):
    days = DaysSerializer(many=True)

    class Meta:
        model = Tour
        fields = ('title_tour', 'text_tour', 'days')

    def create(self, validated_data):
        days_data = validated_data.pop('days')
        tour = Tour.objects.create(**validated_data)

        for day_data in days_data:
            days_images_data = day_data.pop('days_images', [])
            day = Days.objects.create(day=tour, **day_data)

            for image_data in days_images_data:
                DaysImage.objects.create(day=day, **image_data)

        return tour
