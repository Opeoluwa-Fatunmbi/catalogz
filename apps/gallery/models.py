from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from autoslug import AutoSlugField
from apps.accounts.models import User

# Create your models here.


class Media(BaseModel):
    class MediaType(models.TextChoices):
        IMAGE = "IMG", _("Image")
        VIDEO = "VID", _("Video")

    class FormatType(models.TextChoices):
        JPEG = "JPEG", _("JPEG")
        PNG = "PNG", _("PNG")
        MP4 = "MP4", _("MP4")

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)
    desc = models.TextField(_("Description"))
    image = models.ImageField(default="fallback.jpg", upload_to="gallery/")
    media_type = models.CharField(
        max_length=3, choices=MediaType.choices, default=MediaType.IMAGE
    )
    dimensions = models.CharField(max_length=50, blank=True, null=True)
    format = models.CharField(
        max_length=4, choices=FormatType.choices, default=FormatType.JPEG
    )

    def __str__(self):
        return self.name
