shelf1 = ("celery", "spinach", "cucumbers")
shelf1_update = ["tomatoes", "celery", "cilantro"]
shelf1_update_tuple = tuple(shelf1_update)
shelf1_concat = shelf1 + shelf1_update_tuple
celery_count = shelf1_concat.count("celery")
celery_index = shelf1_concat.index("celery")
print(f"updated shelf #1:{shelf1_concat}")
print("Number of Celery:", celery_count)
print("Celery Index:", celery_index)