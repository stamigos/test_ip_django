from django.db import models


class Camera(models.Model):
    class Meta:
        verbose_name = 'Camera'
        verbose_name_plural = 'Cameras'

    ip = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __unicode__(self):
        return 'Camera IP: %s' % self.ip

    def get_url(self):
        return '<a href="http://{ip}/">camera IP: {ip} </a>'.format(ip=self.ip)

