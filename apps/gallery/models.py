from django.db import models
from django.utils.translation import gettext_lazy
from apps.common.models import BaseModel
from autoslug import AutoSlugField

# Create your models here.



class Gallery(BaseModel):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)
    desc = models.TextField(_("Description"))
    image = models.ImageField(default="fallback.jpg", upload_to="products/")