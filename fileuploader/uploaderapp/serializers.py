from rest_framework import serializers
from uploaderapp.models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        # fields = ["id", "uploaded_at", "file", "processed"]
        fields = "__all__"
