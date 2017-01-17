from django.db.models import *
from django.utils import timezone
from tinymce.models import HTMLField


class Basic(Model):
    """
    Base model for all of the models in the application.
    """
    class Meta:
        abstract = True

    created = DateTimeField(editable=False)
    updated = DateTimeField(editable=False)
    is_active = BooleanField(default=True)

    def save(self, *args, **kwargs):
        """
        Save timezone-aware values for created and updated fields.
        """

        self.created = timezone.now()
        self.updated = timezone.now()
        super(Basic, self).save(*args, **kwargs)

    def __unicode__(self):
        if hasattr(self, "name") and self.name:
            return self.name
        else:
            return "%s" % (type(self))


class Person(Basic):
    """
    """
    class Meta:
        verbose_name_plural = "People"
        ordering = ['name', ]

    name = CharField(max_length=140)
    email = EmailField()
    slug = SlugField(max_length=160, blank=True, null=True)


class Image(Basic):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileField("Image", max_length=200, upload_to="images/")


class Document(Basic):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileField("PDF", max_length=200, upload_to="documents/")


class Sound(Basic):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileField("Audio", max_length=200, upload_to="sounds/")


class Video(Basic):
    name = CharField(max_length=140, null=True, blank=True)
    media = FileField("Video", max_length=200, upload_to="video/")


class Vimeo(Basic):
    name = CharField(max_length=140, null=True, blank=True)
    media = TextField()


class Content(Basic):
    """
    """
    class Meta:
        abstract = True

    name = CharField(max_length=140)
    content = HTMLField(null=True, blank=True)
    slug = SlugField(max_length=160)
    position = PositiveSmallIntegerField(null=True)
