from django.contrib import admin
from django.utils.safestring import mark_safe
from main import models
from .models import Image, Question

# admin.site.register(models.Question)
# admin.site.register(models.Image)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    search_fields = ["name"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "image_show", "file"]

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format((obj.image.url)))
        return "None"

    image_show.__name__ = "Picture"
