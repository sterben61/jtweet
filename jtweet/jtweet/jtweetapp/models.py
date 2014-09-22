from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from jtweet.jtweetapp.managers import JTweetManager

class User(AbstractUser):

    followings = models.ManyToManyField('User',
                                        verbose_name=_('Followings'),
                                        related_name='followers',
                                        null=True,
                                        blank=True)


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


# Create your models here.
@python_2_unicode_compatible
class Jtweet(models.Model):
    text = models.TextField(verbose_name=_('Text'))
    owner = models.ForeignKey(User, verbose_name=_('Owner'))

    objects = JTweetManager()

    def __str__(self):
        return self.text