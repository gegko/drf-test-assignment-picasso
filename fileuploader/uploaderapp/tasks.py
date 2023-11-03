import time
from celery import shared_task
from uploaderapp.models import File

@shared_task
def process_file(file_id: int) -> None:
    try:
        time.sleep(3)  # some processing...
        file = File.objects.get(id=file_id)
        file.processed = True
        file.save()
    except File.DoesNotExist:
        pass

# from celery import shared_task
# from .models import File

# @shared_task
# def process_uploaded_file(file_id):
#     try:
#         file_instance = File.objects.get(pk=file_id)
#         file_instance.processed = True
#         file_instance.save()
#     except File.DoesNotExist:
#         pass