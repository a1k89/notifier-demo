from django.contrib import admin
from django.db.models import DateTimeField


from .models import \
    Article, \
    ArticleComment, \
    Gift


models = [Article, ArticleComment, Gift, ]


class ReadonlyAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True


for model in models:
    admin.site.register(model, ReadonlyAdmin)
