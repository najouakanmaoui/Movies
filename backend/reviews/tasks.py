from celery import shared_task
import time

__author__ = 'najouakaanmaoui@gmail.com'

@shared_task(name="simulate_processing")
def simulate_processing(review_id):
    time.sleep(10)
    return f"Review {review_id} processing completed."
