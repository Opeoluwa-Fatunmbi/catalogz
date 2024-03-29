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

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)
    desc = models.TextField(_("Description"))
    image = models.ImageField(default="fallback.jpg", upload_to="gallery/")
    media_type = models.CharField(
        max_length=3, choices=MediaType.choices, default=MediaType.IMAGE
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name