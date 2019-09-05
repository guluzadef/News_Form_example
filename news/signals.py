from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import News,Notification

@receiver(post_save, sender=News, dispatch_uid="create_news")
def create_news(sender, **kwargs):
    instance = kwargs.get('instance')
    created = kwargs.get('created')

    if created:
        Notification.objects.create(
            options="bazaya_melumat_daxil_olundu",
            info=instance
        )

