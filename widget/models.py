from django.db import models


class thingster(models.Model):
  Group = models.CharField(max_length=10, null=True, blank=True)



class Thingy(models.Model):
  Name = models.CharField(max_length=10, null=True, blank=True)
  body = models.TextField(null=True, blank=True)

  group_name = models.ForeignKey(thingster, null=True, related_name='+')



