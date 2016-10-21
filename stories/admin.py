from django.contrib import admin
from .models import Story,Themes, Reader, Reading
# Register your models here.


class StoryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "type"]
    list_filter = ["type"]
    search_fields = ["type", "title", "themes"]

    class Meta:
        model = Story
admin.site.register(Story, StoryModelAdmin)
admin.site.register(Themes)
admin.site.register(Reading)
admin.site.register(Reader)