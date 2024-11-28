import json
import traceback

from rest_framework.exceptions import ValidationError
from ..models import Status, IndexNameStatus
from ..serializers import VideoTranslationMessageSerializer
from ..utils.create_faiss_index import create_faiss_index
from ..utils.s3_downloader import download_s3_file
from .youtube2Medium import convert_to_article

def process_text_processing_request(ch, method, properties, body):
    try:
        print("i recived the message")
        message = json.loads(body)
        serializer = VideoTranslationMessageSerializer(data=message)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        video_translation_message = serializer.validated_data

        print(video_translation_message)

        index_name_status = IndexNameStatus.objects.create(
            index_name=video_translation_message['request_id'],
            status=Status.RECEIVED
        )

        index_name_status.status = Status.IN_PROGRESS
        index_name_status.save()

        s3_file_url = video_translation_message['s3_file_url']
        print("im here just before the download")
        file_content = download_s3_file(s3_file_url)

        if not file_content:
            raise ValueError("Failed to download the file from S3.")

        print("im here just after the download")

        faiss_index_name = create_faiss_index(file_content, video_translation_message['request_id'])

        if not faiss_index_name:
            raise ValueError("Failed to create FAISS index.")

        index_name_status.status = Status.READY
        index_name_status.save()

        print(convert_to_article(index_name_status.index_name, 3))

    except Exception as e:
        # ch.basic_nack(delivery_tag=method.delivery_tag)
        traceback.print_exc()
        return None

    ch.basic_ack(delivery_tag=method.delivery_tag)

    return
