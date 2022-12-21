from celery.contrib.pytest import celery_app


# this will make sure the app is always imported when
#DJANGO starts so that shared_task will use this app.

__all__ = ('celery_app',)

