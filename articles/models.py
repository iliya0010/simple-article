from django.db import models
from utilities.models import TimeStampedModel
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from utils.filename_to_hash import MediaNameToHash
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Article(TimeStampedModel):
    DRAFT = "D"
    PUBLISHED = "P"
    STATUS = (
        (DRAFT, _("Draft")),
        (PUBLISHED, _("Published")),
    )
    title = models.CharField(max_length=255, null=False, verbose_name=_("title"))
    slug = AutoSlugField(
        populate_from="title", unique_with=_("created"), verbose_name=_("slug")
    )
    tags = TaggableManager()
    status = models.CharField(
        max_length=1, choices=STATUS, default=DRAFT, verbose_name=_("status")
    )
    create_user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name=_("created by")
    )
    article_preview_image = models.ImageField(
        upload_to=MediaNameToHash("images"),
        verbose_name=(_("Article preview image")),
        null=True,
    )
    article_preview_image_thumbnail = ImageSpecField(
        source="article_preview_image",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    content = RichTextUploadingField(max_length=900, verbose_name=_("content"))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        ordering = ("created",)
