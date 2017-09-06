from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Group(models.Model):
    name = models.CharField('name', max_length=100)
    vk_groip_id = models.CharField('vk group id', max_length=100)
    description = models.TextField('Description')

    def __str__(self):
        return str('[{}] {}').format(self.id, self.name)


class UserGroup(models.Model):
    vk_id = models.CharField('vk_id', max_length=100, db_index=True)
    group = models.ForeignKey('Group', db_index=True)
    name = models.CharField('name', max_length=100)
    in_time = models.DateTimeField(default=timezone.now)
    out_time = models.DateTimeField(null=True,blank=True)

    class Meta:
        unique_together = (('vk_id', 'group'),)

    def __str__(self):
        return str('[{}] {} - {}').format(self.id, self.vk_id, self.group)
