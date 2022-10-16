from rest_framework import serializers
from todo.models import Todo
from django.template.defaultfilters import slugify


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Todo
        fields = "__all__"
        extra_kwargs = {
            "slug": {"read_only": True}
        }

    def create(self, validated_data):
        todo = Todo.objects.create(
            title=validated_data["title"],
            user=validated_data["user"],
            slug=slugify(validated_data["title"])
        )
        return todo
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
