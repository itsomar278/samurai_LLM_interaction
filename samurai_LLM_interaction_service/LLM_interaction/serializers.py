from rest_framework import serializers


class VideoTranslationMessageSerializer(serializers.Serializer):
    request_id = serializers.UUIDField()
    user_id = serializers.FloatField()
    s3_file_url = serializers.URLField()
    transcription_text = serializers.CharField(allow_blank=True, required=False)

