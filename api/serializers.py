from habit.models import Habit, Record, User
from rest_framework import serializers


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = (
            "pk",
            "name",
            "action",
            "target",
            "units",
            "start",
        )

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = (
            "pk",
            "habit",
            "date",
            "record",
            "units",
        )

class HabitRecordsSerializer(serializers.ModelSerializer):
    records = RecordsSerializer(many=True, required=False, source='habits')
    class Meta:
        model = Habit
        fields = (
            "pk",
            "name",
            "records",
        )

# class UserSerializer(serializers.ModelSerializer):
#   habits = HabitSerializer.PrimaryKeyRelatedField(many=True, queryset = Habit.objects.all())
#   class Meta:
#     model = User
#     fields = (
#       "id",
#       "username",
#       "habits",
#     )