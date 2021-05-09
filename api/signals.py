from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Alloc, AllocLog


@receiver(post_save, sender=Alloc)
def post_save_Alloc(sender, instance, created, **kwargs):
    # print('instance', instance)
    # print('instance Id = ', instance.allocId)
    log = AllocLog(
        allocId=instance.allocId,
        date=instance.date,
        session=instance.session,
        duty=instance.duty,
        staff=instance.staff,
        savedBy=instance.savedBy,
        created=instance.created,
        modified=instance.modified
    )
    log.save()
